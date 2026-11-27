# AI-assisted coding I

<div class="session-meta" markdown>
:material-calendar: Tuesday 1 Dec, 13:15–14:45
:material-account-group: <span class="pill basic">Basic</span> <span class="pill advanced">Advanced</span> (parallel rooms)
:material-laptop: Practical

:material-human-male-board: <span class="pill basic">Basic</span> Luděk Svoboda, Jan Stuchlý &nbsp;&nbsp; <span class="pill advanced">Advanced</span> Sára Veselá, Tomáš Preisler
</div>

!!! abstract "Draft, to be confirmed by instructors"

How to work with an AI coding agent: what it is, how it works and how to give it the right
context. The Advanced track also uses **project instruction files**
(`AGENTS.md`, `CLAUDE.md`) and **plugins** such as
[Superpowers](https://github.com/obra/superpowers), which add structured workflows like
planning, test-driven development and code review.

!!! info "Before this session"
    [Claude Code](../prerequisites/claude-tools.md) installed and logged in. Monday's
    [Git](git.md) review loop is assumed.

=== "Basic"

    ### Learning goals

    - Understand the basic concepts: LLM, token, agent, context window, harness
    - Work with an agent (Claude Code): key commands, plan mode
    - Give the agent the right context, and keep out what is stale or irrelevant
    - Read what the agent reports and what it writes for itself (notes, plans), and check it
      before you rely on it
    - Know the risks: made-up answers, leaked data, deleted files

    ### What we will do

    1. **Basic concepts:** what an AI agent is, what it costs, and how to keep it safe.
    2. **First steps with Claude Code:** let the agent build a small app for synthetic blood
       count data, then check what it flagged and why.
    3. **Working with context:** run the same task with too little, the right, and stale
       context, and compare the results.
    4. **`CLAUDE.md` and plan mode:** tell the agent about your project once, and agree on a
       plan before it writes code.

=== "Advanced"

    ### Learning goals

    - Structure an analysis project so that an agent can work in it reliably
    - Use the agent to write reusable functions, tests and documentation
    - Use project instruction files and plugins to enforce conventions
    - Keep the agent's work reproducible (`renv`, Git, tests)

    ### What we will do

    1. **Project structure for agents:** `R/`, `data/`, `scripts/`, `tests/`, `renv.lock`. Why a
       clear layout makes the agent better.
    2. **Instruction files:** write `CLAUDE.md` / `AGENTS.md` with architecture notes, commands to
       run tests and rules the agent must follow.
    3. **Refactor with an agent:** turn a messy monolithic script into reusable functions with
       `testthat` tests, step by step, reviewing each diff.
    4. **Plugins:** Superpowers workflows (brainstorm → plan → implement → review), and when they
       help or slow you down.

## Materials

- *Exercise projects: to be added*
- [Claude Code documentation](https://code.claude.com/docs)
