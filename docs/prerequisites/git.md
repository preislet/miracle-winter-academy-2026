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

    Or, if you use [Homebrew](https://brew.sh): `brew install git`.

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

## 4. Connect your laptop to GitHub

The simplest way is the **GitHub CLI** (`gh`), which sets up authentication for you.

=== "macOS"

    ```bash
    brew install gh
    ```

    No Homebrew? Download the macOS installer from [cli.github.com](https://cli.github.com).

=== "Windows"

    Download and run the `.msi` installer from [cli.github.com](https://cli.github.com),
    or in PowerShell:

    ```powershell
    winget install --id GitHub.cli
    ```

    Then open a **new** Git Bash window.

=== "Linux"

    Follow [the official instructions](https://github.com/cli/cli/blob/trunk/docs/install_linux.md)
    for your distribution (Ubuntu/Debian: add the GitHub apt repository, then `sudo apt install gh`).

Then log in and follow the prompts. Choose **GitHub.com**, **HTTPS**, *Authenticate Git with your
GitHub credentials: Yes*, and *Login with a web browser*:

```bash
gh auth login
```

Check:

```bash
gh auth status
```
