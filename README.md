# lendwellai

Common AI infrastructure for LendWell.

This repo is a Claude Code plugin marketplace. Each role gets its own plugin.

## Plugins

| Plugin | For | Status |
|---|---|---|
| [engineering](plugins/engineering) | Engineers | Available |

## Install

Add the marketplace once:

```
/plugin marketplace add GetLendWell/lendwellai
```

Then install the plugin for your role:

```
/plugin install engineering@lendwellai
```

Each plugin README has its own setup steps.

## Layout

```
lendwellai/
├── .claude-plugin/
│   └── marketplace.json      # lists every role plugin
└── plugins/
    └── <role>/
        ├── .claude-plugin/
        │   └── plugin.json   # name, version, description
        ├── .mcp.json         # MCP connections for this role
        ├── commands/         # slash commands
        ├── skills/           # skills
        └── README.md         # setup for this role
```

## This repo is public

Never commit secrets, tokens, internal prompts or customer data.

Credentials come from OAuth or from environment variables on each machine.

See [CONTRIBUTING.md](CONTRIBUTING.md) to add a role or change a plugin.
