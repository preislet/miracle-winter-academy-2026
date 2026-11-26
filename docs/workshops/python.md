# Python

<div class="session-meta" markdown>
:material-calendar: Tuesday 1 Dec, 10:35–12:15
:material-account-group: <span class="pill basic">Basic</span> <span class="pill advanced">Advanced</span> (parallel rooms, different topics)
:material-laptop: Practical

:material-human-male-board: <span class="pill basic">Basic</span> Sára Veselá, Luděk Svoboda &nbsp;&nbsp; <span class="pill advanced">Advanced</span> Jan Stuchlý, Tomáš Preisler
</div>

!!! abstract "Draft, to be confirmed by instructors"

AI agents write a lot of Python, especially for single-cell analysis, whether or not you know the
language. This session is about **reading and supervising** Python code, not becoming a Python
programmer. The two tracks cover different topics:

- <span class="pill basic">Basic</span> **Python essentials for reading and reviewing code**
- <span class="pill advanced">Advanced</span> **Python tools for single-cell analysis**

!!! info "Before this session"
    [Miniforge and the `miracle` environment](../prerequisites/python-conda.md) and
    [Positron](../prerequisites/positron.md) installed.
    Advanced track: also the extra packages (scvi-tools, muon).

=== "Basic"

    ### Python essentials for reading and reviewing code

    #### Learning goals

    - Read a Python script and explain what it does, mapping it to R concepts you know
    - Create, activate and use a Conda environment
    - Run a Python script from the terminal and understand modules and `import`
    - Spot common errors in AI-generated Python code and read a traceback

    #### What we will do

    1. **Python and its environment.** What the interpreter is, where packages come from, why
       environments exist: `conda activate miracle`, `which python`, `conda list`.
    2. **Run a script.** `python summary.py` from the terminal: where you run it from, and what it
       produces.
    3. **Read a script.** Where to start, the parts of a script, and each line next to its R
       equivalent.
    4. **Find the bug.** Three versions of the script changed for a task: one crashes, one gives a
       plausible but wrong answer, one does something you didn't ask for.

    ??? abstract "Part 1: Python and its environment"

        You won't write much Python this week. You will **supervise an AI agent that writes and runs
        Python for you**. For that you need to know *which* Python runs, *where* its packages come
        from, and what an *environment* is. Most "it worked yesterday" problems, for you and for the
        agent, come from exactly these three things. Nothing gets installed in this part: we look at
        what you already have.

        !!! tip "Windows"
            Use **Git Bash** for everything below, as set up on the
            [Python and Conda](../prerequisites/python-conda.md) page. The commands are then the same
            as on macOS and Linux.

        ##### What "Python" actually is

        The word *Python* means two things:

        - the **language**: the text in a `.py` file
        - the **interpreter**: the program called `python` that reads that text and runs it

        "Run it in Python" means: give the file to an interpreter.

        **There is more than one Python on your laptop**, even in the fresh `miracle-course` account.
        Miniforge gave you two: one in the `base` environment and one in `miracle`. On top of that,
        macOS and Linux come with a system `python3`, and Windows has a `python` shortcut that only
        opens the Microsoft Store. They have different versions and different packages. **Which one
        runs depends on your `PATH`**, the list of folders the terminal searches for commands (see
        Monday).

        !!! example "Try it: which Pythons can your terminal see?"

            ```bash
            python --version
            which -a python python3    # every match on your PATH; the first one wins
            ```

            Run it now, and again after `conda activate miracle` below. The first line changes.

        **Interactive Python vs a script.** Type `python` alone and you get the prompt `>>>`, the
        equivalent of the R console:

        ```pycon
        >>> 1 + 1
        2
        >>> exit()
        ```

        A **script** is a text file ending in `.py` that the interpreter runs from top to bottom, like
        an R script you `source()`. Agents almost always work with scripts.

        ##### Packages: where the functionality comes from

        Plain Python does little science on its own. Reading tables, plotting and single-cell
        analysis all come from **packages** written by other people.

        | Term | Meaning | In R |
        |---|---|---|
        | **module** | one `.py` file with code you can `import` | one script you `source()` |
        | **package** | a folder of modules, installed as one unit | a package |
        | **library** | used loosely for either of the above | the folder where packages live |
        | `import pandas as pd` | load the package in this script, under the short name `pd` | `library(dplyr)` |

        People mix up *module*, *package* and *library* all the time. What matters: **you can only
        `import` what is installed in the environment that is running.**

        !!! warning "The install name is not always the import name"
            The course [`environment.yml`](../prerequisites/environment.yml) installs `scikit-learn`
            and `python-igraph`, but in code you write `import sklearn` and `import igraph`. When an
            error says a module is missing, the package to install may have a different name.

        **Where packages come from.** Conda downloads them from **conda-forge**, a free collection
        of scientific packages. Everything you need this week is already installed in the `miracle`
        environment, so you won't install anything yourself.

        **conda, mamba, micromamba.** Three commands, one job:

        - **`conda`**: what we use in this course (installed with Miniforge)
        - **`mamba`**: the same commands, historically faster; also included in Miniforge
        - **`micromamba`**: a small stand-alone version that AI agents often install themselves

        If an agent types `mamba install …` or `micromamba create …`, read it as `conda`.

        **Versions matter.** The same code can give different results, or fail, with another package
        version. That's why a methods section lists software versions:

        ```bash
        python -c "import pandas; print(pandas.__version__)"
        ```

        ##### Environments

        An **environment** is a separate folder with **its own interpreter and its own packages**.
        Each project can have its own, so updating a package for project A cannot break project B.
        Compared with R's `renv`, a conda environment also contains the interpreter itself.

        ```mermaid
        flowchart LR
            T["Terminal (PATH)"] -->|"conda activate miracle"| M
            subgraph M["environment: miracle"]
                PY["python 3.12"] --> PK["pandas, matplotlib, scanpy, …"]
            end
            subgraph B["environment: base"]
                PY2["python"] --> PK2["almost no packages"]
            end
        ```

        Activating an environment puts *its* `python` first on your `PATH`.

        **Hands-on: explore the `miracle` environment.** Tick off each step.

        - [ ] **List the environments.** The `*` marks the active one.

            ```bash
            conda env list
            ```

        - [ ] **Activate the course environment.** Your prompt now shows `(miracle)`.

            ```bash
            conda activate miracle
            ```

        - [ ] **Check which Python runs now.** The path should point *into* the `miracle` folder.

            ```bash
            which python
            ```

        - [ ] **See what is installed** and in which version.

            ```bash
            conda list pandas
            ```

        - [ ] **Read the recipe.** It's the `environment.yml` you downloaded before the course to
            create the environment, probably still in your Downloads folder
            ([download it again](../prerequisites/environment.yml) if not):

            ```bash
            cat ~/Downloads/environment.yml
            ```

            It has a name, a channel (where packages come from) and a list of dependencies. Anyone
            with this file can recreate the same environment. This is your first piece of code
            reading today.

        - [ ] **Break it on purpose.** Leave the environment and try to use pandas:

            ```bash
            conda deactivate
            python -c "import pandas"
            ```

            Your prompt is back to `(base)`, and you get
            `ModuleNotFoundError: No module named 'pandas'`. Pandas *is* installed, just not in
            `base`, whose interpreter is the one running now.

        - [ ] **Go back in.**

            ```bash
            conda activate miracle
            python -c "import pandas; print('pandas', pandas.__version__)"
            ```

        !!! success "Checkpoint"
            Your prompt shows `(miracle)`, `which python` points into the `miracle` environment, and
            the last command prints a pandas version.

        **The same environment in Positron.** Positron doesn't use your terminal's activation; you
        pick the interpreter yourself, as in the [setup check](../prerequisites/positron.md#check-that-it-finds-r-and-python):
        click the **interpreter picker** in the top-right corner, choose the Python entry for
        `miracle`, and run `import pandas` in the console. No error means you have the right one.

        ##### Environments and AI agents

        An agent runs commands in a terminal just like you, so it hits the same problems, and it can
        also *change* your environment. When you approve its commands, watch for:

        | The agent wants to run… | Ask yourself |
        |---|---|
        | `conda install …` or `pip install …` (`pip` is Python's other install tool) | Into **which** environment? It should be `miracle`, never `base`. |
        | `conda create …`, `micromamba create …` | Does the project really need a new environment? |
        | a package name you have never heard of | Ask the agent what it is and why it's needed. Agents sometimes invent package names, and attackers register such names. |

        ##### Common problems

        ??? question "`conda: command not found`"
            The terminal doesn't know about Miniforge. Close and reopen the terminal first. If that
            doesn't help:

            === "macOS / Linux"

                ```bash
                ~/miniforge3/bin/conda init "$(basename "$SHELL")"
                ```

                Then close and reopen the terminal.

            === "Windows"

                Check that you ran `conda init bash` in Miniforge Prompt and then opened a *new*
                Git Bash window ([Python and Conda](../prerequisites/python-conda.md)).

        ??? question "`ModuleNotFoundError: No module named '…'`"
            In order of likelihood: (1) the environment is not active, so check the prompt and
            `which python`; (2) the package has a different install name; (3) it really isn't
            installed in this environment; (4) it doesn't exist and the agent made the name up.

        ??? question "Windows: `python` shows no `>>>` prompt in Git Bash"
            Interactive Python sometimes hangs in Git Bash. Press ++ctrl+c++, then start it with
            `winpty python` instead. Running scripts (`python script.py`) is not affected.

        ??? question "Positron finds no `miracle` interpreter"
            Check that the environment exists with `conda env list`, then restart Positron. It looks
            for conda environments when it starts.

        ??? question "My prompt always starts with `(base)`"
            Normal: Miniforge activates `base` in every new terminal. Run `conda activate miracle`
            before working on the course.

        ##### Key terms

        interpreter
        : The program (`python`) that runs Python code.

        package
        : An installable unit of reusable code (`pandas`, `scanpy`), loaded with `import`.

        module
        : A single file of Python code; packages are made of modules.

        environment
        : A folder with its own interpreter and packages, switched on with `conda activate`.

        channel
        : Where conda downloads packages from; we use `conda-forge`.

        `environment.yml`
        : The recipe from which an environment can be recreated.

    ??? abstract "Part 2: Running your first scripts"

        ##### Get the files

        The scripts are in the course materials repository, in the folder
        `Miracle-Winter-Academy/miracle-python-essentials`. **Copy** that folder into your
        `~/miracle-academy` folder, so that the files the scripts create don't end up in the course
        repository, then go into it. Replace `<course-materials>` with the folder where you cloned
        the repository:

        ```bash
        cp -r <course-materials>/Miracle-Winter-Academy/miracle-python-essentials ~/miracle-academy/
        cd ~/miracle-academy/miracle-python-essentials
        ls
        ```

        You should see `hello.py`, `summary.py`, `README.md` and a `data` folder with
        `cbc_samples.csv`: synthetic blood counts of 18 patients at 4 visits, the same data you
        will use in the afternoon.

        ##### A script is just a text file

        Open the folder in Positron: **File → Open Folder…** and choose
        `miracle-academy/miracle-python-essentials` in your home folder. If Positron asks whether
        you trust the authors of the files, answer yes. Then click `hello.py` in the file list on
        the left.

        Three lines of text, nothing more. `import sys` loads a module that knows about the running
        interpreter; the two `print` lines write text to the terminal. Now hand the file to Python:

        ```bash
        conda activate miracle
        python hello.py
        ```

        ```text
        Hello from Python!
        This Python is running from: …/miniforge3/envs/miracle/bin/python
        ```

        The second line shows **which interpreter ran the script**. It should point into the
        `miracle` environment, just like `which python` in Part 1. (On Windows the path looks like
        `C:\Users\…\miniforge3\envs\miracle\python.exe`.)

        ##### The folder you're in matters

        Go to your home folder and try the same command:

        ```bash
        cd ~
        python hello.py
        ```

        ```text
        …python: can't open file '…hello.py': [Errno 2] No such file or directory
        ```

        Python looks for `hello.py` in the folder you are **in**, not where the file lives. Go back
        and it works again:

        ```bash
        cd ~/miracle-academy/miracle-python-essentials
        python hello.py
        ```

        Agents make this mistake too. When an agent's command fails with `can't open file`, check
        which folder it ran in.

        ##### Run a real script

        `summary.py` reads the blood counts and calculates, for each patient, the number of visits
        and the average white blood cells, haemoglobin and platelets. It uses pandas, so it only works
        in the `miracle` environment:

        ```bash
        python summary.py
        ```

        ```text
        Read 72 samples from 18 patients.
        Wrote 18 rows to results/summary.csv
        ```

        ##### What did it produce?

        The script created a new folder `results` with a file in it. Look at it:

        ```bash
        ls results
        head results/summary.csv
        ```

        ```text
        patient_id,visits,mean_wbc,mean_hgb,mean_plt
        P001,4,6.4,147.0,243.8
        …
        ```

        Now run the script once more and list the folder with times:

        ```bash
        python summary.py
        ls -l results
        ```

        The time of `summary.csv` changed: the old file was **replaced without asking**. Scripts
        do this all the time, so before you let an agent run a script, find out what it writes.

        !!! success "Checkpoint"
            `python summary.py` prints *Read 72 samples from 18 patients*, and the first data line
            of `results/summary.csv` is `P001,4,6.4,147.0,243.8`.

        ##### Common problems

        ??? question "`SyntaxError: invalid syntax` when typing `python hello.py`"
            You are inside interactive Python (the prompt shows `>>>`). Type `exit()` first, then
            run the command in the normal terminal.

        ??? question "`can't open file '…': [Errno 2] No such file or directory`"
            You are in the wrong folder. Run `pwd` to see where you are, then
            `cd ~/miracle-academy/miracle-python-essentials`.

        ??? question "`ModuleNotFoundError: No module named 'pandas'`"
            The `miracle` environment is not active: your prompt shows `(base)` or nothing. Run
            `conda activate miracle`. (`hello.py` works anyway, because it needs no packages.)

        ??? question "`FileNotFoundError: … 'data/cbc_samples.csv'`"
            Python found the script but not its data: you started it from another folder, for
            example with `python miracle-python-essentials/summary.py`. Go into the folder first and
            run `python summary.py`.

    ??? abstract "Part 3: Reading a script"

        You ran `summary.py` and saw its result. Now find out **where that result comes from**.
        Open `summary.py` in Positron; the line numbers are on the left.

        ##### Where to start reading

        Python runs a script from top to bottom, but you don't have to read it that way:

        1. **The text between `"""` at the top** describes what the script does. Read it first.
        2. **Jump to the bottom.** `if __name__ == "__main__":` followed by `main()` means
           "start here". You don't need to understand this line, just recognise it.
        3. **Read `main()`.** It lists the steps in order: read the data, summarise, write the result.
        4. **Read a function only when `main()` uses it**, here `summarise_per_patient`.

        ##### The parts of a script

        | You see | It means |
        |---|---|
        | `import pandas as pd` | Load a package (Part 1). `pd.` in front of a name means "from pandas". |
        | `INPUT_FILE = Path("data/…")` | A setting. Names in CAPITALS at the top are settings: file names, thresholds. |
        | `def summarise_per_patient(samples):` | The start of a function. `samples` is what goes in. |
        | indented lines | Belong to the line above that ends with `:`. **In Python, indentation is the structure.** |
        | `return …` | What comes out of the function. |
        | `samples.groupby(…)` | Do `groupby` *on* `samples`. Read the dots from left to right, like `|>` in R. |
        | `# …` and `"""…"""` | Comments and descriptions for humans. Python ignores them. |

        ##### Python next to R

        Every line of `summary.py` has an R equivalent you already know:

        | Python (`summary.py`) | R |
        |---|---|
        | `import pandas as pd` | `library(dplyr)` |
        | `samples = pd.read_csv(INPUT_FILE)` | `samples <- read.csv(input_file)` |
        | `samples["patient_id"]` | `samples$patient_id` |
        | `len(samples)` | `nrow(samples)` |
        | `samples["patient_id"].nunique()` | `n_distinct(samples$patient_id)` |
        | `samples.groupby("patient_id").agg(mean_wbc=("wbc", "mean"))` | `samples |> group_by(patient_id) |> summarise(mean_wbc = mean(wbc))` |
        | `summary.round(1)` | `round(summary, 1)` |
        | `def f(samples):` … `return summary` | `f <- function(samples) { … summary }` |
        | `f"Read {n} samples"` | `paste("Read", n, "samples")` |
        | `summary.to_csv(OUTPUT_FILE)` | `write.csv(summary, output_file)` |

        Two differences to remember: Python uses `=` where R uses `<-`, and a Python function
        returns only what follows `return`.

        ##### Reading questions

        Work in pairs. Answer each question by pointing at **line numbers**.

        1. Which file does the script **read**?
        2. Which file does it **write**? What happens if that file already exists?
        3. Which function does the calculation? What goes in, and what comes out?
        4. Which lines decide that the result is the **mean**? Which would you change to get the
           median? (Just point at it, don't edit.)
        5. What is fixed in the code that you might want to choose yourself? Is there anything in
           the data that the script ignores?
        6. Does the script do anything you didn't ask for: delete, download or install something?

        ??? success "Answers"

            1. `data/cbc_samples.csv`: defined on line 12, read on line 28.
            2. `results/summary.csv`: defined on line 13, written on line 34. Line 33 first creates
               the `results` folder if it is missing. An existing file is **replaced without
               warning**, as you saw in Part 2.
            3. `summarise_per_patient` (lines 16–24), used on line 31. In goes the whole table of
               samples (`samples`); out comes one row per patient (`return`, line 24).
            4. Lines 20–22: `"mean"`. Changing those three to `"median"` would give medians.
               Line 19 counts the visits.
            5. The file names (lines 12–13) and the rounding to one decimal (line 24). The script
               also **ignores** the columns `neut_pct`, `lymph`, `sex` and `age`: only WBC,
               haemoglobin and platelets are summarised (lines 20–22). Nothing tells you that
               unless you read the code.
            6. No. Its only side effects are creating the `results` folder and writing
               `results/summary.csv`. Not every script an agent writes is that harmless, which is
               why you read before you run.

    ??? abstract "Part 4: Finding the bugs"

        The folder also has three changed versions of `summary.py`: `summary_v1.py`,
        `summary_v2.py` and `summary_v3.py`. Each one starts with the **task an agent was given**.
        Each has a problem. Your job is to find it.

        !!! warning "Prepared for demonstration"
            We wrote these scripts ourselves to show typical kinds of problems in agent-written
            code. A real agent can often avoid them or work around them on its own: it reads its
            own error messages and fixes them, and it may notice a suspicious number. But not
            always, and not reliably. The point is that **you** can recognise these problems when
            the agent doesn't.

        ##### Reading a traceback

        When a script crashes, Python prints a **traceback**. It looks long and scary; you only need
        two things from it:

        ```text hl_lines="5 6 13"
        Read 72 samples from 18 patients.
        Traceback (most recent call last):
          File "…/summary_v1.py", line 41, in <module>
            main()
          File "…/summary_v1.py", line 36, in main
            summary.to_excel(OUTPUT_FILE)
          File "…/pandas/core/generic.py", line 2268, in to_excel
            formatter.write(
          File "…/pandas/io/formats/excel.py", line 1003, in write
            writer = ExcelWriter(
          File "…/pandas/io/excel/_openpyxl.py", line 54, in __init__
            from openpyxl.workbook import Workbook
        ModuleNotFoundError: No module named 'openpyxl'
        ```

        1. **The last line says *what* went wrong:** a module called `openpyxl` is missing.
        2. **Going up, the last line that names *your* file says *where*:** `summary_v1.py`,
           line 36. Everything below it happens inside pandas, and is not your problem to read.

        ##### For each script

        1. Read the **task** at the top of the file.
        2. **Read the code before you run it.** Compare it with `summary.py`: what has changed?
        3. Run it: `python summary_v1.py`, and so on.
        4. Check the result against what you know about the data.
        5. Decide: does it crash, give a wrong answer, or do something you didn't ask for?

        ##### `summary_v1.py`: "Save the summary as an Excel file for my supervisor"

        ??? success "Answer"
            The code is fine: `to_excel` on line 36 is the right way to write an Excel file. But
            pandas needs an extra package, `openpyxl`, to do that, and it is not in the `miracle`
            environment. The problem is the **environment**, not the code.

            An agent would now offer to install `openpyxl`. Before you approve, ask the Part 1
            question: **into which environment?** It should be `miracle`, never `base`.

        ##### `summary_v2.py`: "Flag patients with anaemia (haemoglobin below 12)"

        ??? success "Answer"
            It runs and prints *0 of 18 patients flagged with anaemia*. That looks fine, but it is
            wrong. Haemoglobin in this data is in **g/L** (values from 82 to 158), while 12 is a
            threshold in **g/dL**. No value is below 12, so nobody is flagged (line 17).

            With thresholds in g/L (120 for women, 130 for men), **3 patients** are anaemic:
            P005, P011 and P017.

            The agent did exactly what it was asked. The mistake was in the **prompt**, and the
            code passed it on silently. A plausibility check catches it: does *nobody anaemic* make
            sense for this group of patients? What are the units of the data?

        ##### `summary_v3.py`: "Tidy up the data before summarising"

        ??? success "Answer"
            The output is exactly the same as from `summary.py`. But line 41 writes the "tidy"
            data **back over `data/cbc_samples.csv`**, keeping only five columns. Look:

            ```bash
            head -2 data/cbc_samples.csv
            ```

            `sex`, `age`, `neut_pct` and `lymph` are gone, for good. Only reading the code (the
            Part 3 question *does it do anything you didn't ask for?*) reveals it.

            Restore the original from the course materials:

            ```bash
            cp <course-materials>/Miracle-Winter-Academy/miracle-python-essentials/data/cbc_samples.csv data/
            ```

            This is why, in the afternoon, the agent gets the rule *never modify raw data*.

        ##### What the three have in common

        | Script | What you notice | How you catch it |
        |---|---|---|
        | `summary_v1.py` | A crash | The traceback tells you |
        | `summary_v2.py` | Nothing: a plausible number | Check the result against the data |
        | `summary_v3.py` | Nothing: the correct output | Read the code before you run it |

        The crash is the easy one. **The more normal the output looks, the more you need to
        check it.**

    #### Materials

    - Exercise files: `Miracle-Winter-Academy/miracle-python-essentials` in the course materials repository

=== "Advanced"

    ### Python tools for single-cell analysis

    #### Learning goals

    - Understand the `AnnData` object and the scverse ecosystem
    - Run a standard Scanpy workflow: QC, normalisation, HVGs, PCA, neighbours, UMAP, Leiden
    - Use scvi-tools for probabilistic modelling and batch integration
    - Move data between R (`SingleCellExperiment`/Seurat) and Python (`AnnData`)

    #### What we will do

    1. **AnnData anatomy.** `.X`, `.obs`, `.var`, `.obsm`, `.layers`; compare with
       `SingleCellExperiment`.
    2. **Scanpy workflow** on a public PBMC dataset, from raw counts to clusters and markers.
    3. **scvi-tools.** Train an scVI model, use the latent space for integration, and compare the
       result with PCA.
    4. **R ↔ Python.** Export to `.h5ad`; read it in R with `zellkonverter`; discuss pitfalls
       (raw vs normalised counts, metadata types).

    #### Materials

    - *Notebooks: to be added*

## Further reading

- [Scanpy tutorials](https://scanpy.readthedocs.io/en/stable/tutorials/index.html)
- [scvi-tools tutorials](https://docs.scvi-tools.org/en/stable/tutorials/index.html)
- [Single-cell best practices](https://www.sc-best-practices.org/)
