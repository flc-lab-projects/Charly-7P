# Les livrets

Times-tables drill (1–12), in Swiss French. Self-contained: `index.html` plus an icon,
no build step, no dependencies.

## How it works

Pick one or more livrets on the first screen, then every combination from those
tables goes into a pile in random order. A correct answer removes the calculation
from the pile for good; a wrong one shows the right answer and puts the calculation
back a few places further on, so it returns. The round ends only when the pile is
empty — meaning every calculation has been answered correctly at least once.

- The progress bar tracks the pile emptying, and the yellow badge shows how many are left.
- ↺ (top right) restarts the same round with a fresh shuffle, at any point.
- ← (top left) goes back to the livret picker.
- The chosen livrets are remembered on the device between visits.

## Publishing

Drop the `livrets` folder into the repository root. It becomes:

    https://flc-lab-projects.github.io/Charly-7P/livrets/

Open that in Safari, then Share → Add to Home Screen for its own icon.

## Changing the wording

Every phrase the app shows is in the `T` object at the top of the `<script>` block
in `index.html`. Vocabulary is Swiss: *livret* rather than *table de multiplication*.
Should any number ever need spelling out, use *septante*, *huitante*, *nonante*.
