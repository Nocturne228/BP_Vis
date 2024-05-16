import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_cytoscape as cyto

# 创建Dash应用
app = dash.Dash(__name__)

# 创建两个Cytoscape图的数据
elements_1 = [
    {'data': {'id': 'node1', 'label': 'Node 1'}, 'position': {'x': 50, 'y': 50}},
    {'data': {'id': 'node2', 'label': 'Node 2'}, 'position': {'x': 200, 'y': 50}},
    {'data': {'source': 'node1', 'target': 'node2'}}
]

elements_2 = [
    {'data': {'id': 'node3', 'label': 'Node 3'}, 'position': {'x': 50, 'y': 50}},
    {'data': {'id': 'node4', 'label': 'Node 4'}, 'position': {'x': 200, 'y': 50}},
    {'data': {'source': 'node3', 'target': 'node4'}}
]

# 初始显示第一个Cytoscape图
initial_elements = elements_1

# 创建按钮和Cytoscape图的布局
app.layout = html.Div([
    html.Button('切换图表', id='toggle-button', n_clicks=0),
    cyto.Cytoscape(
        id='toggle-cytoscape',
        layout={'name': 'preset'},
        style={'width': '100%', 'height': '400px'},
        elements=initial_elements
    )
])


# 回调函数，根据按钮点击切换Cytoscape图
@app.callback(
    Output('toggle-cytoscape', 'elements'),
    Input('toggle-button', 'n_clicks')
)
def update_cytoscape(n_clicks):
    # 根据按钮点击次数判断当前应该显示哪个Cytoscape图
    if n_clicks % 2 == 0:
        return elements_1
    else:
        return elements_2


# 运行应用
if __name__ == '__main__':
    app.run_server(debug=True)
