"""
    test_kroki
    ~~~~~~~~~~~~~~~~
    Test the kroki extension.
"""

import re
import pytest


@pytest.mark.sphinx('html', testroot='kroki')
def test_kroki_html(app, status, warning):
    app.builder.build_all()

    content = (app.outdir / 'index.html').read_text()

    html = (r'<div class="figure align-default" .*?>\s*'
            r'<div class="kroki kroki-plantuml"><a .+?><img .+?/></a>.*?'
            r'<p class="caption"><span class="caption-text">caption of diagram</span>.*</p>\s*</div>')
    assert re.search(html, content, re.S)

    html = r'<p>Hello <div class="kroki kroki-plantuml"><a .*?><img .*?/></a></div>\n kroki world'
    assert re.search(html, content, re.S)

    html = '<div class="kroki kroki-mermaid graph"><a href.+?<img .+?/></a></div>'
    assert re.search(html, content, re.S)

    html = (r'<div class="kroki kroki-graphviz">\s*'
            r'<a .*?><img .*?/></a></div>')
    assert re.search(html, content, re.S)

    html = (r'<div class="figure align-center" .*?>\s*?'
            r'<div class="kroki kroki-plantuml"><a .*?><img .*? alt="foo -&gt; bar" /></a></div>\s*?'
            r'<p class="caption"><span class="caption-text">on <em>center</em></span>')
    assert re.search(html, content, re.S)

    html = ('<div class="kroki kroki-ditaa"><div align="right" class="align-right">.*?'
            r'<a .*?><img .*?/></a></div>\s*?</div>')
    assert re.search(html, content, re.S)


@pytest.mark.sphinx('html', testroot='kroki', confoverrides={'kroki_inline_svg': True})
def test_kroki_html_inline_svg(app, status, warning):
    app.builder.build_all()

    content = (app.outdir / 'index.html').read_text()

    html = (r'<div class="figure align-default" .*?>\s*'
            r'<div class="kroki kroki-plantuml">.+?<svg.+?</svg>.*?'
            r'<p class="caption"><span class="caption-text">caption of diagram</span>.*</p>\s*</div>')
    assert re.search(html, content, re.S)

    html = r'<p>Hello <div class="kroki kroki-plantuml">.+?<svg .*?</svg></div>\n kroki world'
    assert re.search(html, content, re.S)

    html = '<div class="kroki kroki-mermaid graph"><svg id="mermaid.+?</svg></div>'
    assert re.search(html, content, re.S)

    html = (r'<div class="kroki kroki-graphviz">\s*'
            r'<a .*?><img .*?/></a></div>')
    assert re.search(html, content, re.S)

    html = (r'<div class="figure align-center" .*?>\s*?'
            r'<div class="kroki kroki-plantuml"><a .*?><img .*? alt="foo -&gt; bar" /></a></div>\s*?'
            r'<p class="caption"><span class="caption-text">on <em>center</em></span>')
    assert re.search(html, content, re.S)

    html = ('<div class="kroki kroki-ditaa"><div align="right" class="align-right">.*?'
            r'<svg .*?</svg></div>\s*?</div>')
    assert re.search(html, content, re.S)