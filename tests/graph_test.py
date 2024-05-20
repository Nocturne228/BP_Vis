from dash import Dash, html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
import dash_cytoscape as cyto
import base64

app = Dash(__name__)

# 示例数据
elements = [
    {'data': {'id': 'node1', 'label': 'A', 'colors': ['#ff0000', '#00ff00']}},
    {'data': {'id': 'node2', 'label': 'B', 'colors': ['#0000ff']}},
    {'data': {'id': 'node3', 'label': 'C', 'colors': ['#ff00ff', '#ffff00', '#00ffff']}},
    {'data': {'id': 'node4', 'label': 'D', 'colors': []}},
    {'data': {'source': 'node1', 'target': 'node2'}},
    {'data': {'source': 'node2', 'target': 'node3'}},
    {'data': {'source': 'node3', 'target': 'node4'}},
]


# 生成 SVG 图像
def generate_svg(colors):
    rect_width = 100 / len(colors)
    svg_parts = [f'<rect width="{rect_width}%" height="100%" x="{i * rect_width}%" fill="{color}" />' for i, color in
                 enumerate(colors)]
    svg_content = ''.join(svg_parts)
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100">{svg_content}</svg>'
    svg_base64 = base64.b64encode(svg.encode('utf-8')).decode('utf-8')
    return f'data:image/svg+xml;base64,{svg_base64}'


# 生成节点样式
def generate_node_styles(elements, show_colors):
    styles = []
    for element in elements:
        if 'source' in element['data'] and 'target' in element['data']:
            continue
        colors = element['data'].get('colors', [])
        if colors and show_colors:
            background = generate_svg(colors)
        else:
            background = "#FFFFFF" if show_colors else "#808080"  # 设置默认灰色

        styles.append({
            'selector': f'node[id = "{element["data"]["id"]}"]',
            'style': {
                'background-image': background,
                'background-fit': 'cover cover',
                'background-clip': 'node',
            }
        })
    return styles


app.layout = html.Div([
    dbc.Button('Toggle Colors', id='toggle-button', n_clicks=0),
    cyto.Cytoscape(
        id='cytoscape',
        elements=elements,
        style={'width': '100%', 'height': '400px'},
        layout={'name': 'grid'}
    )
])


@app.callback(
    Output('cytoscape', 'stylesheet'),
    Input('toggle-button', 'n_clicks'),
    State('cytoscape', 'elements')
)
def update_node_colors(n_clicks, elements):
    show_colors = n_clicks % 2 == 1  # 切换显示颜色
    return generate_node_styles(elements, show_colors)


if __name__ == '__main__':
    app.run_server(debug=True)
