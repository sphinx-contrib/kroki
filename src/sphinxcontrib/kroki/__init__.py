"""sphinxcontrib.kroki.

Embed PlantUML, DOT, etc. diagrams in your documentation using Kroki.
:copyright: Copyright 2020 by Martin Hasoň <martin.hason@gmail.com>
:license: MIT, see LICENSE for details.
"""

from __future__ import annotations

from typing import Any

import pkg_resources
from sphinx.application import Sphinx

from .kroki import Kroki
from .transform import KrokiToImageTransform

__version__ = pkg_resources.get_distribution("sphinxcontrib-kroki").version


def setup(app: Sphinx) -> dict[str, Any]:
    app.add_directive("kroki", Kroki)
    app.add_transform(KrokiToImageTransform)
    app.add_config_value("kroki_url", "https://kroki.io", "env")
    app.add_config_value("kroki_output_format", "svg", "env")
    app.add_config_value("kroki_inline_svg", False, "env")

    return {"version": __version__, "parallel_read_safe": True}
