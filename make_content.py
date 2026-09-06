# -*- coding: utf-8 -*-
"""Writes the content files. Only needed once — after this, phrases are edited
directly in the .tsv files (or on github.com), never here."""
import json, os, io

ROOT = os.path.dirname(os.path.abspath(__file__))

index = {
    "title": "Wortkiste",
    "units": [
        {
            "id": "de-01",
            "file": "de/01-vorstellen.tsv",
            "language": "Deutsch",
            "title": "Ich stelle mich vor",
            "subtitle": "Das kenne ich schon",
            "prompt": "Fran\u00e7ais",
            "answer": "Deutsch",
            "colour": "blue",
        }
    ],
}

HEADER = (
    "# Eine Zeile pro Satz. Die Spalten sind durch einen TAB getrennt:\n"
    "# 1) Deutsch   2) Fran\u00e7ais   3) auch richtig (mit | trennen)   4) nur: karten / schreiben\n"
    "# Spalte 3 und 4 d\u00fcrfen leer bleiben.\n"
)

# (deutsch, francais, auch_richtig, nur)
ROWS = [
    ("Ich heisse \u2026", "Je m\u2019appelle \u2026", "Ich heisse Lea", ""),
    ("Er heisst Jonas.", "Il s\u2019appelle Jonas.", "", ""),
    ("Sie heisst Lea.", "Elle s\u2019appelle Lea.", "", ""),
    ("Ich bin 11 (Jahre alt).", "J\u2019ai 11 ans.",
     "Ich bin 11|Ich bin 11 Jahre alt|Ich bin elf|Ich bin elf Jahre alt", ""),
    ("Er / Sie ist 11.", "Il / Elle a 11 ans.", "", "karten"),
    ("Er ist 11.", "Il a 11 ans.", "Er ist elf|Er ist 11 Jahre alt", "schreiben"),
    ("Sie ist 11.", "Elle a 11 ans.", "Sie ist elf|Sie ist 11 Jahre alt", "schreiben"),
    ("Ich wohne in Bern.", "J\u2019habite \u00e0 Berne.", "", ""),
    ("Er / Sie wohnt in Sitten.", "Il / Elle habite \u00e0 Sion.", "", "karten"),
    ("Er wohnt in Sitten.", "Il habite \u00e0 Sion.", "", "schreiben"),
    ("Sie wohnt in Sitten.", "Elle habite \u00e0 Sion.", "", "schreiben"),
    ("Ich komme aus der Schweiz.", "Je viens de Suisse.", "", ""),
    ("Er / Sie kommt aus \u00d6sterreich.", "Il / Elle vient d\u2019Autriche.", "", "karten"),
    ("Er kommt aus \u00d6sterreich.", "Il vient d\u2019Autriche.", "", "schreiben"),
    ("Ich spreche Deutsch.", "Je parle allemand.", "", ""),
    ("Er / Sie spricht Franz\u00f6sisch.", "Il / Elle parle fran\u00e7ais.", "", "karten"),
    ("Er spricht Franz\u00f6sisch.", "Il parle fran\u00e7ais.", "", "schreiben"),
    ("Die Nummer ist 079 421 35.", "Le num\u00e9ro est le 079 421 35.",
     "Die Telefonnummer ist 079 421 35", ""),
    ("Ich habe einen / keinen Bruder.", "J\u2019ai un fr\u00e8re. / Je n\u2019ai pas de fr\u00e8re.", "", "karten"),
    ("Ich habe einen Bruder.", "J\u2019ai un fr\u00e8re.", "", "schreiben"),
    ("Ich habe keinen Bruder.", "Je n\u2019ai pas de fr\u00e8re.", "", "schreiben"),
    ("Ich habe eine / keine Schwester.", "J\u2019ai une s\u0153ur. / Je n\u2019ai pas de s\u0153ur.", "", "karten"),
    ("Ich habe eine Schwester.", "J\u2019ai une s\u0153ur.", "", "schreiben"),
    ("Ich habe keine Schwester.", "Je n\u2019ai pas de s\u0153ur.", "", "schreiben"),
    ("Ich habe keine Geschwister.", "Je n\u2019ai pas de fr\u00e8res et s\u0153urs.", "", ""),
    ("Ich habe eine / keine Katze.", "J\u2019ai un chat. / Je n\u2019ai pas de chat.", "", "karten"),
    ("Ich habe eine Katze.", "J\u2019ai un chat.", "", "schreiben"),
    ("Ich habe keine Katze.", "Je n\u2019ai pas de chat.", "", "schreiben"),
    ("Er / Sie hat einen / keinen Hund.", "Il / Elle a un chien. / Il / Elle n\u2019a pas de chien.", "", "karten"),
    ("Er hat einen Hund.", "Il a un chien.", "", "schreiben"),
    ("Er hat keinen Hund.", "Il n\u2019a pas de chien.", "", "schreiben"),
    ("Ich lese gern / nicht gern.", "J\u2019aime lire. / Je n\u2019aime pas lire.", "", "karten"),
    ("Ich lese gern.", "J\u2019aime lire.", "", "schreiben"),
    ("Ich lese nicht gern.", "Je n\u2019aime pas lire.", "", "schreiben"),
    ("Er / Sie schwimmt gern / nicht gern.", "Il / Elle aime nager. / Il / Elle n\u2019aime pas nager.", "", "karten"),
    ("Er schwimmt gern.", "Il aime nager.", "", "schreiben"),
    ("Er schwimmt nicht gern.", "Il n\u2019aime pas nager.", "", "schreiben"),
    ("Meine Lieblingsfarbe ist Gr\u00fcn.", "Ma couleur pr\u00e9f\u00e9r\u00e9e est le vert.", "", ""),
]

with io.open(os.path.join(ROOT, "content", "index.json"), "w", encoding="utf-8") as f:
    json.dump(index, f, ensure_ascii=False, indent=2)
    f.write("\n")

with io.open(os.path.join(ROOT, "content", "de", "01-vorstellen.tsv"), "w", encoding="utf-8") as f:
    f.write(HEADER)
    for r in ROWS:
        f.write("\t".join(r).rstrip("\t") + "\n")

cards = sum(1 for r in ROWS if r[3] != "schreiben")
write = sum(1 for r in ROWS if r[3] != "karten")
print("rows:", len(ROWS), "| karten:", cards, "| schreiben:", write)
