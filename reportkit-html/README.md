# reportkit-html

small python helper for generating **static, self-contained html reports**.

- no backend
- no templates required
- bundle css + js inline by default
- easy sections: text, tables, code blocks, images (optional data-uri)

## install (local)

```bash
python -m pip install -e .
```

## quick demo

```bash
python examples/demo.py
```

it writes `out/report.html`.

## usage

```python
from reportkit_html import Report

r = Report(title="my report")
r.add_h1("hello")
r.add_text("this is a report")
r.add_table(
    headers=["name","dps"],
    rows=[["twi", 9999],["trixie", 9001]],
)
r.write("report.html")
```

## notes

- this is intentionally tiny. if you want charts, embed your own svg/canvas.
- for images: pass a path and it will embed as a data-uri (optional).

