# AI-assisted coding I

<div class="session-meta" markdown>
:material-calendar: Tuesday 1 Dec, 13:15–14:45
:material-account-group: <span class="pill basic">Basic</span> <span class="pill advanced">Advanced</span> (parallel rooms)
:material-human-male-board: MIRACLE Research Software Engineering team
:material-laptop: Practical
</div>

!!! abstract "Draft, to be confirmed by instructors"

How to give an AI coding agent good instructions, and how to check what it produces. Both tracks
use **project instruction files** (`AGENTS.md`, `CLAUDE.md`), which tell the agent about your
project once so you don't repeat yourself, and **plugins** such as
[Superpowers](https://github.com/obra/superpowers), which add structured workflows like
planning, test-driven development and code review.

!!! info "Before this session"
    [Claude Code](../prerequisites/claude-tools.md) installed and logged in. Monday's
    [Git](git.md) review loop is assumed.

=== "Basic"

    ### Learning goals

    - Write clear, specific instructions for a coding agent
    - Create a project instruction file describing your data, conventions and rules
    - Install and use a plugin (Superpowers)
    - Interpret and verify the analysis code the agent generates

    ### What we will do

    1. **Anatomy of a good prompt:** context, goal, constraints, definition of done. Compare a vague
       and a precise prompt on the same task.
    2. **`CLAUDE.md` / `AGENTS.md`:** write one for a small R analysis project (data location,
       packages to use, "never modify `data/raw/`", style rules), then watch the agent follow it.
    3. **Plugins:** install Superpowers and let it *plan before coding*.
    4. **Verify, don't trust:** the agent writes an analysis in R. You check it by reading the
       diff, re-running it, checking numbers by hand and asking the agent to explain each step.

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
