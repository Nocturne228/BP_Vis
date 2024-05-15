import pandas as pd
import networkx as nx
import copy
import dash_cytoscape as cyto
from data.data_df import nodes_df, edges_df, core_node, key_link
from utils.color_palette import adjust_brightness, label_colors, edge_colors

core_ids = set(core_node['id'])


def create_network_graph():
    g = nx.Graph()
    for i, row in nodes_df.iterrows():
        g.add_node(row['id'], label=row['type'])
    for i, row in edges_df.iterrows():
        g.add_edge(row['source'], row['target'], label=row['relation'])

    pos = nx.spring_layout(g)

    base_elements = []
    # 添加节点到元素列表，并使用计算的位置信息
    for node_id, node_attrs in g.nodes(data=True):
        node_color = label_colors.get(node_attrs['label'], '#FFFFFF')  # 默认为白色
        base_elements.append({
            'data': {'id': node_id, 'label': node_attrs['label'], 'label_color': node_color},
            'position': {'x': pos[node_id][0] * 500, 'y': pos[node_id][1] * 500}
        })

    # 添加边到元素列表
    for u, v, data in g.edges(data=True):
        edge_color = edge_colors.get(data['label'], '#FFFFFF')
        base_elements.append({
            'data': {'source': u, 'target': v, 'label': data['label'], 'label_color': edge_color}
        })

    cyto_graph = cyto.Cytoscape(
        id='base-cyto-graph',
        layout={'name': 'preset'},
        style={'width': '100%', 'height': '600px'},
        elements=base_elements,
        stylesheet=[
            {
                'selector': 'node',
                'style': {
                    'background-color': 'data(label_color)',
                    'width': 10,  # 设置节点宽度
                    'height': 10  # 设置节点高度
                }
            },
            {
                'selector': 'edge',
                'style': {
                    'line-color': 'data(label_color)',
                    'width': 1
                }
            }
        ],
    )

    return cyto_graph, base_elements


base_cyto_graph, base_elements = create_network_graph()

# 核心节点ID集合

# 更新elements，对核心节点进行高亮，其他节点变暗
# for element in temp_elements:
#     if 'id' in element['data']:  # 检查是否是节点
#         if element['data']['id'] not in core_ids:
#             element['data']['label_color'] = adjust_brightness(element['data']['label_color'], 0.4)
#         else:
#             continue
#
# new_elements = temp_elements
