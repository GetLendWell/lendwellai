# engineer

The Claude Code plugin for the LendWell engineer persona.

It gives you our MCP connections and the `/engineer:test` command.

## Install

```
/plugin marketplace add GetLendWell/lendwellai
/plugin install engineer@lendwellai
```

Restart Claude Code after installing.

## Setup

For GitHub, use the `gh` CLI. Claude Code calls it directly, so there is no GitHub MCP server.

```sh
gh auth login
```

BigQuery uses your Google login. Run this once:

```sh
gcloud auth application-default login
gcloud auth application-default set-quota-project lendwell-ie
```

The second command tells Google which project to count your API calls against. Without it, some Google APIs fail with "quota exceeded" or "API not enabled".

BigQuery also needs Node.js, because it runs through `npx`.

It queries the `lendwell-ie` project by default. To change it, set `BIGQUERY_PROJECT` in your shell profile.

The other servers use OAuth in the browser. Run `/mcp`, pick each server and sign in.

## MCP servers

| Server | Used for | Auth |
|---|---|---|
| atlassian | Jira and Confluence | OAuth |
| notion | Proposals and docs | OAuth |
| posthog | Product analytics (EU cloud) | OAuth |
| bigquery | GCP logs and data | Google application default credentials |

## Check your setup

```
/engineer:test
```

It calls one read-only tool on every server and prints a pass or fail table.

## Troubleshooting

- **A server shows no tools.** Run `/mcp` and sign in to it.
- **bigquery fails with `invalid_grant` or `invalid_rapt`.** Your Google login expired. Run `gcloud auth application-default login` again.
- **bigquery fails with "quota exceeded" or "API not enabled".** Run `gcloud auth application-default set-quota-project lendwell-ie`.
- **bigquery fails to start.** Check that Node.js is installed.
- **You see every tool twice.** The same server is also on in your claude.ai connectors. Turn one of them off.

## Not included yet

- **Slack.** Slack needs a pre-registered LendWell Slack app before Claude Code can sign in. Until then, use the Slack connector in claude.ai.
