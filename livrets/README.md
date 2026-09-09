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

Mirrors the school test: 30 calculations drawn at random, 3 minutes on the clock.
The 1, 10 and 11 livrets are left out as already secure — a calculation is excluded
if *either* of its numbers is one of those, so 7 × 10 doesn't appear either. The pool
is therefore 2–9 and 12, i.e. 81 possible calculations. No right/wrong feedback during the test — the review comes
at the end, listing every missed calculation with its answer. "Revoir ces calculs"
drops exactly those into the practice pile.

- The clock turns red for the last 30 seconds.
- "Passer ce calcul" moves on and counts as wrong, so nothing can stall the run.
- Leaving mid-test needs two taps on ←, so the test isn't lost by a mis-tap.
- The best score is kept on the device and shown on the Test tab.

To change the format, `TEST_N`, `TEST_SEC` and `TEST_SKIP` are near the top of the
script. Emptying `TEST_SKIP` puts every livret back in. The sentence on the Test tab
is generated from that list, so it always describes what will actually come up.

Note that Entraînement still offers all twelve livrets — only the test pool is narrowed.

## Publishing

Drop the `livrets` folder into the repository root:

    https://flc-lab-projects.github.io/Charly-7P/livrets/

Open in Safari, then Share → Add to Home Screen.

## Changing the wording

Every phrase is in the `T` object at the top of the `<script>` block. Vocabulary is
Swiss: *livret*, not *table de multiplication*. If a number ever needs spelling out,
use *septante*, *huitante*, *nonante*.
