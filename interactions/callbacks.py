from dash import Input, Output, callback
import pandas as pd


@callback(Output('cytoscape-tapNodeData-output', 'children'),
          Input('cyto-network-graph', 'tapNodeData'))
def display_tap_node_data(data):
    if data:
        return "Node: " + data['label']


@callback(Output('cytoscape-tapEdgeData-output', 'children'),
          Input('cyto-network-graph', 'tapEdgeData'))
def display_tap_edge_data(data):
    if data:
        return "Edge: " + " -> "

# TODO 根据radio item的值显示不同的图像.
