#!/usr/bin/env python3
"""Refresh README skill table from data/skills.json with GitHub metadata."""

from __future__ import annotations

import json
import os
import re
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from urllib import error, request

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "skills.json"
README_FILE = ROOT / "README.md"
START_MARKER = "<!-- SKILLS_TABLE_START -->"
END_MARKER = "<!-- SKILLS_TABLE_END -->"
DATE_START = "<!-- LAST_UPDATED -->"
DATE_END = "<!-- LAST_UPDATED_END -->"


@dataclass
class Skill:
    name: str
    repo_url: str
    providers: list[str]
    categories: list[str]
    description: str
    stars: int | None = None
    latest_release: str = "-"

    @property
    def repo_slug(self) -> str:
        match = re.search(r"github\.com/([^/]+/[^/]+?)(?:\.git|/)?$", self.repo_url)
        if not match:
            raise ValueError(f"Invalid GitHub URL: {self.repo_url}")
        return match.group(1)


def _headers() -> dict[str, str]:
    token = os.getenv("GITHUB_TOKEN")
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "agent-skills-updater",
    }
    if token:
        headers["Authorization"] = "Bearer " + token
    return headers


def _fetch_json(url: str) -> dict | None:
    req = request.Request(url, headers=_headers())
    try:
        with request.urlopen(req, timeout=20) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except error.HTTPError as exc:
        if exc.code == 404:
            return None
        print(f"Warning: failed request {url}: HTTP {exc.code}", file=sys.stderr)
        return None
    except Exception as exc:  # noqa: BLE001
        print(f"Warning: failed request {url}: {exc}", file=sys.stderr)
        return None


def load_skills() -> list[Skill]:
    raw = json.loads(DATA_FILE.read_text(encoding="utf-8"))
    skills = []
    for item in raw:
        skills.append(
            Skill(
                name=item["name"],
                repo_url=item["repo"],
                providers=item["providers"],
                categories=item["categories"],
                description=item["description"],
            )
        )
    return skills


def enrich(skill: Skill) -> Skill:
    repo = _fetch_json(f"https://api.github.com/repos/{skill.repo_slug}")
    if repo:
        skill.stars = repo.get("stargazers_count")
    release = _fetch_json(f"https://api.github.com/repos/{skill.repo_slug}/releases/latest")
    if release and release.get("tag_name"):
        skill.latest_release = release["tag_name"]
    return skill


def markdown_table(skills: list[Skill]) -> str:
    lines = [
        "| Skill | Providers | Categories | Stars | Latest release | Description |",
        "|---|---|---|---:|---|---|",
    ]
    for skill in sorted(skills, key=lambda s: (s.stars or -1), reverse=True):
        stars = f"{skill.stars:,}" if skill.stars is not None else "-"
        providers = ", ".join(f"`{p}`" for p in skill.providers)
        categories = ", ".join(f"`{c}`" for c in skill.categories)
        lines.append(
            "| "
            f"[{skill.name}]({skill.repo_url}) | {providers} | {categories} | {stars} | "
            f"{skill.latest_release} | {skill.description} |"
        )
    return "\n".join(lines)


def replace_section(readme: str, start: str, end: str, content: str) -> str:
    pattern = re.compile(f"{re.escape(start)}.*?{re.escape(end)}", re.DOTALL)
    replacement = f"{start}\n{content}\n{end}"
    if not pattern.search(readme):
        raise ValueError(f"Markers not found: {start} ... {end}")
    return pattern.sub(replacement, readme)


def replace_last_updated(readme: str) -> str:
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    pattern = re.compile(f"{re.escape(DATE_START)}.*?{re.escape(DATE_END)}")
    return pattern.sub(f"{DATE_START}{today}{DATE_END}", readme)


def main() -> int:
    skills = [enrich(skill) for skill in load_skills()]
    readme = README_FILE.read_text(encoding="utf-8")
    readme = replace_section(readme, START_MARKER, END_MARKER, markdown_table(skills))
    readme = replace_last_updated(readme)
    README_FILE.write_text(readme, encoding="utf-8")
    print(f"Updated {README_FILE}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
