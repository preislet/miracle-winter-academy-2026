# AI-assisted coding II

<div class="session-meta" markdown>
:material-calendar: Tuesday 1 Dec, 15:05–16:15
:material-account-group: <span class="pill basic">Basic</span> <span class="pill advanced">Advanced</span> (parallel rooms)
:material-laptop: Practical

:material-human-male-board: <span class="pill basic">Basic</span> Luděk Svoboda, Jan Stuchlý &nbsp;&nbsp; <span class="pill advanced">Advanced</span> Tomáš Preisler, Sára Veselá
</div>

!!! abstract "Draft, to be confirmed by instructors"

A hands-on project session that builds on [AI-assisted coding I](ai-coding-1.md). You direct the
agent on a real task and use Git to keep control of every change.

=== "Basic"

    ### Learning goals

    - Work in small steps: one task, test it yourself, commit
    - Test the result like a user and check a few values by hand
    - Set verifiable goals (expected output, reference data, tests), so the agent can check its own work

    ### What we will do

    1. **Small step and test:** continue with the app from session I, one change at a time.
    2. **Verifiable goals:** ask for neutropenia grading with no yardstick, then run the
       provided tests on it and see how many fail.
    3. **Let the agent check itself:** new session, the tests are now the goal. Watch the agent run
       them, fail and fix its code until they pass. Check with `git diff` that it did not change the tests.
    4. **Move the goalposts:** change the goal (new cases, a changed rule) by updating the
       tests first, then let the agent bring the code in line again.

=== "Advanced"

    ### Improve and extend an existing tool

    #### Learning goals

    - Get to know an unfamiliar codebase quickly with an agent's help
    - Fix, improve and extend a tool, possibly in a language you don't write yourself
    - Use tests and code review to keep changes safe

    #### What we will do

    1. Pick an existing open-source tool (provided, or bring your own).
    2. Ask the agent to explain the architecture: entry points, data flow, tests.
    3. Fix a known issue or add a small feature on a branch. Write a test first.
    4. Review the diff critically: does the code follow the project's style, and do all tests pass?
    5. Optional: run two agents in parallel worktrees on different improvements, then merge.

## Materials

- *Datasets and tool repositories: to be added*
