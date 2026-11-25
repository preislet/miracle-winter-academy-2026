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

    ### Build a small analysis workflow

    #### Learning goals

    - Develop a small, complete R analysis workflow together with an agent
    - Review every code change with Git before accepting it
    - Recognise when the agent is wrong and steer it back

    #### What we will do

    1. Start from a dataset and a research question (provided).
    2. Ask the agent for a plan first; agree on the steps before any code is written.
    3. Build the workflow in small steps (load, clean, summarise, plot, test) and **commit
       after each accepted step**.
    4. Review each change with `git diff` and revert anything you don't understand.
    5. Finish with a script that runs from start to end and a short README written with the agent.

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
