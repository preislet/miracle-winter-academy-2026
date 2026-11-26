# Separate user account

**Do this first, before installing anything else.**

An AI coding agent runs commands **with the rights of the user who started it**. In your normal
account it could, in principle, read everything you can: your documents, e-mail attachments,
SSH keys, browser data and cloud logins.

So for the course you create a **separate user account** on your laptop, sign in to it, and
install and do everything for the course there. Your personal account, with your private files,
stays completely out of reach of the agent.

| Your normal account | Course account `miracle-course` |
|---|---|
| Your own files, e-mail, browser logins | Only course projects and data |
| Not used during the course | Everything for the course: R, RStudio, Positron, Git, Conda, Claude |
| Administrator | **Standard user** (not an administrator) |

!!! warning "You need an administrator password"
    Creating an account and installing programs needs your laptop's administrator password.
    On an institution-managed laptop, ask your IT department in advance.

## 1. Create the course account

Create a **standard** (non-administrator) account named `miracle-course`. Choose a password you will
remember.

=== "macOS"

    *System Settings* → *Users & Groups* → **Add User…** (enter your administrator password):

    - New user: **Standard**
    - Full name: `MIRACLE Course`
    - Account name: `miracle-course`
    - Password: choose one

=== "Windows"

    *Settings* → *Accounts* → *Other users* → **Add account** → *I don't have this person's
    sign-in information* → *Add a user without a Microsoft account*:

    - User name: `miracle-course`
    - Password: choose one (and answer the security questions)

    The new account is a standard user by default. Keep it that way.

=== "Linux"

    ```bash
    sudo adduser miracle-course
    ```

    (On Fedora: `sudo useradd -m miracle-course && sudo passwd miracle-course`.) Do **not** add it to the
    `sudo` or `wheel` group.

## 2. Sign in to the course account

1. **Disconnect any VPN connections and network drives.**
2. **Log out** of your regular account. Don't just use *Switch user*: logging out closes
   everything that runs in your normal account.
3. **Log in** as **`miracle-course`** and finish the first-start setup.
4. **Don't import existing credentials and don't sign in to cloud storage.** Skip the
   Apple ID / iCloud and Microsoft account / OneDrive prompts, don't connect Google Drive or
   Dropbox, and don't import browser profiles, saved passwords or keychains.

From now on, everything for the course happens in this account.

## 3. Install everything there

Work through the rest of the [prerequisites](index.md) **while signed in as `miracle-course`**: terminal,
R and RStudio, Positron, Git and GitHub, Python and Conda, and Claude.

!!! info "Installers will ask for an administrator"
    Because `miracle-course` is a standard user, installers ask for an administrator's name and
    password. Enter your **normal account's** name and password there. Do not turn
    `miracle-course` into an administrator.

!!! info "R asks about a personal library"
    When you run `install.packages()` in the course account, R may ask
    *"Would you like to use a personal library instead?"* Answer **yes** (twice). The packages
    then install into the course account only.

??? note "Already installed everything in your normal account?"
    Programs installed for all users (R, RStudio, Positron, Git) also work in the new account. Everything that belongs to a user has to be done again in `miracle-course`:

    - [Miniforge and the `miracle` environment](python-conda.md)
    - [R packages](r-rstudio.md#course-r-packages)
    - [Git name and e-mail](git.md#2-tell-git-who-you-are)
    - [Claude Code and the Claude desktop app](claude-tools.md), including logging in with your
      MIRACLE Academy team account

    Then you can uninstall the course tools from your normal account if you like.

## 4. Check the separation

In the course account, open a terminal and try to look into your normal account's files.
Replace `<your-username>` with your normal account's name:

=== "macOS"

    ```bash
    whoami                                   # miracle-course
    ls /Users/<your-username>/Documents      # should say: Permission denied
    ```

=== "Windows"

    In Git Bash:

    ```bash
    whoami                                   # ...\miracle-course
    ls /c/Users/<your-username>/Documents    # should say: Permission denied
    ```

=== "Linux"

    ```bash
    whoami                                   # miracle-course
    ls /home/<your-username>                 # should say: Permission denied
    ```

If you can see your files, tell us on Monday. On some Linux distributions home folders are
readable by other users by default; `sudo chmod 750 /home/<your-username>` fixes that.

## During the course

- Always **sign in as `miracle-course`** for the course.
- Keep course projects and data in the course account. Don't copy personal or real patient data
  into it.
- Log in only to Claude (your MIRACLE Academy team account). Don't store GitHub credentials in
  Git or the GitHub CLI: we set up a limited GitHub token together in the Git session.
- No VPN, network drives or cloud storage while you work in the course account.
