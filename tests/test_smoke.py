from reportkit_html import Report


def test_report_generates_html():
    r = Report(title="x")
    r.add_text("hi")
    html = r.html()
    assert "<!doctype html>" in html.lower()
    assert "hi" in html
