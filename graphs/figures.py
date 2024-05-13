import pandas as pd
import networkx as nx
import numpy as np
import dash_cytoscape as cyto
import plotly.express as px
import plotly.graph_objects as go

col_swatch = px.colors.qualitative.Light24



class NetworkGraph:
    def __init__(self, number):
        self.nodes_df, self.edges_df = self.load_data(number)
        self.G = self.create_graph()
        self.label_colors = {
            'Domain': '#636EFA',
            'Whois_Phone': '#EF553B',
            'Whois_EMail': '#00CC96',
            'Whois_Name': '#AB63FA',
            'IP': '#FFA15A',
            'Cert': '#19D3F3',
            'ASP': '#FF6692'
        }

    def load_data(self, number):
        nodes_df = pd.read_csv(f'data/team{number}/Node.csv')
        edges_df = pd.read_csv(f'data/team{number}/Link.csv')
        return nodes_df, edges_df

    def create_graph(self):
        G = nx.Graph()
        for i, row in self.nodes_df.iterrows():
            G.add_node(row['id'], label=row['type'])
        for i, row in self.edges_df.iterrows():
            G.add_edge(row['source'], row['target'])
        return G

    def plot_network_graph(self):
        pos = nx.spring_layout(self.G)
        node_positions = {node: pos[node] for node in self.G.nodes()}

        fig = px.scatter(x=[pos[x][0] for x in self.G.nodes()],
                         y=[pos[x][1] for x in self.G.nodes()],
                         color=[self.nodes_df.loc[self.nodes_df['id'] == x, 'type'].iloc[0] for x in self.G.nodes()],
                         labels={'text': 'Node'},
                         title='Force-Directed Network Graph')

        for edge in self.G.edges():
            fig.add_scatter(x=[pos[edge[0]][0], pos[edge[1]][0], None],
                            y=[pos[edge[0]][1], pos[edge[1]][1], None],
                            mode='lines',
                            line=dict(color='blue', width=0.1))

        fig.update_traces(marker=dict(size=8))
        return fig

    def cyto_graph_plot(self):
        # 使用 NetworkX 的布局算法计算节点位置
        pos = nx.spring_layout(self.G)

        # 创建 cytoscape 元素列表
        elements = []

        # 添加节点到元素列表，并使用计算的位置信息
        for node_id, node_attrs in self.G.nodes(data=True):
            node_color = self.label_colors.get(node_attrs['label'], '#000')  # 默认为黑色
            elements.append({
                'data': {'id': node_id, 'label': node_attrs['label'], 'label_color': node_color},
                'position': {'x': pos[node_id][0] * 500, 'y': pos[node_id][1] * 500}
            })

        # 添加边到元素列表
        for u, v in self.G.edges():
            elements.append({
                'data': {'source': u, 'target': v}
            })

        # 创建 cytoscape 组件
        cyto_graph = cyto.Cytoscape(
            id='cytoscape-two-nodes',
            layout={'name': 'preset'},
            style={'width': '100%', 'height': '400px'},
            elements=elements,
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
                        'line-color': 'blue',
                        'width': 0.1
                    }
                }
            ]
        )

        return cyto_graph


if __name__ == '__main__':
    network = NetworkGraph(number=1)
    fig = network.plot_network_graph()
