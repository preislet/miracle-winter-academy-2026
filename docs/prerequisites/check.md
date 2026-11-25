# Check your setup

Run each check below. Every command should print a version number rather than an error.
If something fails, go back to the relevant page. If you cannot fix it, bring the error
message to Monday's [environment setup](../workshops/environment-setup.md) session.

## In the terminal

Use Terminal on macOS/Linux and Git Bash on Windows. Run the `conda` lines in Miniforge Prompt
if `conda` is not found in Git Bash.

```bash
git --version                 # git version 2.x
gh auth status                # Logged in to github.com account <you>
claude --version              # x.y.z (Claude Code)
conda --version               # conda 2x.x
conda run -n miracle python -c "import scanpy, anndata, leidenalg; print('Python OK, scanpy', scanpy.__version__)"
```

=== "Basic"

    That's all for the Basic track.

=== "Advanced"

    Also check the extra single-cell packages:

    ```bash
    conda run -n miracle python -c "import scvi, muon; print('scvi-tools', scvi.__version__)"
    ```

## In RStudio

Paste into the **Console**:

```r
R.version.string                       # R version 4.4 or newer
pkgs <- c("tidyverse", "here", "testthat", "bench", "renv", "reticulate")
missing <- pkgs[!vapply(pkgs, requireNamespace, logical(1), quietly = TRUE)]
if (length(missing)) message("Missing: ", paste(missing, collapse = ", ")) else message("R packages OK")
```

=== "Basic"

    That's all for the Basic track.

=== "Advanced"

    ```r
    requireNamespace("zellkonverter")    # should return TRUE
    ```

## In Positron

Open Positron. The interpreter picker (top right) should list your **R** installation and
**Python (`miracle`)**. See [Positron](positron.md#check-that-it-finds-r-and-python).

## Everything passed?

You're ready. See you on **Monday 30 November at 09:00**!
