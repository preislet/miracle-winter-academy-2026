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

Both tracks use the same project, `Miracle-Winter-Academy/miracle-r-refresher` in the
[course materials repository](https://github.com/rse-cuni/training-materials).

- [ ] **Download the course materials** into your home folder. You will use this repository
    for the rest of the week.

    ```bash
    cd ~
    git clone https://github.com/rse-cuni/training-materials.git
    ```

- [ ] **Copy the project** into your `~/miracle-academy` folder, so that your work doesn't end
    up in the course repository. `cp -r` copies the whole folder, including the hidden `.claude`
    folder with the tutor's settings.

    ```bash
    cp -r ~/training-materials/Miracle-Winter-Academy/miracle-r-refresher ~/miracle-academy/
    ```

- [ ] **Open the project in RStudio:** *File → Open Project…* →
    `~/miracle-academy/miracle-r-refresher/r_levelling_basics.Rproj`.
- [ ] **Open `work/bulbs.R`.** This is where you write your code. Each step has a section with
    the names of the objects the check looks for.
- [ ] **Start Claude Code** in the RStudio **Terminal** tab (not the Console). When it asks
    whether you trust the folder, answer yes.

    ```bash
    claude
    ```

!!! warning "Start the tutor with the name of your room!"
    Your first message to the tutor decides which route it guides you through.

    In the <span class="pill basic">Basic</span> room type:

    ```text
    start basic
    ```

    In the <span class="pill advanced">Advanced</span> room type:

    ```text
    start advanced
    ```

    Typed only `start`? The tutor will ask you which room you are in.

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

### Common problems

??? question "The check says `object 'bulbs' not found`"
    At the `bulbs_start` line, this only means step 1 is not written yet. Keep the line
    `bulbs_start <- bulbs` right after your step-1 code.

??? question "The check disagrees with what I see in RStudio"
    The check reads the file on disk. Save (++ctrl+s++ / ++cmd+s++) and type `check` again.

??? question "The check reports a timeout"
    Is there a `print()` left inside a loop or a function? The check calls your functions with
    large `n` (up to 1000 bulbs, so a million prints). Remove the prints from functions.

??? question "A step passed earlier and fails now"
    Look for a later line that changes the same object, for example a test such as
    `bulbs <- light_bulbs(10)` or a pasted example. The check runs the whole file from top to
    bottom.

??? question "`claude` does nothing, or the tutor ignores the puzzle"
    Check that you are in the RStudio **Terminal** tab and that RStudio has the
    `r_levelling_basics.Rproj` project open: Claude Code must start *inside* the project folder
    to find the tutor's instructions. Then type `start basic` or `start advanced` again.

=== "Basic"

    ### Learning goals

    By the end you can read and reason about R code that uses:

    - vectors and their types, and indexing
    - nested `for` loops and `if`
    - your own functions with arguments, defaults and a return value, and input checks with
      `stopifnot()`
    - `sapply()`, a first plot, and a linear regression with `lm()`
    - error messages: what they say and where to look

    ### What we will do

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
    You work at your own pace; the tutor helps you along.

    ??? abstract "Step 1: Represent the bulbs"

        How can R hold the state of all 100 bulbs at the start? Store it as **`bulbs`**, and
        keep the line `bulbs_start <- bulbs` right after it: it saves the starting state.

        - What can a single bulb be? How could you write one bulb's state as a value in R?
        - **Any** way of writing on/off works. The choice is yours, and you can keep it for the
          whole puzzle.

        !!! success "Checkpoint"
            `check` reports `STEP 1 PASS`.

    ??? abstract "Step 2: Everyone acts"

        Person *k* toggles every bulb whose number is a multiple of *k*. Change **`bulbs`** so
        that it holds the state after all 100 people. This is the heart of the session.

        - Forget the other people first: what exactly does person 2 do? How do you decide, for
          one bulb, whether person 2 touches it?
        - Then: what changes for person 3, and for every person?
        - Watch it happen: try 10 bulbs and put a `print()` inside the loop.

        !!! success "Checkpoint"
            `check` reports `STEP 2 PASS`.

        ##### Common problems

        ??? question "`unexpected '='`"
            In R, `=` assigns. How do you *compare* two numbers?

        ??? question "`missing value where TRUE/FALSE needed`"
            The condition of an `if` is `NA`. Print the condition just before the `if`: what
            value does it have?

    ??? abstract "Step 3: Read the result"

        **`on_bulbs`**: the *numbers* of the bulbs that are on.

        - `bulbs` says on or off for each position. How would you ask R *which positions*
          are on?
        - Once it passes: what do these numbers have in common?

        !!! success "Checkpoint"
            `check` reports `STEP 3 PASS`.

    ??? abstract "Step 4: Any number of bulbs"

        Wrap your step-2 code into a function **`light_bulbs(n = 100)`**: it returns the state of
        the bulbs after *n* people have acted on *n* bulbs, and stops with an error unless `n` is
        a whole number ≥ 1.

        - Which numbers in your step-2 code really mean "the number of bulbs"?
        - What should `light_bulbs()` return with no argument? And `light_bulbs(2.5)`?

        !!! success "Checkpoint"
            `check` reports `STEP 4 PASS`. It calls your function with 10, 100 and 1000 bulbs, and
            with inputs that should fail.

    ??? abstract "Step 5: The R way"

        **`light_bulbs_fast(n = 100)`**: the same result, but faster. Replace the inner loop and
        its `if` with one vectorised line.

        - In step 3 you turned a TRUE/FALSE vector into bulb numbers. Could one line give you
          *all* the bulbs person *k* touches?
        - Then compare `system.time(light_bulbs(2000))` with `system.time(light_bulbs_fast(2000))`.

        !!! success "Checkpoint"
            `check` reports `STEP 5 PASS` and how many times faster your new function is
            (`speedup=`).

    ??? abstract "Step 6: Find the law"

        **`n_lit(n)`**: how many bulbs are lit after *n* people on *n* bulbs. Collect it for many
        *n* (say 1 to 500) with `sapply()`, **plot it**, then fit a model with `lm()` and save it
        as **`fit`**.

        - What does the plot look like? Does a straight line describe it?
        - What could you do to one side of the formula, or both, so that the points fall on a
          line?
        - What does your model say: if *n* grows 100 times, how many times more bulbs are lit?

        !!! success "Checkpoint"
            `check` reports `STEP 6 PASS r2=…`. A model passes when it follows the points closely
            (R² ≥ 0.99), which a plain straight line doesn't.

    ??? abstract "Step 7: Why these bulbs?"

        A discussion with the whole room, led by the instructor: the regression *suggested* the
        law, now we *prove* it.

        - Who toggles bulb 12? How many times? Will it be on or off?
        - And bulb 16?

        Optional: write **`n_divisors(n)`**, which counts how many divisors the number *n* has,
        and check the link with `identical()`.

        !!! success "Checkpoint"
            `check` reports `STEP 7 PASS` (only if you wrote `n_divisors`).

    ??? abstract "Finished early? Extensions"

        Ask the tutor about them. They are not checked automatically, so go through your code
        with the tutor.

        - `seq(person, n, by = person)` gives the same bulb numbers as your `which()` line.
          Verify it with `identical()`.
        - Change the rules: only odd-numbered people act; person *k* only switches bulbs *on*;
          count how many times each bulb was toggled.
        - Move your functions into `R/bulbs_functions.R` and load them with `source()` at the top
          of `work/bulbs.R`. The check must still pass.

    ### Materials

    - Puzzle project: `Miracle-Winter-Academy/miracle-r-refresher` in the
      [course materials repository](https://github.com/rse-cuni/training-materials/tree/main/Miracle-Winter-Academy/miracle-r-refresher)
      (see [Get started](#get-started))

=== "Advanced"

    ### Learning goals

    - Move quickly through the core R constructs (loops, functions, `sapply()`, `lm()`)
    - Generalise a function to several arguments and validate every input
    - Replace loops with a matrix computation, and with mathematics
    - Measure time *and* memory, and predict how they grow with the size of the problem
    - Predict what code will do before running it, the skill you need to check AI-written code

    ### What we will do

    1. **Steps 1–7 at a brisk pace.** The same puzzle as the Basic track, from representing the
       bulbs to finding the law with a regression and proving it.
    2. **Extension A: N bulbs, M people.** Generalise your function, predict what it does, and
       explain a surprising result.
    3. **Extension B: speed and memory.** Two more versions of the same function, one built on a
       matrix and one on mathematics, and a benchmark of all of them.

    The tutor checks both extensions just like the main steps.

    ??? abstract "Part 1: Steps 1–7"

        Work through the steps in `work/bulbs.R` with the tutor. The objects the check looks for:

        | Step | Create | What it is |
        |---|---|---|
        | 1 | `bulbs` (and keep `bulbs_start <- bulbs`) | the 100 bulbs at the start, any on/off encoding |
        | 2 | `bulbs` | the state after all 100 people: nested loops and `if` |
        | 3 | `on_bulbs` | the numbers of the bulbs that are on |
        | 4 | `light_bulbs(n = 100)` | steps 1–2 as a function, with input validation |
        | 5 | `light_bulbs_fast(n = 100)` | the same without the inner loop |
        | 6 | `n_lit(n)` and `fit` | lit bulbs for many *n*, a plot, and an `lm()` that follows the points (R² ≥ 0.99) |
        | 7 | `n_divisors(n)` | the number of divisors of *n*: why exactly these bulbs stay on |

        In the Advanced track, step 7 is part of the route: you need its result for extension B.
        If the room hasn't discussed it yet, discuss it with the tutor.

        !!! success "Checkpoint"
            `check` reports `STEP 1 PASS` to `STEP 7 PASS`.

    ??? abstract "Part 2: Extension A, N bulbs and M people"

        So far there were always as many people as bulbs. Write
        **`light_bulbs_nm(n_bulbs = 100, n_people = n_bulbs)`**, which returns the state of
        `n_bulbs` bulbs after `n_people` people.

        - [ ] `light_bulbs_nm()` gives the familiar 100 bulbs, and `light_bulbs_nm(10)` uses
            10 people.
        - [ ] It stops with an error unless **both** arguments are whole numbers ≥ 1.
        - [ ] More people than bulbs works, and the result still has exactly `n_bulbs` values.

        ##### Predict first, then run

        Before you run anything, write down which bulbs you expect to be on. Then run your
        function and compare. This is exactly how you will check an agent's code tomorrow: know
        what the answer should look like *before* you see it.

        | Bulbs | People | Your prediction |
        |---|---|---|
        | 100 | 1 | |
        | 100 | 2 | |
        | 100 | 150 | |
        | 100 | 60 | |

        ??? success "Answer"
            - **1 person:** all bulbs are on. Person 1 touches every bulb once.
            - **2 people:** the odd bulbs. Person 2 switches the even ones back off.
            - **150 people:** the same bulbs as with 100 people. People 101–150 have no bulb to
              touch.
            - **60 people:** up to bulb 60 the familiar result; from 61 on, the opposite: every
              bulb that was off with 100 people is on, and the other way round. Why? A bulb
              *b* > 60 has all its divisors except *b* itself at most *b*/2 ≤ 50. So it misses
              exactly one toggle, its own person's, and ends flipped. The same holds for any
              number of people between *n*/2 and *n*.

        - How long is your result for 12 bulbs and 30 people? Which bulb numbers does person 20
          try to touch, and what does R do when you assign to `x[20]` while `x` has 12 values?

        !!! success "Checkpoint"
            `check` reports `STEP A PASS`.

    ??? abstract "Part 3: Extension B, speed and memory"

        Two more versions of `light_bulbs(n = 100)`, each with exactly the same result.

        **`light_bulbs_matrix(n = 100)`**: no loops and no `sapply()` at all. Could you write
        down, for *every* person and *every* bulb at once, whether that person touches that bulb?
        What shape would that table have, and how do you get from it to on or off?

        **`light_bulbs_math(n = 100)`**: use what step 7 showed. No matrix, and no simulating
        the people. The check runs it with a million bulbs and wants the result in under
        2 seconds.

        !!! warning "Large n can freeze your laptop"
            A matrix of *n* × *n* values grows very quickly. Before you try a large *n*, measure
            a small one with `object.size(matrix(TRUE, 1000, 1000))` and **predict** the size for
            the *n* you have in mind.

        !!! success "Checkpoint"
            `check` reports `STEP B1 PASS` and `STEP B2 PASS`.

        ##### Benchmark

        Compare the versions with `bench::mark()`. It runs each expression several times, checks
        that all results are identical, and reports time and memory:

        ```r
        bench::mark(
          light_bulbs(1000),
          light_bulbs_fast(1000),
          light_bulbs_matrix(1000),
          light_bulbs_math(1000)
        )
        ```

        Look at the columns `median` (time) and `mem_alloc`: all the memory R allocated during
        the run, including temporary values it threw away. Then repeat with
        `n = 2000` and `n = 4000`, leaving out `light_bulbs()` for the larger values, and fill in:

        | Version | Time at 1000 → 2000 → 4000 | Memory at 1000 → 2000 → 4000 |
        |---|---|---|
        | `light_bulbs` | | |
        | `light_bulbs_fast` | | |
        | `light_bulbs_matrix` | | |
        | `light_bulbs_math` | | |

        - When *n* doubles, how many times longer does each version take, and how much more
          memory does it allocate?
        - `light_bulbs_fast` and `light_bulbs_matrix` allocate about the same memory in total.
          So why is it only the matrix version that runs out of memory for large *n*?
        - Which version would you use for 10 000 bulbs? For a million?
        - `bench::mark()` complains that the results differ? Then your versions don't use the
          same on/off encoding. That is a finding, not a bug in `bench`.

        ??? success "What to look for"
            - **Time:** the loop versions and the matrix version all do about *n*² work, so
              doubling *n* makes each of them about 4 times slower. The nested loops are the
              slowest; `light_bulbs_fast` and the matrix version are close.
            - **Memory in total vs at once:** `light_bulbs_fast` and the matrix version allocate
              about the same in total, 4 times more for every doubling. But `light_bulbs_fast`
              allocates it in small pieces, one person at a time, and R reuses that memory. The
              matrix version needs all *n*² values *at the same time*, and that is what stops it
              for large *n*. `mem_alloc` doesn't show this difference, but your
              `object.size()` estimate does.
            - `light_bulbs_math` takes microseconds and grows only with *n*: it wins by thinking,
              not by code.

        ##### What the versions have in common

        All five functions give the same answer, and the check accepts each of them. What
        differs is how long they take, how much memory they need, and how easy they are to
        trust. **The version you understand is the one you check the others against**, for
        example with `identical(light_bulbs_math(500), light_bulbs_fast(500))`. Tomorrow you do
        the same with code an AI agent writes.

    ### Materials

    - Puzzle project: `Miracle-Winter-Academy/miracle-r-refresher` in the
      [course materials repository](https://github.com/rse-cuni/training-materials/tree/main/Miracle-Winter-Academy/miracle-r-refresher)
      (see [Get started](#get-started))

## Further reading

- [R for Data Science (2e)](https://r4ds.hadley.nz/)
- [Advanced R](https://adv-r.hadley.nz/), chapters on functions and vectors (Advanced track)
