# R refresher

<div class="session-meta" markdown>
:material-calendar: Monday 30 Nov, 15:35–17:00
:material-account-group: <span class="pill basic">Basic</span> <span class="pill advanced">Advanced</span> (parallel rooms)
:material-laptop: Practical

:material-human-male-board: <span class="pill basic">Basic</span> Jan Stuchlý, Luděk Svoboda &nbsp;&nbsp; <span class="pill advanced">Advanced</span> Tomáš Preisler, Sára Veselá
</div>

A puzzle-based R refresher with a **personal AI tutor**. You solve one puzzle step by step in
RStudio; the tutor, running in Claude Code next to your script, gives hints instead of answers
and checks your work, while the instructors lead the room. The goal is to bring everyone to the
same R level before Tuesday, when you will be reading and checking R code that an AI agent writes.
Understanding matters more than finishing.

!!! question "The puzzle: 100 bulbs"
    A corridor has 100 light bulbs, all off. 100 people walk past, one after another. Person *k*
    toggles (off → on, on → off) every bulb whose number is a multiple of *k*. Which bulbs are on
    at the end, and why?

!!! info "Before this session"
    [R, RStudio and the course R packages](../prerequisites/r-rstudio.md) installed,
    [Git](../prerequisites/git.md) set up, and [Claude Code](../prerequisites/claude-tools.md)
    installed and logged in with your MIRACLE Academy team account.

## Get started

Both tracks use the same project:
[`miracle-r-refresher`](https://github.com/rse-cuni/training-materials/tree/main/Miracle-Winter-Academy/miracle-r-refresher)
in the course materials repository.

1. Download the course materials (in the terminal, in your course working folder):

    ```bash
    git clone https://github.com/rse-cuni/training-materials.git
    ```

2. Copy the folder `training-materials/Miracle-Winter-Academy/miracle-r-refresher` to your
   working folder, so that your work does not end up in the course repository. Copy the whole
   folder: it contains a hidden `.claude` folder with the tutor's settings.
3. Open `r_levelling_basics.Rproj` in that copy. RStudio opens the project.
4. Open `work/bulbs.R`. This is where you write your code.
5. Switch to the **Terminal** tab in RStudio, type `claude`, and when Claude Code asks whether
   you trust the folder, answer yes. Then start the tutor with the name of your room:

    ```text
    start basic
    ```

    or

    ```text
    start advanced
    ```

!!! tip "How the AI tutor works"
    - **Ask for a hint** whenever you are stuck. Each request gives the next, more concrete hint:
      a question, then the concept, an example, the same idea on a different problem, and
      finally a skeleton with blanks.
    - **Type `check`** to have your script checked. The check reads the *saved* file, so save
      often (++ctrl+s++ / ++cmd+s++).
    - **Error messages:** paste them or just ask; the tutor explains what they mean.
    - **The solution:** the tutor won't hand it over at the first request, because working it out
      is the point. If you really want it, ask again and it will write the current step for you.
    - **`notes.md`** is yours: when you pass a step, the tutor writes up what you worked out,
      other approaches and the blind alleys you hit. Take it home.
    - The tutor can only run the check. It cannot run or change anything else on your laptop.

=== "Basic"

    ### Learning goals

    By the end you can read and reason about R code that uses:

    - vectors and their types, and indexing
    - nested `for` loops and `if`
    - your own functions with arguments, defaults and a return value, and input checks with
      `stopifnot()`
    - `sapply()`, a first plot, and a linear regression with `lm()`
    - error messages: what they say and where to look

    ### The route

    | Step | What you do | R you practise |
    |---|---|---|
    | 1 | Represent the 100 bulbs | vectors, types, `rep()` |
    | 2 | Let all 100 people walk past | nested `for` loops, `if`, `%%`, indexing |
    | 3 | Read the result | `which()`, `sum()` on logical vectors |
    | 4 | Any number of bulbs | functions, defaults, `stopifnot()` |
    | 5 | The R way: make it faster | vectorised conditions, `system.time()` |
    | 6 | Find the law: how many bulbs stay on? | `sapply()`, `plot()`, `lm()`, transformations |
    | 7 | Why these bulbs? (discussion) | own function, `identical()` |

    The instructor introduces each step at the whiteboard and leads the discussion of step 7.
    You work at your own pace; if you finish early, the tutor has extensions for you.

    ### Materials

    - [`miracle-r-refresher`](https://github.com/rse-cuni/training-materials/tree/main/Miracle-Winter-Academy/miracle-r-refresher):
      the puzzle project with the tutor (see [Get started](#get-started))

=== "Advanced"

    ### Learning goals

    - Move quickly through the core R constructs (loops, functions, `sapply()`, `lm()`)
    - Generalise a function to several arguments and validate every input
    - Replace loops with a matrix computation, and with mathematics
    - Measure time *and* memory, and predict how they grow with the size of the problem
    - Predict what code will do before running it, the skill you need to check AI-written code

    ### The route

    1. **Steps 1–7 at a brisk pace.** The same puzzle as the Basic track, from representing the
       bulbs to finding the law with a regression and proving it. Writing the function in
       step 7 is part of the route.
    2. **Extension A: N bulbs, M people.** Generalise your function so that the number of people
       can differ from the number of bulbs (`light_bulbs_nm()`). Predict the outcome first, for
       example for 100 bulbs and 60 people, then run it and explain what you see. Watch out for
       a quiet R behaviour that breaks naive solutions.
    3. **Extension B: speed and memory.** Two more versions of the same function: one with no
       loops at all, built on a matrix (`light_bulbs_matrix()`), and one that uses what step 7
       showed (`light_bulbs_math()`). Then compare all versions with `bench::mark()` for
       growing n and explain the differences in time and memory.

    The tutor checks both extensions just like the main steps. If you still have time, it has
    a few more extras (rule variants, moving functions into `R/` files with `source()`).

    !!! warning "Large n can freeze your laptop"
        A matrix of n × n values grows very quickly. Estimate its size with `object.size()` on a
        small example before you try a large n, and ask the tutor if unsure.

    ### Materials

    - [`miracle-r-refresher`](https://github.com/rse-cuni/training-materials/tree/main/Miracle-Winter-Academy/miracle-r-refresher):
      the puzzle project with the tutor (see [Get started](#get-started))

## Further reading

- [R for Data Science (2e)](https://r4ds.hadley.nz/)
- [Advanced R](https://adv-r.hadley.nz/), chapters on functions and vectors (Advanced track)
