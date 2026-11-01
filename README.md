# Agent Skills Library

A curated, community-driven list of **popular agentic skill repositories** across providers and use-cases.

Inspired by awesome-lists, this project tracks skills with consistent tags so users can quickly find the right repository by:
- **Provider/model** (Claude, Gemini, OpenAI, multi-provider, etc.)
- **Category** (video editing, photo editing, website building, excel, data, fashion, token minimization, and more)

## Repository Description

> Curated weekly-updated library of popular agentic skills repositories, tagged by provider and category.

## How this works

- Skills are stored in `data/skills.json`
- `scripts/update_skills_readme.py` refreshes metadata (stars + latest release)
- GitHub Actions runs automatic refreshes:
  - Weekly full refresh
  - Daily release polling to catch important releases quickly

## Tagging model

Each skill entry uses:
- `providers`: one or more tags like `Claude`, `Gemini`, `OpenAI`, `Multi`
- `categories`: one or more tags like `Video Editing`, `Photo Editing`, `Website Builder`, `Excel`, `Data`, `Fashion`, `Token Optimization`

## Skill List

<!-- SKILLS_TABLE_START -->
| Skill | Providers | Categories | Stars | Latest release | Description |
|---|---|---|---:|---|---|
| [ComfyUI](https://github.com/comfyanonymous/ComfyUI) | `Multi` | `Photo Editing`, `Video Editing`, `Fashion` | 144,459 | v0.43.0 | Node-based visual generation workflows for image/video creative pipelines. |
| [browser-use](https://github.com/browser-use/browser-use) | `Multi` | `Website Builder`, `Data` | 119,753 | 0.13.14 | Browser automation toolkit for web-native agent skills. |
| [OpenHands](https://github.com/All-Hands-AI/OpenHands) | `Multi` | `Website Builder`, `Automation` | 92,425 | v1.34.0 | Software engineering agent platform for coding and task execution. |
| [Model Context Protocol Servers](https://github.com/modelcontextprotocol/servers) | `Multi` | `Data`, `Excel` | 91,734 | v2.2.0 | Reusable MCP servers that expand agent tool capabilities. |
| [OpenAI Cookbook](https://github.com/openai/openai-cookbook) | `OpenAI` | `Data`, `Token Optimization` | 76,902 | - | Practical patterns for OpenAI-powered agents and tools. |
| [AutoGen](https://github.com/microsoft/autogen) | `Multi` | `Automation`, `Data` | 61,662 | python-v0.7.5 | Multi-agent framework for orchestrating autonomous workflows. |
| [crewAI](https://github.com/crewAIInc/crewAI) | `Multi` | `Automation`, `Website Builder` | 60,385 | 1.15.33 | Agent role-based orchestration for production automation tasks. |
| [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook) | `Claude` | `Token Optimization`, `Data` | 54,045 | - | Claude-focused skill patterns and implementation recipes. |
| [LangGraph](https://github.com/langchain-ai/langgraph) | `Multi` | `Data`, `Automation` | 44,274 | 1.2.19 | Stateful graph framework for reliable long-running agents. |
| [Google Generative AI Python](https://github.com/google-gemini/generative-ai-python) | `Gemini` | `Data`, `Automation` | 2,329 | v0.8.6 | Gemini SDK examples for building agentic workflows. |
<!-- SKILLS_TABLE_END -->

_Last updated: <!-- LAST_UPDATED -->2026-11-01<!-- LAST_UPDATED_END -->_

## Contributing

Contributions are welcome.

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for contribution steps and entry format.

Please keep entries:
- Real and public
- Clearly tagged
- Relevant to agentic workflows

## License

[MIT](LICENSE)
