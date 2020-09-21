"""
    sphinxcontrib.kroki
    ~~~~~~~~~~~~~~~~~~~~~
    Embed PlantUML, DOT, etc. diagrams in your documentation using Kroki.
    :copyright: Copyright 2020 by Martin Hasoň <martin.hason@gmail.com>
    :license: MIT, see LICENSE for details.
"""

from typing import Any, Dict
from sphinx.application import Sphinx
from .kroki import kroki, Kroki
from .writers import html_visit_kroki
import pkg_resources

__version__ = pkg_resources.get_distribution("sphinxcontrib-kroki").version


def setup(app: Sphinx) -> Dict[str, Any]:
    app.add_node(kroki, html=(html_visit_kroki, None))
    app.add_directive("kroki", Kroki)
    app.add_config_value("kroki_url", "https://kroki.io", "env")
    app.add_config_value("kroki_output_format", "svg", "env")
    app.add_config_value("kroki_inline_svg", False, "env")

    return {"version": __version__, "parallel_read_safe": True}
