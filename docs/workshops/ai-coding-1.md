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

    ### Working on a real project with an agent

    #### Learning goals

    - Explain what an agent is made of and why tests give it a verifiable goal
    - Structure a project so that an agent can find, place and test code
    - Write and test a project instruction file (`CLAUDE.md` / `AGENTS.md`)
    - Refactor a legacy script with an agent in small, reviewed steps against a reference output
    - Judge when a workflow plugin (Superpowers) helps and when it slows you down

    #### What we will do

    All in one small Python project, `cbc-toolkit`, using the same synthetic blood counts as in the
    morning.

    1. **Agents and programming with them** (slides): model vs agent, the agent loop, test-driven
       development, a workflow that keeps you in charge.
    2. **Project structure:** a tour of the project with the agent.
    3. **Instruction files:** write a `CLAUDE.md` and test whether the agent follows it.
    4. **Refactor:** turn `scripts/old_report.py` into reusable, tested functions, one reviewed step
       at a time.
    5. **Superpowers:** do the next step with the plugin and compare.

    ??? info "Notes from the slides"

        **Model vs agent.** The model is stateless and only produces text: it knows only what is in
        its context window. An agent is model + tools + memory + harness (here: Claude Code), and
        acts on your files in a loop until it decides the goal is met.

        **A verifiable goal makes the loop work.** "The tests pass" or "the output equals the
        reference" can be checked by the agent; "make it nicer" cannot. Agents work best with a
        clear specification, a tight feedback loop, well-structured code and such a goal.

        **Verification vs validation.** *Are we building the product right?* (tests, review,
        reference output) can largely be delegated. *Are we building the right product?* (right
        units, thresholds, question) stays with you.

        **Test-driven development.** Red: write a failing test. Green: the minimal code to pass it.
        Refactor: clean up while the tests stay green. Tests express requirements: don't let the
        agent change them to fit the code.

        **Workflow.** Explore → plan → implement in small steps → review the diff → commit. New task,
        new session (`/clear`). Don't take on more *comprehension debt* than you can pay back: you
        should be able to explain the code.

        **Project structure.** A conventional layout (`data/`, `src/`, `tests/`, `scripts/`) lets
        the agent find the right file without reading everything, know where new code belongs and
        check its work with tests. In R the same roles are played by `R/`, `tests/testthat/`,
        `DESCRIPTION` and `renv.lock`.

        **Instruction files.** `CLAUDE.md` (Claude Code) or `AGENTS.md` (the shared standard; reuse
        it from `CLAUDE.md` with the line `@AGENTS.md`) hold what you'd tell a new colleague: layout,
        commands, rules. Short, true, versioned in git, and tested with a small task.

        **Superpowers.** A plugin that enforces brainstorm → plan → implement (TDD) → review. Worth
        it for unclear or larger tasks; overkill for a one-line fix.

    ??? abstract "Part 1: Setup and tour"

        ##### Get the project

        The project is in the course materials repository, in
        `Miracle-Winter-Academy/miracle-ai-assisted-coding-I-advanced/code`. Copy it into
        `~/miracle-academy` under the name `cbc-toolkit` and make it its own git repository.
        Replace `<course-materials>` with the folder where you cloned the repository:

        ```bash
        cp -r <course-materials>/Miracle-Winter-Academy/miracle-ai-assisted-coding-I-advanced/code ~/miracle-academy/cbc-toolkit
        cd ~/miracle-academy/cbc-toolkit
        git init
        git add .
        git commit -m "cbc-toolkit as handed over"
        ```

        ##### Check that it runs

        ```bash
        conda activate miracle
        python -m pytest
        python scripts/old_report.py
        head -4 results/report.csv
        ```

        ```text
        4 passed
        done 18
        patient_id,sex,visits,mean_wbc,mean_anc,min_hgb,neutropenic_visits,anaemic
        P001,M,4,6.4,3.62,140,0,no
        P002,F,4,7.32,4.38,125,0,no
        P003,M,4,2.93,1.49,142,3,no
        ```

        | Path | Role |
        |---|---|
        | `data/cbc_samples.csv` | input data, read-only |
        | `src/cbc/` | reusable functions: `io.py` (reading), `flags.py` (ANC, neutropenia, anaemia) |
        | `tests/test_cbc.py` | tests for `src/cbc/` |
        | `scripts/old_report.py` | legacy report script: one long block, no functions, no tests |
        | `pyproject.toml` | dependencies and pytest settings |

        ##### Ask the agent

        Start `claude` in the project folder and ask:

        > Where is the absolute neutrophil count calculated, and how is it tested?

        Then `/clear` and ask:

        > What does scripts/old_report.py do? Does it reuse anything from src/?

        Compare the two answers: how many files did the agent read, and how sure was it? The first
        answer comes from a function with a name and a test; the second one has to be reconstructed
        from 65 lines of loops. The agent should also notice that `old_report.py` **re-implements**
        the ANC and the anaemia thresholds instead of using `src/cbc/`.

    ??? abstract "Part 2: Instruction files"

        ##### Let the agent write a first version

        In Claude Code, run `/init`. It reads the project and writes `CLAUDE.md`. Open it in your
        editor and read it critically: what is useful, what is noise, what is missing?

        ##### Make it yours

        Edit `CLAUDE.md`. Keep it short; every line is read at the start of every session. It
        should at least say:

        - **Layout:** what is in `data/`, `src/cbc/`, `tests/`, `scripts/`
        - **Units:** `hgb` in g/L, `wbc` in 10^9/L, `neut_pct` in %
        - **Commands:** `conda activate miracle`, `python -m pytest`
        - **Rules:** never modify `data/`; new functions go to `src/cbc/` and get a test; don't
          change existing tests to make them pass; end with a 3-bullet summary of the change

        ??? example "One possible CLAUDE.md"

            ```markdown
            # cbc-toolkit
            Synthetic CBC data of 18 patients, 4 visits each.
            Units: hgb g/L, wbc and plt 10^9/L, neut_pct %.

            ## Layout
            - src/cbc/: reusable functions; scripts/: entry points only
            - data/: input, never modify
            - tests/: pytest tests for src/cbc/

            ## Commands
            - conda activate miracle
            - python -m pytest

            ## Rules
            - Every new function in src/cbc/ gets a test in tests/
            - Do not change existing tests to make them pass
            - End with a 3-bullet summary of what you changed
            ```

        **Optional, if you also use other agents:** keep the content in `AGENTS.md` and let
        `CLAUDE.md` import it:

        ```bash
        mv CLAUDE.md AGENTS.md
        echo "@AGENTS.md" > CLAUDE.md
        ```

        Commit it. Instructions are part of the project; changes to them are reviewed like code:

        ```bash
        git status                   # only CLAUDE.md (and AGENTS.md) should be new
        git add .
        git commit -m "Add instructions for coding agents"
        ```

        ##### Test it

        `/clear`, then:

        > Add a function that counts samples with low platelets (below 150).

        Check with `git status` and `git diff`:

        - [ ] the function is in `src/cbc/`, not in a script
        - [ ] there is a new test, and the agent ran the tests
        - [ ] nothing in `data/` changed
        - [ ] it ended with a 3-bullet summary

        If a rule was ignored: is it unclear, or buried? Fix `CLAUDE.md`, not the prompt. Commit the
        result if you're happy with it, or throw it away with `git restore .` and `git clean -fd`.

    ??? abstract "Part 3: Refactor `old_report.py` step by step"

        The goal: `old_report.py` uses the functions in `src/cbc/`, the per-patient summary becomes a
        tested function, and the script only loads, summarises and writes. **The output must not
        change.**

        Every step ends with the same routine:

        ```bash
        git diff                                         # read what changed
        python -m pytest                                 # tests still pass?
        python scripts/old_report.py                     # run the script
        diff reference/report.csv results/report.csv && echo "same output"
        git commit -am "<what this step did>"            # checkpoint
        ```

        If a step goes wrong, `git restore .` takes you back to the last commit.

        ##### Step 0: save the reference

        The legacy script has no tests. Its current output is the only specification you have, so
        save it before you change anything:

        ```bash
        mkdir reference
        cp results/report.csv reference/report.csv
        git add reference
        git commit -m "Reference output of old_report.py"
        ```

        ##### Step 1: reuse what exists

        > In scripts/old_report.py, replace the code that duplicates src/cbc (reading the CSV, the
        > ANC, the neutropenia and anaemia thresholds) with calls to those functions. Change nothing
        > else. Don't commit.

        !!! warning "A decision you have to make"
            `python scripts/old_report.py` cannot import `cbc` from `src/` on its own
            (`ModuleNotFoundError: No module named 'cbc'`). The agent will propose a fix: editing
            `sys.path` in the script, setting `PYTHONPATH`, or installing the project with
            `pip install -e .`. Ask it to explain the trade-offs, choose one (`pip install -e .` into
            the `miracle` environment is the standard way), and add the command to `CLAUDE.md`.

        ##### Step 2: a tested function for the summary

        Use test-driven development: the test comes first. You don't have to write it yourself;
        let the agent write it, and you read it:

        > Write a test in tests/ for a new function patient_report(samples) in src/cbc/report.py.
        > It should return one row per patient with the same columns as results/report.csv. Run the
        > test and show me that it fails. Don't implement the function yet.

        Read the test. Does it check what matters (columns, one row per patient, a few known
        values)? Then:

        > Now implement patient_report so that the test passes, without changing the test.

        ##### Step 3: a thin script

        > Make scripts/old_report.py a thin entry point: load the samples, call patient_report,
        > write results/report.csv. Remove dead code.

        ##### Step 4: compare with the reference

        Run the routine one last time. `diff` should print nothing except `same output`.

        ??? question "`diff` shows a few means that differ by 0.01"
            The old script rounds with Python's `round()`, pandas uses its own `.round()`, and the
            two can disagree on values that sit exactly halfway (e.g. a mean of 2.925). Neither is
            a bug in the data, but the output changed, and the reference caught it. Ask the agent to
            explain it, decide which behaviour you keep, and write the decision in the commit
            message. This is exactly what a reference output is for.

    ??? abstract "Part 4: Superpowers"

        [Superpowers](https://github.com/obra/superpowers) is a plugin that makes the agent follow a
        process: brainstorm (questions and a design), plan (small tasks, tests first), implement,
        review.

        ##### Install

        In Claude Code:

        ```text
        /plugin install superpowers@claude-plugins-official
        ```

        Exit with `/exit` and start `claude` again so the plugin is loaded.

        ##### The next step, with Superpowers

        > Make the report runnable on any CBC file: input and output paths as command-line
        > arguments, with the current paths as defaults.

        Answer its questions, read the design and the plan **before** you let it implement, then
        review the result as in Part 3 (diff, tests, reference). If it wants to create a git
        worktree or start subagents, you can tell it to work in the current folder.

        **Discussion:** for which of your own tasks would you switch it on, and for which off?
        You can turn it off again with `/plugin`.

## Materials

- <span class="pill advanced">Advanced</span> Exercise project: `Miracle-Winter-Academy/miracle-ai-assisted-coding-I-advanced/code` in the course materials repository
- <span class="pill advanced">Advanced</span> Slides: `Miracle-Winter-Academy/miracle-ai-assisted-coding-I-advanced/presentations/ai_assisted_coding_I_advanced.pptx` in the course materials repository
- [Claude Code documentation](https://code.claude.com/docs)
