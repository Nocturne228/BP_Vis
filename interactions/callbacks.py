import copy
import pandas as pd
from dash import Input, Output, State, callback
from graphs.network_graphs import base_elements, dark_elements, core_ids, key_link
from utils.data_process import get_node_label
from utils.color_palette import adjust_brightness, dark_label_colors, label_colors


@callback(Output('cytoscape-tapNodeData-output', 'children'),
          Input('base-cyto-graph', 'tapNodeData'))
def display_tap_node_data(data):
    if data:
        return data['label']


@callback(Output('cytoscape-tapEdgeData-output', 'children'),
          Input('base-cyto-graph', 'tapEdgeData'))
def display_tap_edge_data(data):
    if data:
        return "Edge: " + data['label']


@callback(
    Output("base-cyto-graph", "elements"),
    [
        Input("radios-button-group", "value"),
        State("base-cyto-graph", "elements")
    ]
)
def display_value(value, old_elements):
    if value == 1:
        for element in old_elements:
            if 'id' in element['data']:
                if element['data']['label_color'] == dark_label_colors.get(element['data']['label'], '#000000'):
                    element['data']['label_color'] = label_colors.get(element['data']['label'], '#FFFFFF')

            if 'source' in element['data'] and 'target' in element['data']:
                edge_color_type = get_node_label(element['data']['target'])
                edge_label_color = label_colors.get(edge_color_type, '#FFFFFF')
                element['data']['label_color'] = edge_label_color
    elif value == 2:
        for element in old_elements:
            if 'source' in element['data'] and 'target' in element['data']:
                flag = True
                for index, row in key_link.iterrows():
                    source = row['source']
                    target = row['target']

                    if element['data']['source'] == source and element['data']['target'] == target:
                        element['data']['label_color'] = adjust_brightness(element['data']['label_color'], factor=2.0)
                        flag = False
                        continue

                if flag:
                    element['data']['label_color'] = dark_label_colors.get(
                        get_node_label(element['data']['target']), '#FFFFFF'
                    )
            else:
                nodes = list(set(key_link['source']) | set(key_link['target']))  # 获取所有节点
                if element['data']['id'] in nodes:
                    pass
                else:
                    element['data']['label_color'] = dark_label_colors.get(element['data']['label'], '#000000')

    else:
        for element in old_elements:
            if 'id' in element['data']:
                if element['data']['id'] not in core_ids:
                    element['data']['label_color'] = dark_label_colors.get(element['data']['label'], '#000000')

            if 'source' in element['data'] and 'target' in element['data']:
                edge_color_type = get_node_label(element['data']['target'])
                edge_label_color = dark_label_colors.get(edge_color_type, '#FFFFFF')
                element['data']['label_color'] = edge_label_color

    return old_elements

    # return f"Selected value: {value}"
