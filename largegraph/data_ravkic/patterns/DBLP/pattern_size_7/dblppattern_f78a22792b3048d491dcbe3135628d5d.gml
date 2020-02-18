graph [
  name "/data/leuven/311/vsc31168/MARTIN_EXPERIMENTS/PATTERNS/PATTERNS_DBLP/PATTERNS_400_BATCH/patterns_size_6/batch1/dblppattern_ea46e2b9ea6344f9937cbb4724551762/dblppattern_ea46e2b9ea6344f9937cbb4724551762.gml"
  node [
    id 0
    label "citations"
    predicate "citations"
    target 1
    valueinpattern 0
    type "None"
  ]
  node [
    id 1
    label "constant:paper"
    predicate "constant"
    target 0
    valueinpattern 0
    type "None"
  ]
  node [
    id 2
    label "coauthored"
    predicate "coauthored"
    target 0
    valueinpattern 0
    type "None"
  ]
  node [
    id 3
    label "constant:paper"
    predicate "constant"
    target 0
    valueinpattern 0
    type "None"
  ]
  node [
    id 4
    label "citations = high"
    predicate "citations"
    target 0
    valueinpattern 1
    type "None"
    value "high"
  ]
  node [
    id 5
    label "references"
    predicate "references"
    target 0
    valueinpattern 0
    type "None"
  ]
  node [
    id 6
    label "references"
    predicate "references"
    target 0
    valueinpattern 0
    type "None"
  ]
  edge [
    source 0
    target 1
  ]
  edge [
    source 1
    target 2
  ]
  edge [
    source 1
    target 5
  ]
  edge [
    source 2
    target 3
  ]
  edge [
    source 3
    target 4
  ]
  edge [
    source 3
    target 6
  ]
]