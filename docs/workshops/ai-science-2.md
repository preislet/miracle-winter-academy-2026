# AI-assisted science II

<div class="session-meta" markdown>
:material-calendar: Wednesday 2 Dec, 10:50–12:30
:material-account-group: <span class="pill basic">Basic</span> <span class="pill advanced">Advanced</span> (parallel rooms)
:material-human-male-board: MIRACLE Research Software Engineering team
:material-laptop: Practical
</div>

!!! abstract "Draft, to be confirmed by instructors"

Building on [Part I](ai-science-1.md): **agent harnesses and toolkits** (skills, tools and
workflows that turn a general agent into a scientific assistant) and the **Model Context Protocol
(MCP)**, the open standard through which agents connect to external tools and data such as
literature databases.

=== "Basic"

    ### Learning goals

    - Understand what a *harness* adds to a language model: tools, skills, memory, permissions
    - Use ready-made skills and workflows for scientific tasks
    - Understand what MCP is and use an existing MCP connector

    ### What we will do

    1. **Model vs agent vs harness:** what actually happens when you type a prompt in Claude Code.
    2. **Skills:** use a ready-made skill for a recurring scientific task and inspect what it
       contains.
    3. **Introduction to MCP:** connect a literature or biological database through an existing
       MCP connector and query it from the agent.
    4. **Trust check:** compare MCP-sourced answers with the agent's answers from memory.

=== "Advanced"

    ### Learning goals

    - Compose skills, tools and workflows into an agent toolkit for your own research
    - Connect the agent to external tools and data with MCP
    - Evaluate the risks of giving an agent access to real systems

    ### What we will do

    1. **Harness anatomy:** tools, skills, hooks, sub-agents; how they combine.
    2. **Write a skill** for a task from your own research and test it.
    3. **MCP integration:** configure several MCP servers (literature, databases, local files) and
       build a workflow that combines them.
    4. **Risk review:** what data leaves your machine, what the agent can change, and how to audit it.

## Materials

- *Skills, MCP configurations and exercises: to be added*
- [Model Context Protocol](https://modelcontextprotocol.io/)
