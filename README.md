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
