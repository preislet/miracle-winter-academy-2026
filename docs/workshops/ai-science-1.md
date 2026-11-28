# AI-assisted science I

<div class="session-meta" markdown>
:material-calendar: Wednesday 2 Dec, 09:00–10:30
:material-account-group: <span class="pill basic">Basic</span> <span class="pill advanced">Advanced</span> (parallel rooms)
:material-laptop: Practical

:material-human-male-board: <span class="pill basic">Basic</span> Sára Veselá, Luděk Svoboda &nbsp;&nbsp; <span class="pill advanced">Advanced</span> Tomáš Preisler, Jan Stuchlý
</div>

!!! abstract "Draft, to be confirmed by instructors"

AI agents in scientific research with **Claude Code**. The focus is on
using agents for real scientific tasks *and* on knowing when not to trust them: sandboxing,
permissions and critical evaluation of results run through the whole session.

!!! info "Before this session"
    [Claude Code](../prerequisites/claude-tools.md) installed, and
    logged in with your MIRACLE Academy team account.

=== "Basic"

    ### Using an agent for science, safely

    #### Learning goals

    - Know which layers protect you when an agent works on your computer, and what each of them
      does **not** protect
    - Set permission rules and switch on the Claude Code sandbox for a project
    - Know the stronger options (containers, virtual machines) and their trade-offs
    - Use an agent for literature search, and check every citation it gives you

    #### What we will do

    1. **Where the agent runs, and what stops it:** your user account, file permissions, Claude
       Code permission rules, the Claude Code sandbox; Docker and virtual machines.
    2. **Literature search with an agent:** find and summarise papers on one question, then
       verify that every citation exists and says what the agent claims. The findings are the
       starting point for [AI-assisted science II](ai-science-2.md).

    ??? info "Notes from the slides"

        **What the agent can reach.** Claude Code runs commands with **your** rights: every file
        your user can read or change, the network, and any login stored in your account.
        Everything it reads goes into the context and is sent to the model provider.

        **Layers of protection**, from weakest to strongest:

        | Layer | Enforced by | Stops | Does not stop |
        |---|---|---|---|
        | Permission prompts and rules | Claude Code | Claude's own tools and commands it recognises | other programs, e.g. a Python script that writes a file |
        | Claude Code sandbox | the operating system, started by Claude Code | shell commands writing outside the project, network access | writes inside the project; Claude's Read and Edit tools |
        | File permissions (`chmod`) | the operating system | accidental overwrites | the same user changing them back |
        | Separate user account | the operating system | access to your personal files | anything inside the course account; network |
        | Container (Docker) | the operating system | everything not mounted into the container; network if configured | what you mount; what is sent to the provider |
        | Virtual machine | a separate operating system | almost everything on the host | what you share with it; what is sent to the provider |

        **None of them stops data going to the model provider.** If the agent reads a file, its
        content leaves your computer. For sensitive data, the only safe option is not to give it
        to a cloud agent at all.

        **The Claude Code sandbox on different systems:**

        | System | Sandbox | What you need |
        |---|---|---|
        | macOS | built in (Seatbelt) | nothing |
        | Linux | bubblewrap | `bubblewrap` and `socat`, installed with `sudo` |
        | Windows | not supported natively | only inside WSL2 (a Linux virtual machine) |

        **Docker (containers).** *Pros:* the agent sees only the folders you mount; the network can
        be limited; the same image gives the same environment everywhere; easy to throw away and
        start again. Anthropic publishes a ready-made development container for Claude Code with a
        firewall. *Cons:* needs installation and administrator rights; something new to learn; the
        mounted project folder is still fully writable; on macOS and Windows it runs inside a
        hidden virtual machine; check the licence of Docker Desktop at your institution (Podman is
        a free alternative).

        **Virtual machines** (UTM, VirtualBox, Hyper-V, WSL2, a cloud VM). *Pros:* the strongest
        separation, a whole separate operating system; snapshots let you roll back everything.
        *Cons:* heavy on memory and disk; slow to set up; needs administrator rights; shared
        folders weaken the separation again.

        **In practice:** a separate user account plus permission rules is a sensible minimum, and
        it is what we use in this course. Add the sandbox where it is available. Use a container or
        a VM when the agent works unattended, runs code you don't trust, or works next to data
        that matters.

        **Literature search with an agent.** From memory, a model writes references that *look*
        right: real authors and journals, but wrong years or PMIDs, or papers that don't exist.
        With a search tool connected through **MCP**, it cites what it actually retrieved. That is
        much better, but it can still misread a paper or overstate what it shows. For every
        reference you use, check three things: **it exists, it says that, it is relevant.**
        PubMed indexes peer-reviewed biomedical literature; most preprints (bioRxiv, medRxiv) are
        not in it.

    ??? abstract "Part 1: Where the agent runs, and what stops it"

        You try four layers one after the other and see what each one blocks, and what it lets
        through. Work in **Manual mode** (the default): Claude asks before it edits files or runs
        commands. Read every request before you answer.

        ##### Get the practice folder

        Replace `<course-materials>` with the folder where you cloned the course repository:

        ```bash
        cp -r <course-materials>/Miracle-Winter-Academy/miracle-ai-assisted-science-basics/science-lab ~/miracle-academy/
        cd ~/miracle-academy/science-lab
        ls data
        ```

        Start `claude` in this folder.

        ##### Layer 1: your user account

        You are signed in as `miracle-course`. Ask the agent to look into your **normal** account
        (replace `<your-username>` with its name):

        === "macOS"

            > List the files in /Users/&lt;your-username&gt;/Documents

        === "Windows"

            > List the files in /c/Users/&lt;your-username&gt;/Documents

        === "Linux"

            > List the files in /home/&lt;your-username&gt;

        Allow the command when Claude asks. The answer is **Permission denied**. That comes from the
        operating system, not from Claude: whatever you allow in Claude, the agent cannot get
        further than your user can.

        ##### Layer 2: file permissions

        Make the data file read-only and check it:

        ```bash
        chmod a-w data/cbc_samples.csv
        ls -l data
        ```

        The line now starts with `-r--r--r--`: nobody may write. Ask:

        > Remove the age column from data/cbc_samples.csv.

        Allow the edit. It fails, because the operating system refuses. Watch what the agent does
        next: it will usually suggest running `chmod` to make the file writable again. **Say no.**

        The agent runs as you, so it *could* change the permissions back. File permissions protect
        against accidents, not against the agent. The permission prompt you just answered was the
        real protection.

        Make the file writable again for the next step:

        ```bash
        chmod u+w data/cbc_samples.csv
        ```

        ##### Layer 3: Claude Code permission rules

        Rules in `.claude/settings.json` decide what Claude may do without asking you. Create the
        file with a rule that forbids editing anything in `data/` and running `chmod`:

        ```bash
        mkdir -p .claude
        cat > .claude/settings.json <<'EOF'
        {
          "permissions": {
            "deny": [
              "Edit(./data/**)",
              "Bash(chmod *)"
            ]
          }
        }
        EOF
        ```

        Leave Claude with `/exit`, start `claude` again, and type `/permissions` to see the rules.
        Then ask the same thing:

        > Remove the age column from data/cbc_samples.csv.

        This time Claude does not even ask: the rule blocks it. Now ask:

        > Is there another way to change this file despite the rules? Explain, don't do it.

        The rules cover Claude's own tools and the commands it recognises (`sed`, `cat`, `tee` …),
        but not what another program does. A Python script that writes the file is not covered.

        Rules live in the project and can be committed to git, so everyone working on the project
        gets the same ones. `deny` always wins over `allow`.

        ##### Layer 4: the Claude Code sandbox

        The sandbox lets the operating system enforce limits on **every command** the agent runs,
        including Python scripts: writes only inside the project folder, no network unless you allow
        a domain.

        === "macOS"

            Built in, nothing to install. Type `/sandbox` and switch it on (auto-allow mode).

        === "Linux"

            The sandbox needs two packages. Install them from your normal account, as on the
            [separate account](../prerequisites/separate-account.md) page:

            ```bash
            su - <your-username>
            sudo apt-get install bubblewrap socat     # Fedora: sudo dnf install bubblewrap socat
            exit
            ```

            Start `claude` again, type `/sandbox` and switch it on (auto-allow mode).

        === "Windows"

            Not available: on Windows, Claude Code runs commands without a sandbox. It works only
            inside WSL2, a Linux virtual machine, which is not part of this course. Follow on the
            projector or with your neighbour.

        Ask the agent to run these three commands, one at a time:

        > Run: touch inside.txt

        > Run: touch ~/outside.txt

        > Run: curl -sI https://example.com

        - `inside.txt` is created **without a question**: the project folder is allowed.
        - `~/outside.txt` is **blocked** by the operating system. Claude may offer to retry the
          command *outside the sandbox*. Read that prompt carefully and **say no**.
        - `curl` is **blocked** or Claude asks whether to allow `example.com`: no network by
          default. Say no.

        Note what the sandbox does **not** do: writing inside the project is allowed, so it does not
        protect `data/`. That is still the job of the rule from Layer 3. And Claude's own Read and
        Edit tools are governed by the permission rules, not by the sandbox.

        ##### What you have now

        - [ ] Course account: personal files out of reach
        - [ ] Permission rules: `data/` protected from Claude's tools
        - [ ] Sandbox (macOS, Linux): commands can't write outside the project or reach the network

        Keep this folder and these settings: the literature search in Part 2 runs here.

        ??? question "I changed the data file by accident"
            Copy it again from the course materials:
            `cp <course-materials>/Miracle-Winter-Academy/miracle-ai-assisted-science-basics/science-lab/data/cbc_samples.csv data/`

    ??? abstract "Part 2: Literature search with an agent"

        One question for the whole Wednesday:

        > **Which genes cause inherited haemolytic anaemia, and what is the evidence for each?**

        ##### Step 1: ask from memory

        Start `claude` in `science-lab` and ask:

        > Without using any tools, list 5 genes that cause inherited haemolytic anaemia. For each,
        > give one reference with first author, year, journal and PMID.

        Keep the answer in the conversation, you will come back to it.

        ##### Step 2: connect PubMed

        **MCP** (Model Context Protocol) connects the agent to outside tools and data. Here it gives
        Claude a PubMed search. We look at MCP properly in
        [AI-assisted science II](ai-science-2.md).

        Leave Claude with `/exit` and add the PubMed server for this folder:

        ```bash
        claude mcp add --transport http pubmed https://pubmed.mcp.claude.com/mcp
        claude mcp list
        ```

        `claude mcp list` shows `pubmed` as connected. Continue the same conversation and check
        the tools:

        ```bash
        claude --continue
        ```

        Type `/mcp`, select `pubmed` and look at its tools: search articles, get article
        metadata, get full text, …

        Note that PubMed works although the sandbox blocked `curl` in Part 1: the sandbox limits
        shell commands, while MCP tools are called by Claude Code itself. They go through
        permission prompts instead, so Claude asks before each new tool.

        ##### Step 3: search with PubMed

        > Using the PubMed tools, find which genes cause inherited haemolytic anaemia. Write
        > literature.md with a table: gene, group (red cell membrane, enzyme, haemoglobin, other),
        > what goes wrong in one sentence, and 1–2 references with first author, year, journal and
        > PMID. Use only articles you retrieved from PubMed in this session. Prefer reviews.

        Allow the PubMed tools when Claude asks. Then:

        > Check the references from your first answer, the one from memory, against PubMed.
        > Which of them are correct?

        ##### Step 4: check it yourself

        The agent checking itself is not enough. Pick **3 rows** of `literature.md` and open each
        PMID in your browser at `https://pubmed.ncbi.nlm.nih.gov/<PMID>/`:

        - [ ] The paper exists, and title, authors and year match the table
        - [ ] The abstract supports what the table says about the gene
        - [ ] The paper is about inherited haemolytic anaemia, not just a passing mention

        ##### What you have now

        - [ ] PubMed connected to Claude Code in this folder
        - [ ] `literature.md`, with references you checked yourself

        Keep both: AI-assisted science II continues from here.

        ??? question "The answer from memory looked fine"
            It often does. The genes are usually right; the errors hide in the references: a real
            author with the wrong year, a real title with someone else's PMID, or a paper that
            does not exist. One wrong PMID is enough to make every unchecked reference suspect.

=== "Advanced"

    ### Learning goals

    - Build multi-step scientific workflows with an agent
    - Integrate the agent with your existing tools and scripts
    - Configure sandboxing and permissions deliberately for sensitive data

    ### What we will do

    1. **Scientific workflow end to end:** from a question to analysis, figures and a methods
       paragraph, with the agent documenting software versions and parameters.
    2. **Tool integration:** let the agent use your own R/Python scripts and command-line tools.
    3. **Sandboxing and permissions:** configure allowed and denied actions, file system and network
       limits; discuss what is acceptable for sensitive data.
    4. **Critical evaluation:** reproduce the agent's result independently and compare.

## Materials

- <span class="pill basic">Basic</span> Practice folder: `Miracle-Winter-Academy/miracle-ai-assisted-science-basics/science-lab`
- <span class="pill basic">Basic</span> Slides (AI-assisted science I and II): `Miracle-Winter-Academy/miracle-ai-assisted-science-basics/ai_assisted_science_basic.pdf`
