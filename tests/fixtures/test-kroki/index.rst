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

.. kroki:: png diagram.puml
   :align: center
   :caption: on *center*

.. kroki:: diagram.ditaa
   :align: right
