# Single-cell practical

<div class="session-meta" markdown>
:material-calendar: Thursday 3 Dec, 15:10–17:00
:material-account-group: <span class="pill basic">Basic</span> <span class="pill advanced">Advanced</span> (parallel rooms)
:material-laptop: Practical

:material-human-male-board: <span class="pill basic">Basic</span> Tomáš Preisler, Sára Veselá &nbsp;&nbsp; <span class="pill advanced">Advanced</span> Jan Stuchlý, Luděk Svoboda
</div>

!!! abstract "Draft, to be confirmed by instructors"

The final applied exercise of the week. You analyse single-cell data **with an AI agent**,
combining everything from the week: the review loop with Git, reading Python, instructing
agents, critical evaluation, and statistics. It follows the lecture *Computational analysis of
single-cell and flow data*.

!!! info "Before this session"
    The `miracle` Conda environment ([Python and Conda](../prerequisites/python-conda.md)) and
    [Claude Code](../prerequisites/claude-tools.md). Advanced track: scvi-tools and muon.

=== "Basic"

    ### Learning goals

    - Direct an agent through a standard single-cell workflow and understand each step
    - Choose and justify QC thresholds rather than accepting defaults
    - Identify and annotate cell populations, and recognise artefacts (doublets, platelets)
    - Apply multiple-testing correction when testing marker genes

    ### What we will do

    1. **Explore the data** (a public PBMC dataset): cells, genes, QC metrics. Ask the agent to
       *propose and justify* filtering thresholds.
    2. **Preprocessing:** normalisation, highly variable genes, PCA, neighbours, UMAP, clustering.
       Commit after each step.
    3. **Something looks odd:** investigate a suspicious cluster with the agent. Is it a real cell
       type or a doublet artefact? Verify the answer.
    4. **Markers and annotation:** marker genes per cluster with corrected p-values; check the
       annotation against literature and databases.
    5. **Report:** final annotated UMAP, cell-type proportions and a short methods paragraph.

=== "Advanced"

    ### Learning goals

    - Integrate multimodal single-cell data (e.g. RNA + surface protein)
    - Use probabilistic models (scvi-tools) for integration and compare with simpler methods
    - Evaluate integration quality critically

    ### What we will do

    1. **Multimodal data:** load a CITE-seq-type dataset (RNA + protein) as a `MuData` object.
    2. **Per-modality processing,** then joint analysis (e.g. weighted nearest neighbours, totalVI).
    3. **Compare** joint clustering with single-modality results: what does each modality add?
    4. **Critical evaluation:** where do the agent's choices (parameters, models) matter, and how do
       you check them?
    5. **Reproducibility:** a script and environment that a colleague can run.

## Materials

- *Datasets and starter notebooks: to be added*
