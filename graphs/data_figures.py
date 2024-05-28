import pandas as pd
import networkx as nx
import plotly.express as px
import plotly.graph_objects as go

from data.data_df import nodes_df, edges_df, core_node, key_link
from utils.color_palette import label_colors

col_swatch = px.colors.qualitative.Light24


class NetworkGraph:
    def __init__(self, number=1):
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
                 title='资产类型组成', height=500, width=500)

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
                 title='关系类型组成', height=500, width=500)

    fig.update_layout(plot_bgcolor='rgba(0, 0, 0, 0)', paper_bgcolor='rgba(0,0,0,0)',
                      legend_font_color='white', title_font_color='white')
    fig.update_traces(textfont_color='white')
    return fig


def generate_core_info():
    pass


def generate_link_sankey():
    from utils.data_process import get_node_label
    node_labels = ['Domain', 'IP', 'Cert', 'Whois_Name', 'Whois_Phone', 'Whois_Email', 'IP_C', 'ASN']

    nodes = list(node_labels)
    links = []
    for index, row in key_link.iterrows():
        source_label = get_node_label(row['source'])
        target_label = get_node_label(row['target'])
        if source_label and target_label and source_label != target_label:
            links.append({
                'source': nodes.index(source_label),
                'target': nodes.index(target_label),
                'value': 1,  # 流量值设为 1
                'label': row['relation']  # 链接的标签为关系列
            })

    # 创建 Sankey 图
    sankey_fig = go.Figure(
        go.Sankey(
            node=dict(
                pad=15,
                thickness=20,
                line=dict(color="black", width=0.5),
                label=nodes,
                color=[label_colors[label] for label in nodes]

            ),
            link=dict(
                source=[link['source'] for link in links],
                target=[link['target'] for link in links],
                value=[link['value'] for link in links],
                label=[link['label'] for link in links],
                color=[label_colors[nodes[link['target']]] for link in links],
            ),
        ),
    )

    # 设置图表标题
    sankey_fig.update_layout(title_text="关键链路流向图")
    sankey_fig.update_layout(plot_bgcolor='rgba(0, 0, 0, 0)', paper_bgcolor='rgba(0,0,0,0)',
                             legend_font_color='white', title_font_color='white', font_color='white')

    # 显示图表
    return sankey_fig


if __name__ == '__main__':
    network = NetworkGraph(number=1)
    fig = network.plot_network_graph()
