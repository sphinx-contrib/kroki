from typing import Tuple, Any
from pathlib import Path
from docutils.nodes import image, SkipNode

from .util import logger
from .kroki import kroki, render_kroki, KrokiError
from sphinx.transforms import SphinxTransform
from sphinx.transforms.post_transforms import SphinxPostTransform
from sphinx.locale import __


class KrokiToImageTransform(SphinxTransform):
    default_priority = 10

    def apply(self, **kwargs: Any) -> None:
        for node in self.document.traverse(kroki):
            img = image()
            img["kroki"] = node
            img["alt"] = node["code"]
            if "align" in node:
                img["align"] = node["align"]
            if "class" in node:
                img["class"] = node["class"]

            rel, out = self.render(node)
            node["uri"] = str(rel)
            img["uri"] = "file://" + str(out)

            node.replace_self(img)

    def output_format(self, node: kroki) -> str:
        builder = self.app.builder

        return node.get("format", builder.config.kroki_output_format)

    def render(self, node: kroki, prefix: str = "kroki") -> Tuple[Path, Path]:
        builder = self.app.builder
        output_format = self.output_format(node)
        diagram_type = node["type"]
        diagram_source = node["code"]

        try:
            rel, out = render_kroki(
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

        return rel, out


class FixKrokiImagePathTransform(SphinxPostTransform):
    default_priority = 10

    def run(self, **kwargs: Any) -> None:
        for node in self.document.traverse(image):
            if "kroki" not in node or "uri" not in node["kroki"]:
                continue

            node["uri"] = node["kroki"]["uri"]
