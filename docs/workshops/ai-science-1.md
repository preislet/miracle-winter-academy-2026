# AI-assisted science I

<div class="session-meta" markdown>
:material-calendar: Wednesday 2 Dec, 09:00–10:30
:material-account-group: <span class="pill basic">Basic</span> <span class="pill advanced">Advanced</span> (parallel rooms)
:material-human-male-board: MIRACLE Research Software Engineering team
:material-laptop: Practical
</div>

!!! abstract "Draft, to be confirmed by instructors"

AI agents in scientific research with **Claude Science** and **Claude Code**. The focus is on
using agents for real scientific tasks *and* on knowing when not to trust them: sandboxing,
permissions and critical evaluation of results run through the whole session.

!!! info "Before this session"
    [Claude desktop app and Claude Code](../prerequisites/claude-tools.md) installed, with
    access to Claude Science (details from the organisers).

=== "Basic"

    ### Learning goals

    - Use an AI agent for literature search and simple scientific workflows
    - Understand what the agent can access (sandbox, permissions) and how to limit it
    - Check an agent's claims and citations critically

    ### What we will do

    1. **Literature search with an agent:** find and summarise recent papers on a MIRACLE-related
       question, then verify every citation actually exists and says what the agent claims.
    2. **A small scientific workflow:** load a dataset, explore it and produce a figure, with the
       agent working inside a sandboxed project folder.
    3. **Sandboxing and permissions in practice:** what happens when the agent asks to access files
       outside the project, run commands or reach the internet.
    4. **Spot the error:** examples where the agent's output looks convincing but is wrong.
       Discuss how to detect them.

=== "Advanced"

    ### Learning goals

    - Build multi-step scientific workflows with an agent
    - Integrate the agent with your existing tools and scripts
    - Configure sandboxing and permissions deliberately for sensitive data

    ### What we will do

    1. **Scientific workflow end to end:** from a question to analysis, figures and a methods
       paragraph, with the agent documenting software versions and parameters.
    2. **Tool integration:** let the agent use your own R/Python scripts and command-line tools.
    3. **Sandboxing and permissions:** configure allowed and denied actions, file system and network
       limits; discuss what is acceptable for pseudonymised medical data.
    4. **Critical evaluation:** reproduce the agent's result independently and compare.

## Materials

- *Datasets and prompts: to be added*
