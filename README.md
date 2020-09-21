sphinxcontrib-kroki
===================

Embed PlantUML, DOT, etc. diagrams in your Sphinx-based documentation using
[kroki](https://kroki.io/).

Instalation
-----------

Install this package via pip:

```shell script
pip install sphinxcontrib-kroki
```

and enable in project configuration (`conf.py`):

```python
extensions = [
    'sphinxcontrib.kroki',
]
```

Usage
-----

Inline diagram, show as svg:

```rest
.. kroki::
   :caption: Diagram

    @startuml
    Alice -> Bob: Authentication Request
    Bob --> Alice: Authentication Response

    Alice -> Bob: Another authentication Request
    Alice <-- Bob: Another authentication Response
    @enduml
```

Load a diagram from a file and show as png:

```rest
.. kroki:: ./path/to/graph.puml png
```

### Options

- `:align:` The horizontal alignment of the diagram (left, center or right).
- `:caption:` The caption of the diagram.
- `:class:` The class names (a list of class names separeted by spaces).
- `:filename:` The path to the file with the diagram.
- `:format:` The output format of the diagram (default svg).
- `:type:` The type of the diagram (blockdiag, bpmn, bytefield, seqdiag,
  actdiag, nwdiag, packetdiag, rackdiag, c4plantuml, ditaa, erd, graphviz, mermaid,
  nomnoml, plantuml, svgbob, vega, vegalite, wavedrom)

The diagram type can be automatically derived from the file extension:

Extension  | Type
---------- | ----
*.dot      | graphviz
*.gv       | graphviz
*.bpmn     | bpmn
*.puml     | plantuml
*.ditaa    | ditaa

Configuration
-------------

- `kroki_url` (default https://kroki.io).
- `kroki_output_format` (default svg).
- `kroki_inline_svg` (dafault False).

Alternatives
------------

- https://github.com/sphinx-contrib/plantuml
- https://github.com/sphinx-contrib/gravizo
- https://github.com/j-martin/sphinx-diagrams
