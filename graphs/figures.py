import pandas as pd
import networkx as nx
import numpy as np
import dash_cytoscape as cyto
from dash import callback, Input, Output
import plotly.express as px
import plotly.graph_objects as go
from utils.color_palette import label_colors

col_swatch = px.colors.qualitative.Light24

numbers = 1
nodes_df = pd.read_csv(f'data/team{numbers}/node.csv')
edges_df = pd.read_csv(f'data/team{numbers}/link.csv')
core_node = pd.read_csv(f'data/team{numbers}/核心资产.csv')


class NetworkGraph:
    def __init__(self, number):
        self.nodes_df, self.edges_df = self.load_data(number)
        self.G = self.create_graph()
        self.label_colors = {
            'Domain': '#636EFA',
            'Whois_Phone': '#EF553B',
            'Whois_Email': '#00CC96',
            'Whois_Name': '#AB63FA',
            'IP': '#FFA15A',
            'IP_C': '#5fab28',
            'Cert': '#19D3F3',
            'ASN': '#FF6692'
        }

        self.edge_colors = {'r_cert': '#19D3F3',
                            'r_subdomain': '#636EFA',
                            'r_request_jump': '#636EFA',
                            'r_dns_a': '#FFA15A',
                            'r_whois_name': '#AB63FA',
                            'r_whois_email': '#00CC96',
                            'r_whois_phone': '#EF553B',
                            'r_cert_chain': '#19D3F3',
                            'r_cname': '#636EFA',
                            'r_asn': '#FECB52',
                            'r_cidr': '#5fab28'
                            }

    def load_data(self, number):
        nodes_df = pd.read_csv(f'data/team{number}/node.csv')
        edges_df = pd.read_csv(f'data/team{number}/link.csv')
        return nodes_df, edges_df

    def create_graph(self):
        g = nx.Graph()
        for i, row in self.nodes_df.iterrows():
            g.add_node(row['id'], label=row['type'])
        for i, row in self.edges_df.iterrows():
            g.add_edge(row['source'], row['target'], label=row['relation'])
        return g

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
                            line=dict(color='#204c6b', width=0.1))

        fig.update_traces(marker=dict(size=8))
        return fig


def generate_pie_chart():
    df = nodes_df

    type_counts = df['type'].value_counts()
    # 计算每种'type'的数量并转换为DataFrame
    type_counts_df = type_counts.reset_index()
    type_counts_df.columns = ['type', 'count']

    # 创建饼图并显示图例
    fig = px.pie(names=type_counts_df['type'], values=type_counts_df['count'],
                 title='资产类型组成', height=350, width=500)

    fig.update_layout(plot_bgcolor='rgba(0, 0, 0, 0)', paper_bgcolor='rgba(0,0,0,0)',
                      legend_font_color='white', title_font_color='white')
    fig.update_traces(textfont_color='white')
    return fig


def generate_edge_pie_chart():
    df = edges_df

    type_counts = df['relation'].value_counts()
    # 计算每种'type'的数量并转换为DataFrame
    type_counts_df = type_counts.reset_index()
    type_counts_df.columns = ['type', 'count']

    # 创建饼图并显示图例
    fig = px.pie(names=type_counts_df['type'], values=type_counts_df['count'],
                 title='关系类型组成', height=350, width=500)

    fig.update_layout(plot_bgcolor='rgba(0, 0, 0, 0)', paper_bgcolor='rgba(0,0,0,0)',
                      legend_font_color='white', title_font_color='white')
    fig.update_traces(textfont_color='white')
    return fig


if __name__ == '__main__':
    network = NetworkGraph(number=1)
    fig = network.plot_network_graph()
