from typing import Any
from pathlib import Path
from os.path import relpath, dirname
from docutils.nodes import image, SkipNode

from .util import logger
from .kroki import kroki, render_kroki, KrokiError
from sphinx.transforms import SphinxTransform
from sphinx.locale import __


class KrokiToImageTransform(SphinxTransform):
    default_priority = 10

    def apply(self, **kwargs: Any) -> None:
        source = dirname(self.document["source"])
        for node in self.document.traverse(kroki):
            img = image()
            img["kroki"] = node
            img["alt"] = node["code"]
            if "align" in node:
                img["align"] = node["align"]
            if "class" in node:
                img["class"] = node["class"]

            out = self.render(node)
            img["uri"] = relpath(out, source)

            node.replace_self(img)

    def output_format(self, node: kroki) -> str:
        builder = self.app.builder

        return node.get("format", builder.config.kroki_output_format)

    def render(self, node: kroki, prefix: str = "kroki") -> Path:
        builder = self.app.builder
        output_format = self.output_format(node)
        diagram_type = node["type"]
        diagram_source = node["code"]

        try:
            out = render_kroki(
                builder, diagram_type, diagram_source, output_format, prefix
            )
        except KrokiError as exc:
            logger.warning(
                __("kroki %s diagram (%s) with code %r: %s"),
                diagram_type,
                output_format,
                diagram_source,
                exc,
            )
            raise SkipNode from exc

        return out
