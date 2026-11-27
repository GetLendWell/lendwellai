---
description: Check that the engineer plugin and every MCP connection work
---

Run a read-only health check of each MCP server from the engineer plugin.

The servers are: atlassian, notion, posthog, bigquery.

For each server:

1. Find its tools. They are named `mcp__plugin_engineer_<server>__<tool>`.
2. Call the cheapest read-only tool that proves you are signed in. Good choices:
   - atlassian: get the current user info
   - notion: get the current user (self)
   - posthog: list projects or get the current organization
   - bigquery: list dataset ids
3. Never call a tool that creates, edits, sends or deletes anything.

Call the servers in parallel. One failure must not stop the other checks.

Then print one table with these columns: Server, Status (pass or fail), Detail.

- On pass, Detail is who you are signed in as, or what the call returned in a few words.
- On fail, Detail is the short error and the fix from the plugin README.
- If a server has no tools at all, mark it fail with "not connected, run /mcp".

End with one line: how many servers passed out of four.
