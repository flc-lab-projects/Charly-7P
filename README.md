# Wortkiste

A small vocabulary trainer for the school year. Two ways to practise each unit:
**Karten** (tap a card to flip between the two languages) and **Schreiben**
(the app shows one language, you type the other).

Runs as a plain static site — no build step, no dependencies. Add it to the
iPhone home screen and it behaves like an app.

## Live site

Published with GitHub Pages from the repository root:

    https://flc-lab-projects.github.io/Charly-7P/

## Adding vocabulary

**All content lives in `content/`. You never need to touch `index.html` to add words.**

### Adding phrases to an existing unit

Open the unit's `.tsv` file (e.g. `content/de/01-vorstellen.tsv`) and add a line.
On github.com you can do this in the browser — pencil icon, type, commit. It works
from a phone.

Columns are separated by a **tab**. Lines starting with `#` are ignored.

| # | Column | Required | What it is |
|---|--------|----------|------------|
| 1 | Answer language | yes | The phrase in the language being learnt (German) |
| 2 | Prompt language | yes | The same phrase in the language it's shown from (French) |
| 3 | Also correct | no | Other spellings that should count as right, separated by `\|` |
| 4 | Only | no | `karten` = flashcards only, `schreiben` = typing only, empty = both |

Example:

    Ich habe einen Bruder.	J'ai un frère.
    Ich bin 11 (Jahre alt).	J'ai 11 ans.	Ich bin 11|Ich bin elf
    Ich lese gern / nicht gern.	J'aime lire. / Je n'aime pas lire.		karten

The third line shows why column 4 exists: a phrase with a slash is fine on a
flashcard but has no single right answer to type, so the typing exercise skips it.
The two halves are added separately as `schreiben` rows.

### Adding a new unit

1. Create the file, e.g. `content/de/02-schule.tsv`, using the format above.
2. Add an entry to `content/index.json`:

```json
{
  "id": "de-02",
  "file": "de/02-schule.tsv",
  "language": "Deutsch",
  "title": "In der Schule",
  "subtitle": "Lektion 2",
  "prompt": "Français",
  "answer": "Deutsch",
  "colour": "green"
}
```

`id` must stay unique and must not change later — progress is stored against it.
`colour` is one of `blue`, `green`, `violet`, `orange`, `pink`, `teal`.

### Adding English

Same thing with `"language": "English"` and files under `content/en/`. As soon as
there is more than one language, the home screen grows a language filter on its own.

## Notes

- Progress (which phrases have been typed correctly) is stored in the browser on
  the device. Clearing Safari's website data resets it. It is keyed on the phrase
  itself, so adding new phrases to a unit doesn't wipe what's already done.
- `index.html` contains a tiny fallback lesson used only when `content/` can't be
  loaded — which happens if you open the file directly from disk instead of over
  http. A yellow banner says so when it happens. To preview locally:
  `python3 -m http.server` then open http://localhost:8000
- `make_content.py` generated the first unit from a photo of the textbook page.
  It isn't needed any more and can be deleted.

## Possible next steps

- A service worker, so the app is reliably available offline rather than
  depending on Safari's cache.
- Audio, if pronunciation becomes the thing that needs practice.
