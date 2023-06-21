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

.. kroki::
   :type: d2

   # Actors
   hans: Hans Niemann

   defendants: {
      mc: Magnus Carlsen
      playmagnus: Play Magnus Group
      chesscom: Chess.com
      naka: Hikaru Nakamura

      mc -> playmagnus: Owns majority
      playmagnus <-> chesscom: Merger talks
      chesscom -> naka: Sponsoring
   }

   # Accusations
   hans -> defendants: 'sueing for $100M'

   # Claim
   defendants.naka -> hans: Accused of cheating on his stream
   defendants.mc -> hans: Lost then withdrew with accusations
   defendants.chesscom -> hans: 72 page report of cheating
