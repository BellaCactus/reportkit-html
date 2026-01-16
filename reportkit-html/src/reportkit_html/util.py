from __future__ import annotations

import base64
import html
import mimetypes
from pathlib import Path


def esc(s: object) -> str:
    """HTML-escape anything."""
    return html.escape(str(s), quote=True)


def guess_mime(path: str | Path) -> str:
    mt, _ = mimetypes.guess_type(str(path))
    return mt or "application/octet-stream"


def file_to_data_uri(path: str | Path) -> str:
    """Return data: URI for a file."""
    p = Path(path)
    data = p.read_bytes()
    b64 = base64.b64encode(data).decode("ascii")
    mime = guess_mime(p)
    return f"data:{mime};base64,{b64}"
