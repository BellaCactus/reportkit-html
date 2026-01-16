<div align="center">

# reportkit-html

a small python library for generating consistent, self-contained html reports for cli tools.

![python](https://img.shields.io/badge/python-3.11%2B-0b0b0b?style=for-the-badge)
![type](https://img.shields.io/badge/type-library-ff78c8?style=for-the-badge)
![license](https://img.shields.io/badge/license-mit-0b0b0b?style=for-the-badge)

</div>

---

## what is this?

reportkit-html is a tiny helper library used to generate clean, shareable html reports from python tools.

it is designed to be:
- consistent across multiple projects
- readable without external assets
- easy to embed into other tools
- stable and simple (small api surface)

---

## features

- single-file html output (self-contained)
- common report layout (header, sections, tables, key/value blocks)
- optional collapsible sections for long output
- minimal styling that works in dark or light environments

---

## install

requires python 3.11+.

### editable install (recommended for development)

```bash
python -m venv .venv
# windows
.venv\Scripts\activate
# mac/linux
source .venv/bin/activate

python -m pip install -U pip
python -m pip install -e .

quick start

run the included demo:

python examples/demo.py

it will generate an html file under out/ (or print the output path).

open the report in your browser:

    windows: double click the html file

    or serve locally if you prefer

usage (library)

basic pattern:

from reportkit_html import Report

r = Report(title="report title")
r.add_kv("file", "example.bin")
r.add_kv("status", "ok")

r.add_section("summary", "short human-readable summary text")

r.add_table(
    "results",
    columns=["name", "value"],
    rows=[
        ["alpha", "1"],
        ["beta", "2"],
    ],
)

r.write("report.html")

note: the exact helper method names may vary slightly between versions. check reportkit_html/__init__.py or examples/demo.py for the current public api.
philosophy

reportkit-html exists so other tools can focus on analysis while reports stay:

    consistent

    readable

    easy to share

it is intentionally not a templating engine. the goal is "good default reports" with minimal effort.
development

run the demo while iterating:

python examples/demo.py

if you modify the library code and installed editable (-e), changes apply immediately.
