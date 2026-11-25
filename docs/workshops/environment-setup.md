# Environment setup and terminal essentials

<div class="session-meta" markdown>
:material-calendar: Monday 30 Nov, 11:30–12:45
:material-account-group: <span class="pill all">All participants</span>
:material-human-male-board: MIRACLE Research Software Engineering team
:material-laptop: Practical
</div>

!!! abstract "Draft, to be confirmed by instructors"

Everything else in the week depends on a working laptop setup. In this session we fix whatever
did not install cleanly, learn just enough terminal to feel at home, and set up the AI coding
agent so that it is **safe by default**.

!!! info "Before this session"
    Work through all [prerequisites](../prerequisites/index.md) and run the
    [setup check](../prerequisites/check.md). Bring the error messages of anything that failed.

## Learning goals

- Have R/RStudio, Git, Conda and Claude Code working on your own laptop
- Navigate the file system from a terminal and run commands with confidence
- Understand what an AI agent is allowed to do on your machine: permissions, built-in and
  runtime sandboxing
- Set up a dedicated, safe working folder for the course

## What we will do

1. **Setup clinic (≈20 min).** Run the setup check together; instructors and helpers fix
   remaining installation problems one-on-one.
2. **Terminal essentials (≈20 min).**
    - Where am I and what is here: `pwd`, `ls`, `cd`, paths, `~`, `..`
    - Making and moving things: `mkdir`, `cp`, `mv`, and why `rm` has no undo
    - Reading files: `cat`, `head`, `less`; tab completion and command history
    - What an environment variable and `PATH` are, and why "command not found" happens
3. **First contact with the AI agent (≈20 min).**
    - Create `~/miracle-academy` and start Claude Code *inside it*
    - Watch the agent ask for permission before reading, editing or running anything
    - Permission modes: what "allow once", "allow always" and "deny" mean
    - Sandboxing: limiting the agent to a folder and network access, and why it matters for
      medical data
4. **Wrap-up (≈10 min).** Checklist: every participant leaves with a green setup check.

## Materials

- *Slides: to be added*
- Cheat sheet: terminal commands. *To be added*
