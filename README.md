# lendwellai

Common AI infrastructure for LendWell.

This repo is a Claude Code plugin marketplace. Each persona gets its own plugin.

## Plugins

| Plugin | Persona | Status |
|---|---|---|
| [engineer](plugins/engineer) | Engineer | Available |

## Install

Add the marketplace once:

```
/plugin marketplace add GetLendWell/lendwellai
```

Then install the plugin for your persona:

```
/plugin install engineer@lendwellai
```

Each plugin README has its own setup steps.

## Versions

Each plugin has its own semver version and release tag, for example `engineer-v0.0.1`.

The marketplace always points at the latest release, never at `main`.

To get a new release, run `/plugin marketplace update lendwellai`, then update the plugin in `/plugin`.

## Layout

```
lendwellai/
├── .claude-plugin/
│   └── marketplace.json      # lists every persona plugin, pinned to release tags
├── release-please-config.json  # one release package per persona
├── .release-please-manifest.json
├── scripts/
│   └── pin_marketplace.py    # pins and checks marketplace refs
└── plugins/
    └── <persona>/
        ├── .claude-plugin/
        │   └── plugin.json   # name, version, description
        ├── .mcp.json         # MCP connections for this persona
        ├── commands/         # slash commands
        ├── skills/           # skills
        ├── CHANGELOG.md      # generated on release
        └── README.md         # setup for this persona
```

## This repo is public

Never commit secrets, tokens, internal prompts or customer data.

Credentials come from OAuth or from environment variables on each machine.

See [CONTRIBUTING.md](CONTRIBUTING.md) to add a persona or change a plugin.
