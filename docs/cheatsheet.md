---
description: Terminal, Git, GitHub, Conda, Python, R and Claude Code commands used during the MIRACLE Winter Academy 2026.
---

# Cheat sheet

The commands we use during the week, on one page. Words in `<angle brackets>` are placeholders:
replace them, including the brackets. Print the page with ++ctrl+p++ / ++cmd+p++.

!!! tip "The review loop: use it every time an AI agent touches your code"
    1. `git add . && git commit -m "Before agent"` saves a checkpoint.
    2. Let the agent work.
    3. `git diff` shows exactly what changed. Read it.
    4. Keep it with `git add . && git commit -m "<what changed>"`, or throw it away with `git restore .`

## Terminal

Use Terminal on macOS, your terminal app on Linux, and **Git Bash** on Windows.

| Command | What it does |
|---|---|
| `pwd` | Show the folder you are in |
| `ls` / `ls -la` | List files / including hidden files, with details |
| `cd <folder>` | Go into a folder |
| `cd ..` / `cd ~` / `cd -` | Go up one level / home / back to the previous folder |
| `mkdir -p <folder>` | Create a folder, including missing parent folders |
| `cp <file> <copy>` / `cp -r <dir> <copy>` | Copy a file / a folder |
| `mv <old> <new>` | Move or rename |
| `rm <file>` / `rm -r <folder>` | Delete. **There is no undo and no trash bin.** |
| `cat <file>` / `head -n 20 <file>` | Print a whole file / its first 20 lines |
| `less <file>` | Scroll through a file (++q++ quits) |
| `which <command>` | Where is this program? Useful for "command not found" |
| `history` | Commands you ran before |

| Key | What it does |
|---|---|
| ++tab++ | Complete a file or command name. Press twice to list the options |
| ++arrow-up++ / ++arrow-down++ | Previous / next command |
| ++ctrl+c++ | Stop the running command |
| ++ctrl+l++ | Clear the screen |
| ++ctrl+r++ | Search earlier commands |

## Git

| Command | What it does |
|---|---|
| `git init` | Turn the current folder into a repository |
| `git clone <url>` | Download a repository |
| `git status` | What changed, and what is staged? **Run it often.** |
| `git add <file>` / `git add .` | Stage one file / everything |
| `git commit -m "<message>"` | Save a checkpoint of the staged changes |
| `git diff` | Changes not yet staged |
| `git diff --staged` | Changes staged for the next commit |
| `git log --oneline --graph --all` | Compact history of all branches |
| `git show <commit>` | What one commit changed |
| `git restore <file>` | Discard uncommitted changes in a file. **Cannot be undone.** |
| `git restore --staged <file>` | Unstage a file but keep the changes |
| `git revert <commit>` | Undo a commit by adding a new, opposite commit |
| `git switch -c <branch>` | Create a branch and switch to it |
| `git switch <branch>` | Switch to an existing branch |
| `git branch` | List branches |
| `git merge <branch>` | Merge a branch into the current one |
| `git branch -d <branch>` | Delete a merged branch |
| `git push` / `git pull` | Send commits to / get commits from GitHub |
| `git push -u origin <branch>` | Push a new branch for the first time |
| `git stash` / `git stash pop` | Put uncommitted changes aside / bring them back |

**Worktrees** let you run several AI agents in parallel, each in its own folder and branch
(Advanced track):

| Command | What it does |
|---|---|
| `git worktree add ../<folder> -b <branch>` | New folder with a new branch from the same repository |
| `git worktree list` | Show all worktrees |
| `git worktree remove ../<folder>` | Remove a worktree when you are done |

## GitHub access (limited token)

