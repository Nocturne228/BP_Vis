import holoviews as hv
from holoviews import opts
from bokeh.embed import file_html
from bokeh.resources import CDN
import networkx as nx
import pandas as pd

from utils.color_palette import label_colors
from utils.data_process import get_node_label

nodes_df = pd.read_csv("data/team1/node.csv")
links_df = pd.read_csv("data/team1/link.csv")

hv.extension('bokeh')

# 按照 type 列分组并排序
nodes_df = nodes_df.sort_values(by='type')


# Function to assign colors based on node type
def get_color_for_type(node_type):
    return label_colors.get(node_type)


# Adding color to nodes_df
nodes_df['color'] = nodes_df['type'].apply(get_color_for_type)
links_df['color'] = links_df['target'].apply(get_node_label).apply(get_color_for_type)

# Create a NetworkX graph
G = nx.Graph()

# Add nodes with attributes
for _, row in nodes_df.iterrows():
    G.add_node(row['id'], label=row['type'], color=row['color'])

# Add edges with attributes
for _, row in links_df.iterrows():
    G.add_edge(row['source'], row['target'], value=1, relation=row['relation'])

# Create holoviews dataset from NetworkX graph
nodes_hv = hv.Dataset(nodes_df, 'id')
edges_hv = hv.Dataset(links_df, ['source', 'target'])

# Create Chord diagram
chord = hv.Chord((edges_hv, nodes_hv))

# Customize Chord diagram
chord.opts(
    opts.Chord(
        cmap='Category20',
        edge_cmap='Category20',
        labels='ype',
        edge_color='color',
        node_color='color',
        node_size=10,
        width=400,
        height=400,
        bgcolor='rgba(0,0,0,0)',  # 设置背景透明
        label_text_color='white'  # 设置文字颜色为白色
    )
)

# 渲染为 Bokeh 图表
bokeh_chord = hv.render(chord, backend='bokeh')


# 设置背景透明和文字颜色为白色
bokeh_chord.background_fill_color = None
bokeh_chord.border_fill_color = None
bokeh_chord.outline_line_color = None

# 自定义工具栏样式
bokeh_chord.toolbar.logo = None  # 去除Bokeh的logo
bokeh_chord.toolbar_location = 'above'
bokeh_chord.toolbar.autohide = True


# 转换为HTML
chord_graph_html_content = file_html(bokeh_chord, CDN, "Chord Diagram")
