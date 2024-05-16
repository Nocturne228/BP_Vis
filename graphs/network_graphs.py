import pandas as pd
import networkx as nx
import copy
import dash_cytoscape as cyto
from dash import callback, Input, Output, State
from data.data_df import nodes_df, edges_df, core_node, key_link
from utils.data_process import get_node_label
from utils.color_palette import adjust_brightness, label_colors, edge_colors, dark_label_colors

core_ids = set(core_node['id'])

g = nx.Graph()
for i, row in nodes_df.iterrows():
    g.add_node(row['id'], label=row['type'], name=row['name'], industry=row['industry'])
for i, row in edges_df.iterrows():
    g.add_edge(row['source'], row['target'], label=row['relation'])

# pos = nx.spring_layout(g)

base_elements = []
dark_elements = []
# 添加节点到元素列表，并使用计算的位置信息
for node_id, node_attrs in g.nodes(data=True):
    node_color = label_colors.get(node_attrs['label'], '#FFFFFF')  # 默认为白色
    dark_node_color = dark_label_colors.get(node_attrs['label'], '#000000')
    base_elements.append({
        'data': {
            'id': node_id, 'label': node_attrs['label'], 'label_color': node_color,
            'name': node_attrs['name'], 'industry': node_attrs['industry']
        },
        # 'position': {'x': pos[node_id][0] * 500, 'y': pos[node_id][1] * 500}
    })
    if node_id in core_ids:
        dark_elements.append({
            'data': {
                'id': node_id,
                'label': node_attrs['label'],
                'label_color': node_color,
                'name': node_attrs['name'],
                'industry': node_attrs['industry']
            },
            # 'position': {'x': pos[node_id][0] * 500, 'y': pos[node_id][1] * 500}
        })
    else:
        dark_elements.append({
            'data': {
                'id': node_id,
                'label': node_attrs['label'],
                'label_color': dark_node_color,
                'name': node_attrs['name'],
                'industry': node_attrs['industry']
            },
            # 'position': {'x': pos[node_id][0] * 500, 'y': pos[node_id][1] * 500}
        })

# 添加边到元素列表
for u, v, data in g.edges(data=True):
    edge_color = edge_colors.get(data['label'], '#FFFFFF')
    base_elements.append({
        'data': {'source': u, 'target': v, 'label': data['label'], 'label_color': edge_color}
    })

initial_elements = base_elements

base_cyto_graph = cyto.Cytoscape(
    id='base-cyto-graph',
    layout={'name': 'cose'},
    style={'width': '500px', 'height': '600px'},
    elements=initial_elements,
    stylesheet=[
        {
            'selector': 'node',
            'style': {
                'background-color': 'data(label_color)',
                'width': 10,  # 设置节点宽度
                'height': 10,  # 设置节点高度
                'border-width': 1,  # 边缘宽度
                'border-color': 'data(border_color)',  # 边缘颜色
            }
        },
        {
            'selector': 'edge',
            'style': {
                'line-color': 'data(label_color)',
                'width': 1,
            }
        }
    ],
)