Set up together in the [Git session](workshops/git.md#connecting-to-github-safely). The token
works for **one repository** and **expires after 7 days**.

| Step | What to do |
|---|---|
| 1 | On github.com, create a dedicated repository for the Academy |
| 2 | *Settings* → *Developer settings* → *Fine-grained tokens* → *Generate new token*: expiration **7 days**, *Only select repositories* → your Academy repository, **Contents: Read and write**, Pull requests only if needed, nothing else |
| 3 | `git config --global credential.https://github.com.useHttpPath true` |
| 4 | `git remote add origin https://github.com/<you>/<repo>.git` |
| 5 | `git push -u origin main`. When Git asks for a password, paste the token |

!!! danger "Never run `gh auth login` in the course account"

## Conda

On Windows, run these in **Miniforge Prompt** unless you set up Git Bash with `conda init bash`.

| Command | What it does |
|---|---|
| `conda env list` | List environments. `*` marks the active one |
| `conda activate miracle` / `conda deactivate` | Switch the course environment on / off |
| `conda env create -f environment.yml` | Create an environment from a file |
| `conda env update -n miracle -f environment.yml --prune` | Update it after the file changed |
| `conda create -n <name> python=3.12` | New empty environment |
| `conda install -c conda-forge <package>` | Install a package into the active environment |
| `conda list` | Packages in the active environment |
| `conda run -n miracle <command>` | Run one command inside an environment without activating it |
| `conda env export --from-history > environment.yml` | Save what you installed, for others to recreate |
| `conda env remove -n <name>` | Delete an environment |

## Python

| Command | What it does |
|---|---|
| `python <script>.py` | Run a script |
| `python -i <script>.py` | Run a script, then stay in Python to inspect variables |
| `which python` | Which Python runs? It should point into the `miracle` environment |
| `jupyter lab` | Start JupyterLab in your browser |
| `help(<object>)` / `type(<object>)` / `dir(<object>)` | Documentation / type / attributes of an object |

!!! tip "Reading a traceback"
    Read Python errors **from the bottom up**. The last line says *what* went wrong; the lines
    above say *where*. Look for the first line that points to your own file.

## R, RStudio and Positron

| Command | What it does |
|---|---|
| `install.packages("<pkg>")` / `library(<pkg>)` | Install / load a package |
| `?<function>` | Help for a function |
| `getwd()` | Current working directory |
| `here::here("data", "<file>.csv")` | Path relative to the project root, works on every computer |
| `source("R/<file>.R")` | Load functions from a file |
| `testthat::test_dir("tests/testthat")` | Run the tests |
| `renv::init()` / `renv::snapshot()` / `renv::restore()` | Start / record / recreate the project's package versions |
| `sessionInfo()` | R and package versions, for methods sections and bug reports |

| RStudio shortcut | Windows / Linux | macOS |
|---|---|---|
| Run current line or selection | ++ctrl+enter++ | ++cmd+enter++ |
| Run the whole file | ++ctrl+shift+enter++ | ++cmd+shift+enter++ |
| Insert `<-` | ++alt+minus++ | ++option+minus++ |
| Insert pipe `|>` | ++ctrl+shift+m++ | ++cmd+shift+m++ |
| Clear the console | ++ctrl+l++ | ++ctrl+l++ |

Most RStudio shortcuts also work in Positron.

## Claude Code

!!! danger "Before you start the agent"
    `cd` into your project folder first, and commit. Never start Claude Code in your home folder or
    in a folder with real patient data.

**In the terminal**

| Command | What it does |
|---|---|
| `claude` | Start a session in the current folder |
| `claude "<task>"` | Start a session with a first prompt |
| `claude -c` | Continue the most recent conversation in this folder |
| `claude -r` | Pick an earlier conversation to resume |
| `claude -p "<question>"` | Answer once and exit, without an interactive session |
| `claude --version` / `claude update` / `claude doctor` | Version / update / check the installation |

**Inside a session: type `/` to see all commands**

| Command | What it does |
|---|---|
| `/help` | Help and the list of commands |
| `/init` | Create a `CLAUDE.md` file describing your project for the agent |
| `/memory` | Edit `CLAUDE.md` instruction files |
| `/permissions` | Review and change what the agent may do without asking |
| `/sandbox` | Switch sandbox mode on or off (supported platforms only) |
| `/model` | Switch the model |
| `/context` | How full the conversation's context is |
| `/compact` | Summarise the conversation to free up context |
| `/clear` | Start a fresh conversation |
| `/rewind` | Go back to an earlier point, in the conversation and/or the code |
| `/resume` | Open an earlier conversation |
| `/mcp` | Manage MCP connections to external tools and data |
| `/plugin` | Install and manage plugins (e.g. Superpowers) |
| `/usage` | Plan usage and limits |
| `/status` | Version, model and account |
| `/login` / `/logout` | Sign in to / out of your account |
| `/exit` | Quit |

**Keys and prefixes**

| Key | What it does |
|---|---|
| ++esc++ | Stop Claude mid-answer so you can redirect it. The work so far is kept |
| ++esc++ ++esc++ | With an empty prompt: open the rewind menu |
| ++shift+tab++ | Cycle permission modes: *Manual* (asks before every edit) → *accept edits* → *plan* (only plans, changes nothing) |
| `@<file>` | Point Claude to a file (with autocomplete) |
| `!<command>` | Run a shell command yourself and show its output to Claude |
| ++ctrl+o++ | Show the detailed transcript: every tool call and command |
| ++ctrl+c++ | Interrupt; with an empty prompt, press twice to exit |
| ++shift+enter++ | New line in your prompt (works in most terminals) |

Full reference: [Claude Code commands](https://code.claude.com/docs/en/commands) ·
[keyboard shortcuts](https://code.claude.com/docs/en/interactive-mode).
