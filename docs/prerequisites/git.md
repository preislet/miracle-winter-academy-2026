# Git and GitHub

**Git** keeps a history of every change in your project. During the course it is the safety net
for AI-assisted work: you commit, let the agent make changes, read the diff, then keep or revert.
**GitHub** hosts Git repositories online so you can share and collaborate.

## 1. Install Git

=== "macOS"

    Git comes with Apple's command line tools:

    ```bash
    xcode-select --install
    ```

=== "Windows"

    Download **Git for Windows** from [git-scm.com/downloads/win](https://git-scm.com/downloads/win)
    and run the installer. The defaults are fine, with one recommendation:

    - *Choosing the default editor*: pick **Nano** or **Visual Studio Code** rather than Vim.

    This also installs **Git Bash**, which you will use as your terminal.

=== "Linux"

    ```bash
    sudo apt install git        # Ubuntu / Debian
    sudo dnf install git        # Fedora
    ```

Check it works (in a new terminal window):

```bash
git --version
```

## 2. Tell Git who you are

Use the **same email address** as your GitHub account:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.org"
git config --global init.defaultBranch main
```

## 3. Create a GitHub account

Sign up for free at [github.com/signup](https://github.com/signup). Remember your username, as you
will need it on Monday.

!!! danger "Do not log in to GitHub from the terminal"
    In the course account, **never run `gh auth login`** and don't connect Git to GitHub with
    your password or a browser login. The AI agent works in this account and could use those
    credentials on all of your repositories.

    During the [Git session](../workshops/git.md#connecting-to-github-safely) we connect to
    GitHub together, with a short-lived access token limited to one Academy repository.
