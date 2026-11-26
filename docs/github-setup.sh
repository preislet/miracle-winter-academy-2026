#!/usr/bin/env bash
# MIRACLE Winter Academy 2026: connect ONE project to GitHub with a limited token.
#
# Run it inside your project folder:
#   curl -fsSL https://preislet.github.io/miracle-winter-academy-2026/github-setup.sh -o ~/github-setup.sh
#   bash ~/github-setup.sh
#
# What it does, only for this project (nothing global):
#   - saves your GitHub username and token in .env (readable only by you)
#   - adds .env to .gitignore, so the token is never committed
#   - tells Git to take the password from .env, and switches off the system password stores
#     (macOS Keychain / Windows Credential Manager) for this project
#   - sets the GitHub address of the project (remote "origin")
#   - adds a Claude Code rule that forbids the agent to read .env
# Run it again whenever you get a new token.
set -euo pipefail

if ! top=$(git rev-parse --show-toplevel 2>/dev/null); then
  echo "This folder is not a Git project. Open the terminal inside your project folder and try again."
  exit 1
fi
cd "$top"
echo "Project folder: $top"
echo

read -r -p "1/3  Your GitHub username: " gh_user
read -r -p "2/3  Name of the repository on GitHub (for example miracle-academy): " gh_repo
read -r -s -p "3/3  Paste your token (it stays hidden) and press Enter: " gh_token
echo
echo

gh_user=${gh_user//[[:space:]]/}
gh_repo=${gh_repo//[[:space:]]/}
gh_repo=${gh_repo%.git}
gh_token=${gh_token//[[:space:]]/}
if [ -z "$gh_user" ] || [ -z "$gh_repo" ]; then
  echo "Username and repository name must not be empty. Nothing was changed."
  exit 1
fi
case "$gh_token" in
  github_pat_*) ;;
  *) echo "That does not look like a fine-grained token (it should start with github_pat_). Nothing was changed."
     exit 1 ;;
esac

# 1. Token in .env, readable only by you
umask 077
printf 'GITHUB_USER=%s\nGITHUB_TOKEN=%s\n' "$gh_user" "$gh_token" > .env
chmod 600 .env 2>/dev/null || true
echo "Saved the token in .env"

# 2. Never commit .env
touch .gitignore
if ! grep -qxF ".env" .gitignore; then
  echo ".env" >> .gitignore
  echo "Added .env to .gitignore"
fi

# 3. Git reads the password from .env, only in this project
git config --local --unset-all credential.helper 2>/dev/null || true
git config --local --add credential.helper ""
git config --local --add credential.helper '!f() { test "$1" = get || exit 0; . "$(git rev-parse --show-toplevel)/.env"; echo "username=$GITHUB_USER"; echo "password=$GITHUB_TOKEN"; }; f'
echo "Git will take the token from .env (this project only)"

# 4. GitHub address of the project
url="https://github.com/$gh_user/$gh_repo.git"
if git remote get-url origin >/dev/null 2>&1; then
  git remote set-url origin "$url"
else
  git remote add origin "$url"
fi
echo "GitHub address: $url"

# 5. Claude Code must not read .env
mkdir -p .claude
if [ ! -f .claude/settings.json ]; then
  printf '{\n  "permissions": {\n    "deny": ["Read(./.env)"]\n  }\n}\n' > .claude/settings.json
  echo "Added a Claude Code rule that blocks reading .env"
elif ! grep -qF 'Read(./.env)' .claude/settings.json; then
  echo "Note: .claude/settings.json already exists. Add \"Read(./.env)\" to permissions.deny in it."
fi

# 6. Test the connection
echo
echo "Checking the connection to GitHub..."
if GIT_TERMINAL_PROMPT=0 git ls-remote origin >/dev/null 2>&1; then
  echo "OK: connected. To upload your work, run:  git push -u origin main"
else
  echo "Could not connect. Check that:"
  echo "  - the repository $gh_user/$gh_repo exists on GitHub"
  echo "  - the token was created for this repository, with Contents: Read and write"
  echo "  - the token has not expired"
  echo "Then run this script again."
  exit 1
fi
