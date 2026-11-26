# R and RStudio

You need **R 4.4 or newer** and **RStudio Desktop**. If you already have both, check your R
version (`R.version.string` in the RStudio console) and skip to
[R packages](#course-r-packages).

## Install R

=== "macOS"

    1. Go to [cran.r-project.org/bin/macosx](https://cran.r-project.org/bin/macosx/).
    2. Download the installer matching your chip:
       **arm64** for Apple Silicon (M1/M2/M3/M4), **x86_64** for older Intel Macs.
       Unsure? Apple menu → *About This Mac* → *Chip*.
    3. Open the `.pkg` file and follow the steps.

=== "Windows"

    1. Go to [cran.r-project.org/bin/windows/base](https://cran.r-project.org/bin/windows/base/).
    2. Download **R-4.x.x-win.exe** and run it with the default options.
    3. Also install **Rtools** from
       [cran.r-project.org/bin/windows/Rtools](https://cran.r-project.org/bin/windows/Rtools/)
       (the version matching your R). Some packages need it to compile.

=== "Linux"

    Follow the instructions for your distribution at
    [cran.r-project.org/bin/linux](https://cran.r-project.org/bin/linux/). On Ubuntu:

    ```bash
    sudo apt update
    sudo apt install --no-install-recommends software-properties-common dirmngr
    wget -qO- https://cloud.r-project.org/bin/linux/ubuntu/marutter_pubkey.asc \
      | sudo tee /etc/apt/trusted.gpg.d/cran_ubuntu_key.asc
    sudo add-apt-repository "deb https://cloud.r-project.org/bin/linux/ubuntu $(lsb_release -cs)-cran40/"
    sudo apt install --no-install-recommends r-base r-base-dev
    # system libraries needed by common packages
    sudo apt install libcurl4-openssl-dev libssl-dev libxml2-dev libfontconfig1-dev \
      libharfbuzz-dev libfribidi-dev libfreetype6-dev libpng-dev libtiff5-dev libjpeg-dev libuv1-dev
    ```

    On Linux, R packages are compiled from source, so installing the course packages below
    takes longer than on macOS or Windows (about 5–15 minutes).

## Install RStudio Desktop

Download the free **RStudio Desktop** for your system from
[posit.co/download/rstudio-desktop](https://posit.co/download/rstudio-desktop/) and install it.
Install R first, then RStudio.

## Course R packages

Open RStudio and paste into the **Console**:

```r
install.packages(c(
  "tidyverse",  # data wrangling and plotting
  "here",       # project-relative file paths
  "testthat",   # simple automated tests
  "bench",      # timing code
  "renv",       # reproducible package environments
  "reticulate"  # calling Python from R
))
```

If asked *"Would you like to use a personal library instead?"*, answer **yes** (twice). This is
normal in the [course account](separate-account.md), which is not an administrator.

If asked *"Do you want to install from sources the packages which need compilation?"*,
answer **No**.

## Advanced track: extra packages

These let you move single-cell data between R and Python:

```r
install.packages("BiocManager")
BiocManager::install(c("SingleCellExperiment", "zellkonverter"))
```

!!! note "Package list to be confirmed"
    The instructors may add packages before the course. This page will be updated, so check it
    again the weekend before.
