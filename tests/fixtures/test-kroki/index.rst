kroki
=====

.. kroki::
   :type: plantuml
   :caption: caption of diagram

   bar -> baz

.. |diagram| kroki:: plantuml svg

           bar -> baz

Hello |diagram| kroki world

.. kroki:: svg
   :type: mermaid
   :class: graph

   graph TD
     A[ Anyone ]

.. kroki:: graphviz graph.dot png
   :options:
     layout: neato
     graph-attribute-label: My favorite graph
     node-attribute-shape: rect

.. kroki:: png diagram.puml
   :align: center
   :caption: on *center*

.. kroki:: diagram.ditaa
   :align: right
