#!/usr/bin/env python
#coding=utf-8

from pyecharts import Graph

def test_graph():

    # graph_0
    nodes = [{"name": "结点1", "symbolSize": 10},
             {"name": "结点2", "symbolSize": 20},
             {"name": "结点3", "symbolSize": 30},
             {"name": "结点4", "symbolSize": 40},
             {"name": "结点5", "symbolSize": 50},
             {"name": "结点6", "symbolSize": 40},
             {"name": "结点7", "symbolSize": 30},
             {"name": "结点8", "symbolSize": 20}]
    links = []
    for i in nodes:
        for j in nodes:
            links.append({"source": i.get('name'), "target": j.get('name')})
    graph = Graph("关系图-力引导布局示例")
    graph.add("", nodes, links, repulsion=8000)
    graph.show_config()
    graph.render()

    # graph_1
    graph = Graph("关系图-环形布局示例")
    graph.add("", nodes, links, is_label_show=True, repulsion=8000, layout='circular', label_text_color=None)
    graph.show_config()
    graph.render()

    # graph_2
    import json
    with open("..\json\weibo.json", "r", encoding="utf-8") as f:
        j = json.load(f)
        nodes, links, categories, cont, mid, userl = j
    graph = Graph("微博转发关系图", width=1200, height=600)
    graph.add("", nodes, links, categories, label_pos="right", repulsion=50, is_legend_show=False, line_curve=0.2,
              label_text_color=None)
    graph.show_config()
    graph.render()