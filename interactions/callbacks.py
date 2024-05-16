import copy
from utils.color_palette import adjust_brightness
from dash import Input, Output, State, callback
from graphs.network_graphs import base_elements, dark_elements, core_ids, key_link
from utils.data_process import get_node_label
import pandas as pd


@callback(Output('cytoscape-tapNodeData-output', 'children'),
          Input('base-cyto-graph', 'tapNodeData'))
def display_tap_node_data(data):
    if data:
        return "Node: " + data['label']


@callback(Output('cytoscape-tapEdgeData-output', 'children'),
          Input('base-cyto-graph', 'tapEdgeData'))
def display_tap_edge_data(data):
    if data:
        return "Edge: " + data['label']


@callback(
    Output('radio-item-output', 'children'),
    Input('radio-items-input', 'value'),
)
def radio_item_output(value):
    return value


# @callback(
#     Output('base-cyto-graph', 'elements'),
#     [Input('radio-item-output', 'children')],  # Assuming it's a radio item, use 'value' not 'children'
#     [State('base-cyto-graph', 'elements')]
# )
# def update_network_graph(radio_item_value, old_elements):
#     # Ensure this is defined or passed appropriately
#     # print(type(radio_item_value), type(old_elements))
#     if radio_item_value == 1:  # Assuming '1' is a string or adjust based on actual value type
#         for element in old_elements:
#             if 'id' in element['data']:  # Checking if it is a node
#                 if element['data']['id'] in core_ids:
#                     # print("核心")
#                     # Assuming adjust_brightness is a defined function that adjusts the color
#                     element['data']['label_color'] = adjust_brightness(element['data']['label_color'], factor=2.0)
#                 else:
#                     # print("非核心")
#                     element['data']['label_color'] = adjust_brightness(element['data']['label_color'], factor=0.5)
#
#     elif radio_item_value == 2:
#         for element in old_elements:
#             if 'source' in element['data'] and 'target' in element['data']:
#                 flag = True
#                 for index, row in key_link.iterrows():
#                     source = row['source']
#                     target = row['target']
#
#                     if element['data']['source'] == source and element['data']['target'] == target:
#                         element['data']['label_color'] = adjust_brightness(element['data']['label_color'], factor=2.0)
#                         flag = False
#                         continue
#
#                 if flag:
#                     element['data']['label_color'] = adjust_brightness(element['data']['label_color'], factor=0.2)
#             else:
#                 nodes = list(set(key_link['source']) | set(key_link['target']))  # 获取所有节点
#                 if element['data']['id'] in nodes:
#                     element['data']['label_color'] = adjust_brightness(element['data']['label_color'], factor=2.0)
#                 else:
#                     element['data']['label_color'] = adjust_brightness(element['data']['label_color'], factor=0.2)
#
#     else:
#         pass
#     return old_elements

