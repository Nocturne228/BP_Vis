import pandas as pd
import networkx as nx
import dash_bootstrap_components as dbc
import dash_cytoscape as cyto
from dash import Dash

from utils.color_palette import label_colors, dark_label_colors, edge_colors

nodes_df = pd.read_csv('data/team1/node.csv')
edges_df = pd.read_csv('data/team1/link.csv')

g = nx.Graph()
for i, row in nodes_df.iterrows():
    g.add_node(row['id'], label=row['type'], name=row['name'], industry=row['industry'])
for i, row in edges_df.iterrows():
    g.add_edge(row['source'], row['target'], label=row['relation'])

base_elements = []
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

# 添加边到元素列表
for u, v, data in g.edges(data=True):
    edge_color = edge_colors.get(data['label'], '#FFFFFF')
    base_elements.append({
        'data': {'source': u, 'target': v, 'label': data['label'], 'label_color': edge_color}
    })

base_cyto_graph = cyto.Cytoscape(
    id='base-cyto-graph',
    layout={'name': 'cose'},
    style={'width': '600px', 'height': '600px'},
    elements=base_elements,
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


body = dbc.Container(
    dbc.Row(
        base_cyto_graph
    )
)

app = Dash(external_stylesheets=[dbc.themes.VAPOR])
app.layout = body

if __name__ == '__main__':
    app.run(debug=True)

