"""test_kroki
~~~~~~~~~~~~~~~~
Test the kroki extension.
"""

import re

import pytest
from sphinx.application import Sphinx
from sphinx.testing.path import path


def get_content(app: Sphinx) -> str:
    app.builder.build_all()

    index = app.outdir / "index.html"  # type: ignore[operator]
    return index.read_text() if "read_text" in path.__dict__ else index.text()  # type: ignore[no-any-return]


@pytest.mark.sphinx(
    "html",
    testroot="kroki",
    confoverrides={"master_doc": "index"},
)
def test_kroki_html(app: Sphinx) -> None:
    content = get_content(app)
    html = (
        r'figure[^>]*?(?:kroki kroki-plantuml align-default)?" .*?>\s*'
        r'<img alt="bar -&gt; baz" class="kroki kroki-plantuml" .+?/>.*?'
        r'<span class="caption-text">caption of diagram</span>.*?</p>'
    )
    assert re.search(html, content, re.S)

    html = (
        r'<p>Hello <img alt="bar -&gt; baz" class="kroki kroki-plantuml" .*?/>'
        r" kroki world</p>"
    )
    assert re.search(html, content, re.S)

    html = r'<img .+?class="kroki kroki-mermaid graph" .+?/>'
    assert re.search(html, content, re.S)

    html = r'<img .+?class="kroki kroki-graphviz" .*?/>'
    assert re.search(html, content, re.S)

    html = (
        r'figure[^>]*?kroki kroki-plantuml align-center" .*?>\s*?'
        r'<img alt="foo -&gt; bar ".*?/>.*?'
        r'<span class="caption-text">on <em>center</em></span>'
    )
    assert re.search(html, content, re.S)

    html = r'<img.*?class="kroki kroki-ditaa align-right".*?/>'
    assert re.search(html, content, re.S)
