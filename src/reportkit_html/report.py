from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable, Sequence

from .util import esc, file_to_data_uri


_DEFAULT_CSS = r"""
:root{
  --bg:#070707;
  --bg2:#0b0b0b;
  --panel: rgba(255,255,255,0.055);
  --panel2: rgba(255,255,255,0.03);
  --border: rgba(255,255,255,0.10);
  --text:#f7f7f7;
  --muted:#b9b9c2;
  --pink:#ff78c8;
  --pink2:#ffb3e6;
  --shadow: 0 20px 70px rgba(0,0,0,0.55);
  --radius:16px;
  --mono: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
  --sans: ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, Arial, sans-serif;
}
*{box-sizing:border-box;}
html,body{height:100%;}
body{
  margin:0;
  background:
    radial-gradient(800px 500px at 15% 10%, rgba(255,120,200,0.14), transparent 55%),
    radial-gradient(900px 600px at 90% 30%, rgba(255,179,230,0.10), transparent 55%),
    radial-gradient(1000px 700px at 40% 95%, rgba(255,77,184,0.08), transparent 55%),
    linear-gradient(180deg, var(--bg), var(--bg2));
  color:var(--text);
  font-family: var(--sans);
  line-height:1.55;
}
a{color:var(--pink); text-decoration:none;}
a:hover{text-decoration:underline;}
.wrap{max-width:980px; margin:0 auto; padding:34px 16px 80px;}
.header{display:flex; justify-content:space-between; gap:12px; align-items:flex-end; margin-bottom:14px;}
.title{margin:0; font-size:2rem; letter-spacing:0.5px;}
.sub{color:var(--muted); font-family:var(--mono); font-size:0.9rem;}
.panel{background: linear-gradient(180deg, var(--panel), var(--panel2)); border:1px solid var(--border);
  border-radius: var(--radius); box-shadow: var(--shadow); overflow:hidden; margin-top:12px;}
.panelInner{padding:14px 16px;}
.h1{font-size:1.35rem; margin:0 0 10px; color:var(--pink2); letter-spacing:0.2px;}
.h2{font-size:1.1rem; margin:18px 0 8px; color:var(--pink2); letter-spacing:0.2px;}
.p{margin:0 0 10px; color:rgba(255,255,255,0.92);}
.hr{border:0; border-top:1px dashed rgba(255,255,255,0.10); margin:14px 0;}
.code{font-family:var(--mono); font-size:12px; background:rgba(0,0,0,0.35); border:1px solid rgba(255,255,255,0.10);
  border-radius:14px; padding:12px; overflow:auto; white-space:pre;}
.kv{display:grid; grid-template-columns: 180px 1fr; gap:8px 12px; font-family:var(--mono); font-size:0.86rem;}
.k{color:rgba(255,255,255,0.70);}
.v{color:rgba(255,255,255,0.94);}
.tableWrap{overflow:auto; border:1px solid rgba(255,255,255,0.10); border-radius:14px;}
table{width:100%; border-collapse:collapse; font-family:var(--mono); font-size:0.86rem;}
th,td{padding:10px 10px; border-bottom:1px dashed rgba(255,255,255,0.10); text-align:left;}
th{color:var(--pink2); background:rgba(0,0,0,0.22); position:sticky; top:0;}
tr:hover td{background:rgba(255,120,200,0.06);}
.badge{display:inline-flex; gap:8px; align-items:center; font-family:var(--mono); font-size:0.78rem; padding:6px 10px;
  border-radius:999px; border:1px solid rgba(255,255,255,0.10); background:rgba(0,0,0,0.22); color:rgba(255,255,255,0.88);}
.dot{width:7px; height:7px; border-radius:999px; background:var(--pink); box-shadow:0 0 12px rgba(255,120,200,0.55);}
img{max-width:100%; border-radius:14px; border:1px solid rgba(255,255,255,0.10);}
.footer{margin-top:18px; text-align:center; color:var(--muted); font-size:0.86rem; font-family:var(--mono);}
"""


@dataclass
class Report:
    title: str = "report"
    subtitle: str | None = None
    css: str = _DEFAULT_CSS
    _blocks: list[str] = field(default_factory=list)

    def add_badge(self, text: str) -> None:
        self._blocks.append(
            f'<div class="badge"><span class="dot" aria-hidden="true"></span>{esc(text)}</div>'
        )

    def add_hr(self) -> None:
        self._blocks.append('<div class="hr"></div>')

    def add_h1(self, text: str) -> None:
        self._blocks.append(f'<div class="h1">{esc(text)}</div>')

    def add_h2(self, text: str) -> None:
        self._blocks.append(f'<div class="h2">{esc(text)}</div>')

    def add_text(self, text: str) -> None:
        # allow simple newlines
        safe = "<br>".join(esc(text).splitlines())
        self._blocks.append(f'<div class="p">{safe}</div>')

    def add_kv(self, items: Sequence[tuple[str, object]]) -> None:
        rows = []
        for k, v in items:
            rows.append(f'<div class="k">{esc(k)}</div><div class="v">{esc(v)}</div>')
        self._blocks.append(f'<div class="kv">{"".join(rows)}</div>')

    def add_code(self, code: str) -> None:
        self._blocks.append(f'<pre class="code">{esc(code)}</pre>')

    def add_table(self, headers: Sequence[str], rows: Iterable[Sequence[object]]) -> None:
        thead = "".join(f"<th>{esc(h)}</th>" for h in headers)
        body_rows = []
        for r in rows:
            tds = "".join(f"<td>{esc(c)}</td>" for c in r)
            body_rows.append(f"<tr>{tds}</tr>")
        tbody = "".join(body_rows)
        self._blocks.append(
            f'<div class="tableWrap"><table><thead><tr>{thead}</tr></thead><tbody>{tbody}</tbody></table></div>'
        )

    def add_image(self, path: str | Path, alt: str = "image", embed: bool = True) -> None:
        p = Path(path)
        if embed:
            src = file_to_data_uri(p)
        else:
            src = p.as_posix()
        self._blocks.append(f'<img src="{src}" alt="{esc(alt)}">')

    def html(self) -> str:
        sub = esc(self.subtitle) if self.subtitle else ""
        blocks = "\n".join(self._blocks)
        return f"""<!doctype html>
<html lang=\"en\">
<head>
  <meta charset=\"utf-8\"/>
  <meta name=\"viewport\" content=\"width=device-width,initial-scale=1\"/>
  <title>{esc(self.title)}</title>
  <style>{self.css}</style>
</head>
<body>
  <div class=\"wrap\">
    <div class=\"header\">
      <h1 class=\"title\">{esc(self.title)}</h1>
      <div class=\"sub\">{sub}</div>
    </div>
    <div class=\"panel\"><div class=\"panelInner\">{blocks}</div></div>
    <div class=\"footer\">generated by reportkit-html</div>
  </div>
</body>
</html>"""

    def write(self, path: str | Path) -> Path:
        out = Path(path)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(self.html(), encoding="utf-8")
        return out
