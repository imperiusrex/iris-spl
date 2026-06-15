# IRIS SPL

**IRIS SPL** is an AI-powered security solution that utilizes **AI for Splunk Apps**, **Splunk MCP Server**, **Splunk AI Assistant**, and **Splunk AI Toolkit**.


# Example Python Project

Objective: a single Python entrypoint where an analyst can type:

“Investigate failed logins from suspicious IPs in the last 60 minutes and summarize top users and sources.”

**IRIS SPL** then:

1. Uses Splunk AI Assistant (SAIA) to:
  * Generate safe SPL
  * Optionally explain/optimize it
2. Uses Splunk MCP Server to:
  * Execute the SPL with guardrails
  * Return JSON results
3. Uses a Python AI SDK / LLM to:
  * Summarize findings
  * Suggest next steps or automated actions

So the workflow shows: “natural language → SPL → results → AI summary” for security investigations.
