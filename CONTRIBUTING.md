# Contributing

## Add a role plugin

1. Copy the layout of `plugins/engineering` to `plugins/<role>`.
2. Set the name and description in `plugins/<role>/.claude-plugin/plugin.json`.
3. Add the plugin to `.claude-plugin/marketplace.json`.
4. Add a `/<role>:test` command that checks every MCP server of the plugin.
5. Write the plugin README with the setup steps.
6. Run `claude plugin validate .` before you open a PR.

## Rules

- Each plugin stands alone. Do not depend on another role plugin.
- Never put a secret in `.mcp.json`. Use OAuth or `${ENV_VAR}`.
- Bump `version` in `plugin.json` when you change a plugin.
- Keep commands and skills read-only unless their purpose is to write.

## Try a plugin locally

```
/plugin marketplace add ./path/to/lendwellai
/plugin install <role>@lendwellai
```
