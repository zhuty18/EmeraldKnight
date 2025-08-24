"""
绘制设计图
"""

import json

import pydot

graph = pydot.Dot("graph", graph_type="digraph")
with open("data/scenes.json", "r", encoding="utf-8") as f:
    scenes = json.load(f)

with open("data/choices.json", "r", encoding="utf-8") as f:
    choices = json.load(f)

choice_map = {}
for c in choices:
    choice_map[c["id"]] = c


for s in scenes:
    graph.add_node(pydot.Node(s["id"]))
    for o in s["options"]:
        graph.add_edge(pydot.Edge(s["id"], choice_map[o]["target"]))

graph.write("1.png", format="png")
