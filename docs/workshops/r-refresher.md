# R refresher

<div class="session-meta" markdown>
:material-calendar: Monday 30 Nov, 15:35–17:00
:material-account-group: <span class="pill basic">Basic</span> <span class="pill advanced">Advanced</span> (parallel rooms)
:material-human-male-board: MIRACLE Research Software Engineering team
:material-laptop: Practical
</div>

!!! abstract "Draft, to be confirmed by instructors"

A puzzle-based R refresher with **individual AI tutoring**. You work through a puzzle step by
step; an AI tutor gives hints instead of answers, and instructors circulate. The goal is to bring
everyone to the same R level before the AI-assisted coding sessions on Tuesday.

!!! info "Before this session"
    [R, RStudio and the course R packages](../prerequisites/r-rstudio.md) installed.

!!! tip "How the AI tutor works"
    The tutor is set up to *guide*, not to solve: it asks questions, points to the relevant
    function and explains error messages. Asking it for the full solution defeats the purpose.

=== "Basic"

    ### Learning goals

    - Work confidently with vectors, indexing and data frames
    - Write `for` loops and `if` conditions
    - Write your own small functions with arguments and return values
    - Make a basic plot and fit a simple linear regression

    ### What we will do

    1. **Warm-up puzzle:** vectors, indexing, `seq()`, `sum()`, logical conditions.
    2. **Loops:** repeat a calculation over many samples; collect the results.
    3. **Functions:** turn the repeated code into a function; add arguments and defaults.
    4. **Plotting:** visualise the result with base R or `ggplot2`.
    5. **Regression:** fit `lm()`, read the summary, plot the fitted line.
    6. Each step comes with hints from the AI tutor and a checkpoint to verify your answer.

    ### Materials

    - *Puzzle repository: to be added*

=== "Advanced"

    ### Learning goals

    - Replace loops with vectorised code and measure the difference
    - Write reusable functions and keep them in separate files (`source()`, project structure)
    - Extend an existing solution to a harder version of the problem

    ### What we will do

    1. **Same puzzle, faster pace:** solve the core puzzle quickly with the AI tutor.
    2. **Vectorise and time it:** rewrite loop solutions with vectorised operations and
       `apply`-family functions; compare with `bench::mark()`.
    3. **Structure:** move functions into `R/` files, load them with `source()`, and use `here()`
       for paths.
    4. **Puzzle extensions:** generalise the solution, handle edge cases, add a `testthat` test.

    ### Materials

    - *Puzzle repository: to be added*

## Further reading

- [R for Data Science (2e)](https://r4ds.hadley.nz/)
- [Advanced R](https://adv-r.hadley.nz/), chapters on functions and vectors (Advanced track)
