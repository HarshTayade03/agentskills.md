# Contributing

Thanks for helping grow this agent skills library.

## Add a new skill

1. Edit `data/skills.json`
2. Add an entry with this shape:

```json
{
  "name": "Skill Name",
  "repo": "https://github.com/owner/repo",
  "providers": ["Claude"],
  "categories": ["Data"],
  "description": "Short practical summary"
}
```

## Tagging rules

- `providers` must include one or more: `Claude`, `Gemini`, `OpenAI`, `Multi`
- `categories` should describe practical use-cases (for example: `Video Editing`, `Photo Editing`, `Website Builder`, `Excel`, `Data`, `Fashion`, `Token Optimization`)

## Validation

Run:

```bash
python scripts/update_skills_readme.py
```

This refreshes the generated table in `README.md`.

## Review expectations

PRs should add real, public repositories and include clear provider/category tags.
