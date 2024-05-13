# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd
from graphs.figures import NetworkGraph
import dash_cytoscape as cyto


app = Dash(__name__)

colors = {
    'background': '#FFFFFF',
    'text': '#7FDBFF'
}

network = NetworkGraph(number=1)
fig = network.plot_network_graph()
cy_graph = network.cyto_graph_plot()

# 定义样式表，设置节点的样式
stylesheet = [
    {'selector': 'node', 'style': {'label': 'data(label)', 'color': 'black'}},  # 显示文本标签，颜色为黑色
    {'selector': 'edge', 'style': {'line-color': 'blue', 'width': 0.1}}  # 设置边的样式
]


app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Hello Dash',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='Dash: A web application framework for your data.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(
        id='example-network-graph-scatter',
        figure=fig
    ),

    # 添加 cy_graph 到布局中
    html.Div(children=[
        html.H2("Cytoscape Graph"),
        cy_graph
    ])

])

if __name__ == '__main__':
    app.run(debug=True)
