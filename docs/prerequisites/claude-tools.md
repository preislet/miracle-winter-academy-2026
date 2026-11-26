# Claude

Two Claude tools are used during the course:

- **Claude Code**: an AI coding agent that runs in your terminal, reads and edits files in your
  project and runs commands. It asks for your permission before editing files or running
  commands. Used in the *AI-assisted
  coding* and *single-cell* practicals.
- **Claude desktop app / Claude Science**: used in the *AI-assisted science* sessions for
  literature search and scientific workflows.

!!! info "Your course account: the MIRACLE Academy team"
    You don't need your own Claude subscription. You will receive an **email with an invitation
    link to join the *MIRACLE Academy* team** on Claude.

    1. Open the link from the email and sign in or create a Claude account, ideally with the same
       email address the invitation was sent to.
    2. Accept the invitation to the **MIRACLE Academy** team.
    3. Log in to Claude Code and the Claude desktop app with this account, and choose the
       **MIRACLE Academy** organisation if you are asked.

    No email yet? Check your spam folder, then contact
    [Jan Stuchlý](mailto:jan.stuchly@lfmotol.cuni.cz). You can install the software now and
    log in later.

## Install Claude Code

=== "macOS"

    ```bash
    curl -fsSL https://claude.ai/install.sh | bash
    ```

=== "Windows"

    Make sure [Git for Windows](git.md) is installed first, because Claude Code uses Git Bash
    internally. Then, in **PowerShell**:

    ```powershell
    irm https://claude.ai/install.ps1 | iex
    ```

    Close and reopen your terminal afterwards.

=== "Linux"

    ```bash
    curl -fsSL https://claude.ai/install.sh | bash
    ```

If the installer ends with a note that **`~/.local/bin` is not in your PATH**, run:

=== "macOS"

    ```bash
    echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc && source ~/.zshrc
    ```

=== "Windows"

    In **PowerShell**:

    ```powershell
    [Environment]::SetEnvironmentVariable('Path', [Environment]::GetEnvironmentVariable('Path', 'User') + ";$env:USERPROFILE\.local\bin", 'User')
    ```

    Then close all terminals and open a new one.

=== "Linux"

    ```bash
    echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc && source ~/.bashrc
    ```

Check (in a **new** terminal window):

```bash
claude --version
```

If it says `command not found`, the PATH step above is missing.

### First start (once you have access)

```bash
mkdir -p ~/miracle-academy && cd ~/miracle-academy
claude
```

Follow the login prompt in your browser. Type `/exit` to quit.

!!! danger "Only in the course account, never on sensitive data"
    Use Claude Code only while signed in to your [separate course account](separate-account.md),
    and always `cd` into a dedicated project folder first. The agent can read files in the folder
    where it is started. Sandboxing and permissions are covered on Monday and Wednesday.

## Install the Claude desktop app

=== "macOS"

    Download from [claude.ai/download](https://claude.ai/download), open the `.dmg`, and drag
    Claude into *Applications*.

=== "Windows"

    Download and run the installer from [claude.ai/download](https://claude.ai/download).

=== "Linux"

    There is no official desktop app for Linux. Use [claude.ai](https://claude.ai) in your browser.

## Claude Science

Access to **Claude Science** comes with your MIRACLE Academy team account. Further instructions
will follow in the invitation email or during the course.
