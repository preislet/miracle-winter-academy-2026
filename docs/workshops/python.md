# Python

<div class="session-meta" markdown>
:material-calendar: Tuesday 1 Dec, 10:35–12:15
:material-account-group: <span class="pill basic">Basic</span> <span class="pill advanced">Advanced</span> (parallel rooms, different topics)
:material-human-male-board: MIRACLE Research Software Engineering team
:material-laptop: Practical
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

    1. **Python for R users.** Side-by-side: vectors ↔ lists/NumPy arrays, data frames ↔ pandas,
       `library()` ↔ `import`, indexing from 0 vs 1.
    2. **Environments.** `conda activate miracle`, `conda list`, why environments exist.
    3. **Run a script.** `python analysis.py` and a Jupyter notebook. When to use which.
    4. **Read before you run.** Annotate an agent-generated script line by line in pairs.
    5. **Find the bug.** Several AI-generated scripts, each with a planted error (wrong column,
       off-by-one, silent `NaN`, wrong file path). Find it from the code and the traceback.

    #### Materials

    - *Exercise scripts: to be added*

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
    - Instructors: Jan Stuchlý, Tomáš Preisler *(to be confirmed)*

## Further reading

- [Scanpy tutorials](https://scanpy.readthedocs.io/en/stable/tutorials/index.html)
- [scvi-tools tutorials](https://docs.scvi-tools.org/en/stable/tutorials/index.html)
- [Single-cell best practices](https://www.sc-best-practices.org/)
