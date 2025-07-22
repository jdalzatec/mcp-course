MCP Course

```bash
uv sync
uv run mcp dev main.py
```

To run the tini-agents example:

```bash
uv run tiny-agents run agent.json
```

To use tini-agents, we need to pay for HF inference. However, we can use cursor as our Host, and use this MCP:

```json
{
  "mcpServers": {
    "playwright": {
        "command": "npx",
        "args": [
            "@playwright/mcp@latest"
        ]
    }
  }
}
```
