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

- `:align:` The horizontal alignment of the diagram (left, center or right);
- `:caption:` The caption of the diagram;
- `:class:` The class names (a list of class names separeted by spaces);
- `:filename:` The path to the file with the diagram;
- `:format:` The output format of the diagram (default svg);
- `:name:` The hyperlink reference to the element;
- `:options:`: The [diagram options](https://docs.kroki.io/kroki/setup/diagram-options/) in yaml format;
- `:type:` The type of the diagram (actdiag, blockdiag, bpmn, bytefield,
  c4plantuml, dot, ditaa, er, erd, excalidraw, graphviz, mermaid, nomnoml,
  nwdiag, packetdiag, pikchr, plantuml, rackdiag, structurizr, seqdiag,
  svgbob, umlet, vega, vegalite, wavedrom).

The diagram type can be automatically derived from the file extension (as same as `type`).
Additional supported extensions:

Extension  | Type
---------- | ----
*.bob      | svgbob
*.c4       | c4plantuml
*.c4puml   | c4plantuml
*.dot      | graphviz
*.dsl      | structurizr
*.er       | erd
*.gv       | graphviz
*.iuml     | plantuml
*.pu       | plantuml
*.puml     | plantuml
*.uxf      | umlet
*.vg       | vega
*.vgl      | vegalite
*.vl       | vegalite
*.wsd      | plantuml

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
