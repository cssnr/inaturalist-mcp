# Agents - inaturalist-mcp

An MCP server exposing iNaturalist taxonomy data via the Model Context Protocol.

SDK: https://github.com/modelcontextprotocol/python-sdk

## Commands

This project uses `toml-run` — run any `[tool.scripts]` entry by name:

| Command      | What it does                                 |
| ------------ | -------------------------------------------- |
| `run build`  | hatch build                                  |
| `run cli`    | python -m inaturalist_mcp                    |
| `run dev`    | uvicorn w/ --reload                          |
| `run server` | uvicorn w/ --host 0.0.0.0                    |
| `run lint`   | Full lint: should always be used to lint     |
| `run format` | Full format: should always be used to format |
