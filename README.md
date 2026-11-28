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
| [ComfyUI](https://github.com/comfyanonymous/ComfyUI) | `Multi` | `Photo Editing`, `Video Editing`, `Fashion` | 148,954 | v0.46.0 | Node-based visual generation workflows for image/video creative pipelines. |
| [browser-use](https://github.com/browser-use/browser-use) | `Multi` | `Website Builder`, `Data` | 122,251 | 1.0.9 | Browser automation toolkit for web-native agent skills. |
| [OpenHands](https://github.com/All-Hands-AI/OpenHands) | `Multi` | `Website Builder`, `Automation` | 94,474 | v1.46.0 | Software engineering agent platform for coding and task execution. |
| [Model Context Protocol Servers](https://github.com/modelcontextprotocol/servers) | `Multi` | `Data`, `Excel` | 92,305 | v2.6.0 | Reusable MCP servers that expand agent tool capabilities. |
| [OpenAI Cookbook](https://github.com/openai/openai-cookbook) | `OpenAI` | `Data`, `Token Optimization` | 77,543 | - | Practical patterns for OpenAI-powered agents and tools. |
| [AutoGen](https://github.com/microsoft/autogen) | `Multi` | `Automation`, `Data` | 61,967 | python-v0.7.5 | Multi-agent framework for orchestrating autonomous workflows. |
| [crewAI](https://github.com/crewAIInc/crewAI) | `Multi` | `Automation`, `Website Builder` | 61,334 | 1.15.45 | Agent role-based orchestration for production automation tasks. |
| [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook) | `Claude` | `Token Optimization`, `Data` | 55,352 | - | Claude-focused skill patterns and implementation recipes. |
| [LangGraph](https://github.com/langchain-ai/langgraph) | `Multi` | `Data`, `Automation` | 45,524 | cli==0.4.44 | Stateful graph framework for reliable long-running agents. |
| [Google Generative AI Python](https://github.com/google-gemini/generative-ai-python) | `Gemini` | `Data`, `Automation` | 2,331 | v0.8.6 | Gemini SDK examples for building agentic workflows. |
<!-- SKILLS_TABLE_END -->

_Last updated: <!-- LAST_UPDATED -->2026-11-28<!-- LAST_UPDATED_END -->_

## Contributing

Contributions are welcome.

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for contribution steps and entry format.

Please keep entries:
- Real and public
- Clearly tagged
- Relevant to agentic workflows

## License

[MIT](LICENSE)
