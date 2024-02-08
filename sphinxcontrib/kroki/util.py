import re
from pathlib import Path
from typing import Tuple, List

from sphinx.util import logging

logger = logging.getLogger(__name__)


def process_structurizr_includes(
    contents: str, path: Path
) -> Tuple[str, List[Path]]:
    """Reads the input file and preprocesses any includes, returning the resulting file contents and dependencies."""
    dependencies: List[Path] = []
    lines = contents.split("\n")
    for i, line in enumerate(lines):
        match = re.match(r"^\s*!include\s+\"([^\"]+)\"\s*$", line)
        if match:
            include_path = path.parent / match.group(1)
            if not include_path.exists():
                raise FileNotFoundError(
                    f"Include file {include_path} not found, included from {include_path}:{i}"
                )

            dependencies.append(include_path)
            with open(include_path, "r") as f:
                include_contents = f.read()

            (include_contents, new_dependencies) = (
                process_structurizr_includes(include_contents, include_path)
            )
            lines[i] = include_contents
            dependencies.extend(new_dependencies)

    return ("\n".join(lines), dependencies)
