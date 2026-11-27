# Python and Conda

You will not need to *write* much Python, but you will read, run and review Python code that the
AI agent generates, especially for single-cell analysis. **Conda** manages isolated Python
environments so that the course packages don't clash with anything else on your laptop.

We use **Miniforge**, a minimal Conda installer that uses the free `conda-forge` channel.

## Install Miniforge

=== "macOS"

    ```bash
    curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
    bash Miniforge3-$(uname)-$(uname -m).sh
    ```

    Accept the licence, keep the default location, and answer **yes** when asked whether to
    initialise Conda. Then **close and reopen** the terminal.

=== "Windows"

    1. Download **Miniforge3-Windows-x86_64.exe** from
       [conda-forge.org/download](https://conda-forge.org/download/).
    2. Run it: *Just Me*, default location, keep the default checkboxes.
    3. From the Start menu, open **Miniforge Prompt** and run:

        ```
        conda init bash
        ```

    4. Close Miniforge Prompt and open a **new Git Bash** window. From now on, use Git Bash for
       all `conda` commands: the AI agent runs in Git Bash and needs conda there.

=== "Linux"

    ```bash
    curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
    bash Miniforge3-$(uname)-$(uname -m).sh
    ```

    Accept the licence, keep the default location, and answer **yes** when asked whether to
    initialise Conda. Then **close and reopen** the terminal.

Check:

```bash
conda --version
```

## Create the course environment

1. Download the environment file:
   [:material-download: environment.yml](environment.yml){ download="environment.yml" .md-button }
2. In the terminal (Git Bash on Windows), go to the folder where you saved it.
   Usually that is your Downloads folder:

    ```bash
    cd ~/Downloads
    ```

3. Create the environment. This takes 5–15 minutes:

    ```bash
    conda env create -f environment.yml
    ```

4. Activate it and test:

    ```bash
    conda activate miracle
    python -c "import scanpy; print('scanpy OK')"
    ```

The environment contains Python 3.12, pandas, matplotlib, JupyterLab, pytest, **scanpy**,
**anndata** and **leidenalg**.

## Advanced track: extra packages

Install **scvi-tools** (deep generative models for single-cell data) and **muon** (multimodal
data). They pull in PyTorch, which is about 2–3 GB, so do this on a good connection:

```bash
conda activate miracle
conda install -c conda-forge scvi-tools muon
```

Check:

```bash
python -c "import scvi, muon; print('scvi-tools and muon OK')"
```

The Advanced Python session also downloads two public datasets (about 45 MB). You will do that
on Monday evening, once you have the course materials; see
[Get started](../workshops/python.md#get-started) in the Advanced tab.

!!! note "Package list to be confirmed"
    The instructors may update `environment.yml` before the course. If it changes, update your
    environment with `conda env update -n miracle -f environment.yml`.
