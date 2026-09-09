# Les livrets

Times-tables app (1–12) in Swiss French, with two modes. Self-contained:
`index.html` plus an icon, no build step, no dependencies.

## Entraînement

Pick one or more livrets; every combination goes into a shuffled pile. A correct
answer removes the calculation for good, a wrong one shows the right answer and
puts it back a few places on, so it returns. The round ends when the pile is empty,
which means every calculation has been answered correctly at least once. No clock.

- ↺ restarts the same round with a fresh shuffle, at any point.
- ← goes back to the livret picker.
- The chosen livrets are remembered between visits.

## Test

Mirrors the school test: 30 calculations drawn at random from all twelve livrets,
3 minutes on the clock. No right/wrong feedback during the test — the review comes
at the end, listing every missed calculation with its answer. "Revoir ces calculs"
drops exactly those into the practice pile.

- The clock turns red for the last 30 seconds.
- "Passer ce calcul" moves on and counts as wrong, so nothing can stall the run.
- Leaving mid-test needs two taps on ←, so the test isn't lost by a mis-tap.
- The best score is kept on the device and shown on the Test tab.

To change the format, `TEST_N` and `TEST_SEC` are near the top of the script.

## Publishing

Drop the `livrets` folder into the repository root:

    https://flc-lab-projects.github.io/Charly-7P/livrets/

Open in Safari, then Share → Add to Home Screen.

## Changing the wording

Every phrase is in the `T` object at the top of the `<script>` block. Vocabulary is
Swiss: *livret*, not *table de multiplication*. If a number ever needs spelling out,
use *septante*, *huitante*, *nonante*.
