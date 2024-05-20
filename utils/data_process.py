import re

industry_mapping = {
    'A': '涉黄',
    'B': '涉赌',
    'C': '诈骗',
    'D': '涉毒',
    'E': '涉枪',
    'F': '黑客',
    'G': '非法交易平台',
    'H': '非法支付平台',
    'I': '其他'
}

industry_colors = {
    'A': '#fcff00',  # 涉黄
    'B': '#fa3586',  # 涉赌
    'C': '#5733FF',  # 诈骗
    'D': '#acff1a',  # 涉毒
    'E': '#FF33FF',  # 涉枪
    'F': '#33FFFF',  # 黑客
    'G': '#FF8C00',  # 非法交易平台
    'H': '#9eb9ff',  # 非法支付平台
    'I': '#00FA9A'  # 其他
}


def get_color_for_industry(industry_codes):
    industry_codes_list = re.findall(r"'(\w+)'", industry_codes)
    colors = []
    for code in industry_codes_list:
        color = industry_colors.get(code, '#000000')  # 默认黑色
        colors.append(color)
    return colors


def get_node_label(node_id):
    node_label_list = ['Domain', 'IP', 'Cert', 'Whois_Name', 'Whois_Phone', 'Whois_Email', 'IP_C', 'ASN']
    if 'IP_C' in node_id:
        return 'IP_C'

    for label in node_label_list:
        if label != 'IP_C' and label in node_id:
            return label

    return None  # 如果未找到对应的标签，返回 None


def get_neighbors_with_edges(elements, node_id, hops):
    """
    Find all neighboring nodes and edges within a specified number of hops from a given node.

    This function performs a breadth-first search (BFS) on the graph represented by `elements`
    to find all nodes and edges that are within a certain number of hops from the specified node.
    The graph is described by a list of elements where each element is a dictionary
    representing either a node or an edge.

    Parameters:
    elements (list): A list of dictionaries representing the graph's nodes and edges.
                     Each dictionary must contain a 'data' key with relevant node or edge information.
                     Nodes have an 'id' key, and edges have 'source' and 'target' keys.
    node_id (str): The ID of the starting node from which the search will begin.
    hops (int): The maximum number of hops from the starting node to consider.

    Returns:
    tuple: A tuple containing two sets:
           - A set of node IDs that are within the specified number of hops from the starting node.
           - A set of edges that are within the specified number of hops from the starting node.

    Example:
    elements = [
        {'data': {'id': 'A', 'label': 'Node A'}},
        {'data': {'id': 'B', 'label': 'Node B'}},
        {'data': {'source': 'A', 'target': 'B', 'label': 'Edge AB'}}
    ]
    neighbors, edges = get_neighbors_with_edges(elements, 'A', 1)
    print(neighbors)  # Output: {'A', 'B'}
    print(edges)  # Output: {('A', 'B')}
    """
    visited = set()
    queue = [(node_id, 0)]
    neighbors = set()
    edges = set()

    while queue:
        current_node, current_hop = queue.pop(0)
        if current_hop > hops:
            break
        if current_node not in visited:
            visited.add(current_node)
            neighbors.add(current_node)
            for ele in elements:
                if 'source' in ele['data'] and 'target' in ele['data']:
                    source = ele['data']['source']
                    target = ele['data']['target']
                    if source == current_node and target not in visited:
                        queue.append((target, current_hop + 1))
                        edges.add((source, target))
                    elif target == current_node and source not in visited:
                        queue.append((source, current_hop + 1))
                        edges.add((source, target))

    return neighbors, edges
