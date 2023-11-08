from os.path import relpath
from pathlib import Path
from typing import Any

from docutils.nodes import SkipNode, image
from sphinx.locale import __
from sphinx.transforms import SphinxTransform

from .kroki import KrokiError, kroki, render_kroki
from .util import logger


class KrokiToImageTransform(SphinxTransform):
    default_priority = 10

    def apply(self, **_kwargs: Any) -> None:
        source = Path(self.document["source"]).parent
        for node in self.document.traverse(kroki):
            img = image()
            img["kroki"] = node
            img["alt"] = node["source"]
            if "align" in node:
                img["align"] = node["align"]
            if "class" in node:
                img["class"] = node["class"]

            out = self.render(node)
            img["uri"] = relpath(out, source)

            node.replace_self(img)

    def output_format(self, node: kroki) -> str:
        builder = self.app.builder

        return node.get("format", builder.config.kroki_output_format)  # type: ignore[no-any-return]

    def render(self, node: kroki, prefix: str = "kroki") -> Path:
        builder = self.app.builder
        output_format = self.output_format(node)
        diagram_type = node["type"]
        diagram_source = node["source"]
        diagram_options = node.get("options", {})

        try:
            out = render_kroki(
                builder,
                diagram_type,
                diagram_source,
                output_format,
                diagram_options,
                prefix,
            )
        except KrokiError as exc:
            logger.warning(
                __("kroki %s diagram (%s) with source %r: %s"),
                diagram_type,
                output_format,
                diagram_source,
                exc,
            )
            raise SkipNode from exc

        return out
