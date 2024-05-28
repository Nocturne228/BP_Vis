# import networkx as nx
# import community.community_louvain as community_louvain
# import matplotlib.pyplot as plt
# import pandas as pd
#
# nodes_df = pd.read_csv("../data/team4/node.csv")
# edges_df = pd.read_csv("../data/team4/link.csv")
#
# G = nx.Graph()
# for i, row in nodes_df.iterrows():
#     G.add_node(row['id'], label=row['type'], name=row['name'], industry=row['industry'])
# for i, row in edges_df.iterrows():
#     G.add_edge(row['source'], row['target'], label=row['relation'])
#
#
#
# # 应用Louvain社区检测算法
# partition = community_louvain.best_partition(G)
#
# # 为每个节点分配颜色
# colors = [partition[node] for node in G.nodes()]
#
# # 绘制网络图
# pos = nx.kamada_kawai_layout(G)
# plt.figure(figsize=(10, 10))
# nx.draw_networkx_nodes(G, pos, node_color=colors, cmap=plt.cm.viridis, node_size=50)
# nx.draw_networkx_edges(G, pos, alpha=0.5)
# plt.title("Louvain Community Detection")
# plt.show()
#
#
