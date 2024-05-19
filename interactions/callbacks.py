import dash_bootstrap_components as dbc
from dash import Input, Output, State, callback, html

from graphs.network_graphs import core_ids, key_link
from utils.data_process import get_node_label, industry_mapping, get_neighbors_with_edges
from utils.color_palette import adjust_brightness, dark_label_colors, label_colors


@callback(
    Output('cytoscape-tapNodeData-output', 'children'),
    [
        Input('base-cyto-graph', 'tapNodeData')
    ]
)
def display_tap_node_data(data):
    """
    Display information about a tapped node in a Dash Cytoscape graph.

    This callback function is triggered when a node in the Cytoscape graph is clicked (tapped).
    It displays the relevant information about the tapped node, formatted as a list of items,
    excluding certain keys and translating some key names for better readability.

    Parameters:
    data (dict): A dictionary containing data about the tapped node.
                 This dictionary is expected to have keys such as 'id', 'label', 'industry', and 'name'.
                 Keys 'label_color' and 'timeStamp' are ignored.

    Returns:
    list or str: A list of `dbc.ListGroupItem` elements displaying the node information,
                 or a string prompting the user to click a node if no data is provided.

    Example:
    If a node with the following data is clicked:
    {
        'id': 'Node_1',
        'label': 'Domain',
        'industry': ['industry_code_1', 'industry_code_2'],
        'name': 'example.com',
        'label_color': '#636EFA',
        'timeStamp': 1615877931163
    }
    The function might return:
    [
        dbc.ListGroupItem(html.Strong('id: Node_1'), class_name='transparent-list-group-item'),
        dbc.ListGroupItem(html.Strong('类型: Domain'), class_name='transparent-list-group-item'),
        dbc.ListGroupItem(html.Strong('产业: Industry Description 1, Industry Description 2'), class_name='transparent-list-group-item'),
        dbc.ListGroupItem(html.Strong('名称: example.com'), class_name='transparent-list-group-item')
    ]

    Note:
    - The 'industry' field in the data dictionary is expected to be a list of industry codes.
      These codes are mapped to their descriptions using an `industry_mapping` dictionary.
    - If the 'industry' field is empty or none of the codes are found in `industry_mapping`,
      the function returns "无相关黑灰产业" (No relevant black-gray industry).

    """
    keys_to_skip = {'label_color', 'timeStamp'}
    keys_dict = {
        'id': 'id',
        'label': '类型',
        'industry': '产业',
        'name': '名称',
    }
    if data:
        industry_description = ', '.join(
            [industry_mapping[code] for code in data.get('industry', []) if code in industry_mapping])
        if industry_description == '':
            industry_description = "无相关黑灰产业"
        data['industry'] = industry_description

        return [dbc.ListGroupItem(html.Strong(
            f"{keys_dict.get(key)}: {value}"), class_name='transparent-list-group-item'
        ) for key, value in data.items() if key not in keys_to_skip]
    return "点击查看资产节点信息"


# @callback(
#     Output('base-cyto-graph', 'elements'),
#     [
#         Input('base-cyto-graph', 'tapEdgeData'),
#         Input('input-jumps', 'value'),
#         State('base-cyto-graph', 'elements')
#     ],
# )
# def display_tap_node_graph(node, jumps, old_elements):
#     node_list, edge_list = get_neighbors_with_edges(old_elements, node['id'], jumps)
#     print(node_list)
#     return old_elements


@callback(
    Output('cytoscape-tapEdgeData-output', 'children'),
    Input('base-cyto-graph', 'tapEdgeData')
)
def display_tap_edge_data(data):
    """
    Display information about a tapped edge in a Dash Cytoscape graph.

    This callback function is triggered when an edge in the Cytoscape graph is clicked (tapped).
    It displays the relevant information about the tapped edge, formatted as a list of items,
    excluding certain keys and translating some key names for better readability.

    Parameters:
    data (dict): A dictionary containing data about the tapped edge.
                 This dictionary is expected to have keys such as 'source', 'target', and 'label'.
                 Keys 'id', 'label_color', and 'timeStamp' are ignored.

    Returns:
    list or str: A list of `dbc.ListGroupItem` elements displaying the edge information,
                 or a string prompting the user to click an edge if no data is provided.

    Example:
    If an edge with the following data is clicked:
    {
        'source': 'Node_1',
        'target': 'Node_2',
        'label': 'r_cert_chain',
        'id': 'Edge_1',
        'label_color': '#19D3F3',
        'timeStamp': 1615877931163
    }
    The function might return:
    [
        dbc.ListGroupItem(html.Strong('起点: Node_1'), class_name='transparent-list-group-item'),
        dbc.ListGroupItem(html.Strong('终点: Node_2'), class_name='transparent-list-group-item'),
        dbc.ListGroupItem(html.Strong('类型: r_cert_chain'), class_name='transparent-list-group-item')
    ]

    Note:
    - The function translates the keys 'source', 'target', and 'label' to '起点' (start point),
      '终点' (end point), and '类型' (type) respectively.
    - The keys 'id', 'label_color', and 'timeStamp' are skipped and not displayed.

    """
    keys_to_skip = {'id', 'label_color', 'timeStamp'}
    keys_dict = {
        'source': '起点',
        'target': '终点',
        'label': '类型'
    }
    if data:
        return [dbc.ListGroupItem(html.Strong(
            f"{keys_dict.get(key)}: {value}"), class_name='transparent-list-group-item'
        ) for key, value in data.items() if key not in keys_to_skip]
    return "点击查看资产链路信息"


@callback(
    Output("base-cyto-graph", "elements"),
    [
        Input("radios-button-group", "value"),
        State("base-cyto-graph", "elements")
    ]
)
def display_graph_info(value, old_elements):
    """
    接收按钮值，控制图谱的信息展示，如关键链路和核心资产节点

    参数：按钮的值
    1->将所有点和边都设置回正常颜色
    2->显示关键链路
    3->显示核心资产
    """

    for element in old_elements:
        if 'id' in element['data']:
            if element['data']['label_color'] == dark_label_colors.get(element['data']['label'], '#000000'):
                element['data']['label_color'] = label_colors.get(element['data']['label'], '#FFFFFF')

        if 'source' in element['data'] and 'target' in element['data']:
            edge_color_type = get_node_label(element['data']['target'])
            edge_label_color = label_colors.get(edge_color_type, '#FFFFFF')
            element['data']['label_color'] = edge_label_color

    if value == 1:
        pass

    elif value == 2:
        for element in old_elements:
            if 'source' in element['data'] and 'target' in element['data']:
                element['data']['label_color'] = dark_label_colors.get(
                    get_node_label(element['data']['target']), '#FFFFFF'
                )
                for index, row in key_link.iterrows():
                    source = row['source']
                    target = row['target']

                    if element['data']['source'] == source and element['data']['target'] == target:
                        element['data']['label_color'] = adjust_brightness(element['data']['label_color'], factor=2.0)

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


@callback(Output("base-cyto-graph", 'layout'),
          Input('dropdown-update-layout', 'value'))
def update_layout(layout):
    return {
        'name': layout,
        'animate': True
    }


@callback(
    Output('check-node-subgraph-button', 'disabled'),
    Input('radios-button-group', 'value')
)
def toggle_button(radio_value):
    """
    Enable or disable the 'Random name' button based on the selected radio button value.

    Parameters:
    radio_value (str): The value of the selected radio button, either 'enable' or 'disable'.

    Returns:
    bool: True if the button should be disabled, False otherwise.
    """
    if radio_value != 1:
        return True
    else:
        return False
