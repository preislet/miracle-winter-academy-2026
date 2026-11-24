# Terminal basics

A **terminal** (also called a shell or command line) is a text window where you type commands.
The AI coding agent, Git and Conda all run there. You only need to be able to open one and
paste a command before the course. Everything else is covered on Monday.

=== "macOS"

    Open **Terminal**: press ++cmd+space++, type `Terminal`, press ++enter++.

    The default shell is `zsh`. Try:

    ```bash
    pwd      # where am I?
    ls       # what is in this folder?
    ```

    !!! tip "Command line developer tools"
        Several tools below need Apple's command line tools. Install them once:

        ```bash
        xcode-select --install
        ```

        If it says they are already installed, you are done.

=== "Windows"

    You will use two terminals on Windows:

    - **PowerShell** (built in): press ++win++, type `PowerShell`, press ++enter++.
      Used to install Claude Code.
    - **Git Bash** (installed together with [Git](git.md)): a Linux-style terminal. Use it for
      Git and Claude Code during the course, so that the commands match those of macOS and Linux users.

    Conda has its own **Miniforge Prompt**, which you will get when you install
    [Python and Conda](python-conda.md).

    Try in Git Bash:

    ```bash
    pwd
    ls
    ```

    ??? info "Optional: WSL2 (Linux on Windows)"
        If you are already comfortable with Linux, you can instead work inside
        **WSL2** (Windows Subsystem for Linux) and follow the *Linux* instructions everywhere.
        Install it from an **administrator** PowerShell, then restart:

        ```powershell
        wsl --install
        ```

        Keep in mind that RStudio then runs on Windows while your other tools run in Linux. This
        is fine, but it adds one more thing to keep track of. If unsure, skip WSL2.

=== "Linux"

    Open your terminal application (e.g. ++ctrl+alt+t++ on Ubuntu). Try:

    ```bash
    pwd
    ls
    ```

## Copying commands from this site

Every code block has a :material-content-copy: copy button in its top-right corner. Click it,
paste into the terminal (++cmd+v++ on macOS; right-click or ++shift+insert++ in Git Bash;
++ctrl+shift+v++ on Linux) and press ++enter++.

Lines starting with `#` are comments and are ignored by the shell.
