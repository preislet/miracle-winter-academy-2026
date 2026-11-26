# Version control with Git

<div class="session-meta" markdown>
:material-calendar: Monday 30 Nov, 13:45–15:15
:material-account-group: <span class="pill basic">Basic</span> <span class="pill advanced">Advanced</span> (parallel rooms)
:material-laptop: Practical

:material-human-male-board: <span class="pill basic">Basic</span> Luděk Svoboda, Sára Veselá &nbsp;&nbsp; <span class="pill advanced">Advanced</span> Tomáš Preisler, Jan Stuchlý
</div>

!!! abstract "Draft, to be confirmed by instructors"

When an AI agent edits your code, you need to see *exactly* what it changed and be able to undo
it. Git gives you that. This session builds the **review loop** used for the rest of the week:

> **commit → let the agent work → read the diff → keep or revert**

!!! info "Before this session"
    [Git installed and configured](../prerequisites/git.md) in your
    [course account](../prerequisites/separate-account.md), and a GitHub account.
    No GitHub login in the terminal; we set that up together (see below).

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
    7. **Push to GitHub.** Create an Academy repository on github.com, connect to it with a
       [limited access token](#connecting-to-github-safely) and push your work.

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

## Connecting to GitHub safely

We do this together during the session, so don't worry if it looks long. The AI agent works in
your course account, so we never give that account full access to GitHub. Instead your project
gets a **token**: a password that only works for **one repository** and **expires after 7 days**.

### 1. Create the repository on GitHub

1. Go to [github.com](https://github.com) and sign in.
2. Click **+** (top right) → **New repository**.
3. Repository name: `miracle-academy`. Choose **Private**.
4. Do **not** tick *Add a README*, *.gitignore* or *license*. The repository must be empty.
5. Click **Create repository**.

### 2. Create the token

1. Click your **profile picture** (top right) → **Settings**.
2. At the very bottom of the left menu: **Developer settings** → **Personal access tokens** →
   **Fine-grained tokens** → **Generate new token**.
3. Fill in:
    - **Token name:** `miracle-academy`
    - **Expiration:** 7 days
    - **Repository access:** *Only select repositories* → choose `miracle-academy`
    - **Permissions** → *Repository permissions* → **Contents:** *Read and write*
      (*Metadata: Read-only* is added automatically). Leave everything else as it is.
4. Click **Generate token** and **copy** it (it starts with `github_pat_`). GitHub shows it only
   once; if you lose it, simply create a new one.

### 3. Connect your project

In the terminal, go to your project folder (replace the path with yours):

```bash
cd ~/miracle-academy
```

Tell Git to keep GitHub passwords **separate for each repository**, instead of one password for
all of GitHub:

```bash
git config --global credential.https://github.com.useHttpPath true
```

Add the GitHub address of the repository (use **HTTPS**, replace `<you>` with your GitHub
username) and upload your work:

```bash
git remote add origin https://github.com/<you>/miracle-academy.git
git push -u origin main
```

Git asks for your login. Use the **token instead of a password**:

```text
Username for 'https://github.com': <your GitHub username>
Password for 'https://<you>@github.com': <paste the token>
```

Nothing appears while you paste the token. That is on purpose; just press ++enter++.

=== "macOS"

    The Keychain remembers the token **for this repository only**, so the next `git push`
    won't ask again.

=== "Windows"

    Instead of the questions above, a **Git Credential Manager** window may open. Choose
    **Token** and paste it there. Do **not** choose *Sign in with your browser*: that would
    give access to all your repositories.

=== "Linux"

    Git asks for the token on every push. Keep the token at hand (for example in a password
    manager).

**After 7 days** the token expires and `git push` fails. Create a new token (step 2) and run
`git push` again; Git asks for the new one.

!!! danger "Never run `gh auth login` in the course account"
    It would give the account, and with it the agent, access to all your repositories.

## Further reading

- [Cheat sheet: Git commands](../cheatsheet.md#git)
- [Pro Git book](https://git-scm.com/book/en/v2), chapters 1–3
- [Happy Git and GitHub for the useR](https://happygitwithr.com/)
