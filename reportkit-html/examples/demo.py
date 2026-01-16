from __future__ import annotations

from pathlib import Path

from reportkit_html import Report


def main() -> None:
    out_dir = Path(__file__).resolve().parent / "out"

    r = Report(title="reportkit-html demo", subtitle="static html report • no backend • pink mode")
    r.add_badge("status: online")
    r.add_h1("hello")
    r.add_text("this is a tiny html report generator.\nships as one file.")

    r.add_h2("kv")
    r.add_kv([
        ("timezone", "Pacific/Auckland"),
        ("build", "0.1.0"),
        ("mood", "sleepy"),
    ])

    r.add_h2("table")
    r.add_table(headers=["name", "power"], rows=[
        ["twi", "teleport"],
        ["trixie", "theatrics"],
        ["you", "stubbornness"],
    ])

    r.add_h2("code")
    r.add_code("""def hello():\n    return 'hi :3'\n""")

    r.add_hr()
    r.add_text("done. open the html in a browser.")

    out_path = r.write(out_dir / "report.html")
    print(f"wrote: {out_path}")


if __name__ == "__main__":
    main()
