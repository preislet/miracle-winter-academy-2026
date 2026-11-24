# Version control with Git

<div class="session-meta" markdown>
:material-calendar: Monday 30 Nov, 13:45–15:15
:material-account-group: <span class="pill basic">Basic</span> <span class="pill advanced">Advanced</span> (parallel rooms)
:material-human-male-board: MIRACLE Research Software Engineering team
:material-laptop: Practical
</div>

!!! abstract "Draft, to be confirmed by instructors"

When an AI agent edits your code, you need to see *exactly* what it changed and be able to undo
it. Git gives you that. This session builds the **review loop** used for the rest of the week:

> **commit → let the agent work → read the diff → keep or revert**

!!! info "Before this session"
    [Git installed and configured](../prerequisites/git.md), GitHub account, `gh auth status`
    shows you are logged in.

=== "Basic"

    ### Learning goals

    - Explain what a repository, a commit and a diff are
    - Record changes with `git add` and `git commit`, and inspect history with `git log`
    - Read a diff and decide whether a change is acceptable
    - Undo changes safely: discard uncommitted edits, revert a commit
    - Create and switch branches to try things without risk

    ### What we will do

    1. **Why version control?** The `analysis_final_v3_REALLY_final.R` problem.
    2. **Your first repository.** `git init` a small R project, check `git status`, make the
       first commit.
    3. **Change → diff → commit.** Edit a script in RStudio, read `git diff`, commit with a
       meaningful message. Also use RStudio's Git pane for the same steps.
    4. **Undo.** Break something on purpose, then recover with `git restore` and `git revert`.
    5. **Branches.** Try an experimental change on a branch, compare it, merge or delete it.
    6. **Reviewing AI-generated changes.** Let the agent modify a script. Read its diff line by
       line, decide what to keep, and revert the rest.
    7. **Push to GitHub.** Create a repository with `gh repo create` and push your work.

    ### Materials

    - *Exercise repository: to be added*
    - *Slides: to be added*

=== "Advanced"

    ### Learning goals

    - Work with branches, merges and pull requests in a shared repository
    - Use `git worktree` to run several AI agents in parallel without them colliding
    - Run automated tests before merging changes
    - Review an AI-generated pull request critically

    ### What we will do

    1. **Quick recap** of the review loop: commit, diff, revert.
    2. **Collaborative workflow.** Fork or clone a shared course repository, create feature
       branches, open pull requests on GitHub, review a colleague's PR, resolve a merge conflict.
    3. **Worktrees for parallel agents.** Create two worktrees from one repository, run an agent
       in each on a different task, then compare and merge the results.
    4. **Tests as a gate.** Add `testthat` (R) or `pytest` (Python) tests, run them before merging,
       and see a test catch an agent's subtle bug.
    5. **Optional: continuous integration.** A minimal GitHub Actions workflow that runs the tests
       on every pull request.

    ### Materials

    - *Shared exercise repository: to be added*
    - *Slides: to be added*

## Further reading

- [Pro Git book](https://git-scm.com/book/en/v2), chapters 1–3
- [Happy Git and GitHub for the useR](https://happygitwithr.com/)
