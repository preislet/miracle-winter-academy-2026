# Positron

[Positron](https://positron.posit.co/) is a free data-science IDE from Posit, the makers of
RStudio. It works with **both R and Python** in one window: consoles, a data explorer, plots and
notebooks. It is built on the same base as VS Code. We use it in the sessions where R and Python
meet, such as the Python and single-cell practicals.

!!! info "Install R and Conda first"
    Positron finds your existing R and Python installations automatically. Install
    [R](r-rstudio.md) (4.4 or newer) and the [course Conda environment](python-conda.md) first.

## Install Positron

Download the installer for your system from
[positron.posit.co/download](https://positron.posit.co/download.html). The download is about
0.5–0.9 GB.

=== "macOS"

    macOS 11 or newer. Pick **Apple Silicon** (M1/M2/M3/M4) or **Intel**, matching your Mac.
    Open the `.dmg` file and drag Positron into *Applications*.

=== "Windows"

    Windows 10 or 11.

    1. First install the latest **Microsoft Visual C++ Redistributable**:
       [vc_redist.x64.exe](https://aka.ms/vs/17/release/vc_redist.x64.exe).
    2. Download the Positron **User install** for **x64**. Use ARM64 only on Windows-on-ARM
       laptops. The user install does not need administrator rights.
    3. Run the installer.

    Rtools, which you installed with [R](r-rstudio.md), is needed to build some R packages.

=== "Linux"

    Download the `.deb` package (Ubuntu/Debian) or the `.rpm` package (Fedora/RHEL) for your
    architecture, then install it:

    ```bash
    sudo apt install ./Positron-*.deb      # Ubuntu / Debian
    sudo dnf install ./Positron-*.rpm      # Fedora / RHEL
    ```

## Check that it finds R and Python

1. Open Positron.
2. Click the interpreter picker in the top-right corner of the window.
3. You should see your **R** installation and a **Python** entry for the `miracle` Conda
   environment. Select R and run `1 + 1` in the console, then select Python (`miracle`) and run
   `import scanpy`.

If the `miracle` environment is missing from the list, see
[Python installations](https://positron.posit.co/python-installations.html) in the Positron docs.

!!! tip "Coming from RStudio?"
    Positron's [migration guide](https://positron.posit.co/migrate-rstudio.html) explains where
    familiar RStudio features live in Positron. Keep RStudio installed too; both are used during
    the course.
