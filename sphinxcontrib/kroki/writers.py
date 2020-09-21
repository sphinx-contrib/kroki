from typing import Dict

from docutils import nodes

from .util import logger
from .kroki import kroki, render_kroki, KrokiError
from sphinx.locale import __
from sphinx.writers.html import HTMLTranslator


def render_html(
    self: HTMLTranslator,
    node: kroki,
    diagram_type: str,
    diagram_source: str,
    options: Dict,
    prefix: str = "kroki",
    kroki_class: str = None,
) -> None:
    output_format: str = node.get(
        "format", self.builder.config.kroki_output_format
    )

    try:
        fname, outfn = render_kroki(
            self.builder, diagram_type, diagram_source, output_format, prefix
        )
    except KrokiError as exc:
        logger.warning(
            __("kroki %s diagram (%s) with code %r: %s"),
            diagram_type,
            output_format,
            diagram_source,
            exc,
        )
        raise nodes.SkipNode from exc

    classes = [kroki_class, "kroki", "kroki-" + diagram_type] + node.get(
        "classes", []
    )

    if fname is None:
        self.body.append(self.encode(diagram_source))
    else:
        self.body.append('<div class="%s">' % " ".join(filter(None, classes)))
        if "align" in node:
            self.body.append(
                '<div align="%s" class="align-%s">'
                % (node["align"], node["align"])
            )
        if output_format == "svg" and self.builder.config.kroki_inline_svg:
            with open(outfn, "r") as f:
                self.body.append("%s" % f.read())
        else:
            self.body.append(
                '<a href="%s"><img src="%s" alt="%s" /></a>'
                % (
                    fname,
                    fname,
                    self.encode(
                        options.get("caption", diagram_source)
                    ).strip(),
                )
            )
        if "align" in node:
            self.body.append("</div>\n")
        self.body.append("</div>\n")

    raise nodes.SkipNode


def html_visit_kroki(self: HTMLTranslator, node: kroki) -> None:
    render_html(self, node, node["type"], node["code"], node["options"])
