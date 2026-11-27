# Contributing

## Pull requests

Every change goes through a pull request. PRs are squash merged.

The PR title becomes the commit message. It must be a conventional commit:

```
feat(engineer): add deploy skill
fix(engineer): correct the PostHog check in /engineer:test
docs: explain the BigQuery setup
```

The type decides the next version:

| Type | Bump |
|---|---|
| `feat` | Minor |
| `fix` | Patch |
| `feat!` or `fix!` | Major, or minor while below 1.0.0 |
| `docs`, `chore`, `ci`, `refactor`, `test` | No release |

Use `!` when engineers must change something. Examples: a removed command, a renamed MCP server, a new setup step.

## Versions and releases

Each persona plugin has its own version. It follows semver.

Never edit these by hand:

- `version` in `plugin.json`
- `.release-please-manifest.json`
- `ref` in `.claude-plugin/marketplace.json`
- any `CHANGELOG.md`

release-please updates them all.

### How a release happens

1. A PR is merged to `main`.
2. release-please opens or updates a release PR for each changed persona.
3. A maintainer merges the release PR.
4. release-please tags the release, for example `engineer-v0.1.0`, and creates a GitHub release.
5. The release workflow pins the marketplace to the new tag.
6. Engineers get the new version on their next plugin update.

Merging to `main` alone changes nothing for engineers. Only a merged release PR does.

## Add a persona plugin

1. Copy the layout of `plugins/engineer` to `plugins/<persona>`.
2. Set the name, description and `"version": "0.0.1"` in its `plugin.json`.
3. Add `plugins/<persona>` to `release-please-config.json` and `.release-please-manifest.json`.
4. Add the plugin to `.claude-plugin/marketplace.json` with ref `<persona>-v0.0.1`.
5. Add a `/<persona>:test` command that checks every MCP server of the plugin.
6. Write the plugin README with the setup steps.
7. After merging, a maintainer creates the first tag `<persona>-v0.0.1`.

## Rules

- Each plugin stands alone. Do not depend on another persona plugin.
- Never put a secret in `.mcp.json`. Use OAuth or `${ENV_VAR}`.
- Keep commands and skills read-only unless their purpose is to write.

## Checks

CI runs these on every PR. Run them locally before you push:

```sh
claude plugin validate .
claude plugin validate plugins/<persona>
python3 scripts/pin_marketplace.py --check
```

## Try a plugin locally

The marketplace installs released tags, not your working copy. To test local changes, load the folder directly:

```sh
claude --plugin-dir ./plugins/<persona>
```

This loads the plugin for that session only. Uninstall the released copy first, or you will see every tool twice.
