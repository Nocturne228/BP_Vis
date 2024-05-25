import pandas as pd


node_label = ['Domain', 'IP', 'Cert', 'Whois_Name', 'Whois_Phone', 'Whois_Email', 'IP_C', 'ASN']

team_no = 9

csv_path = f'data/team{team_no}/'

nodes_df = pd.read_csv(csv_path + 'node.csv')
edges_df = pd.read_csv(csv_path + 'link.csv')
core_node = pd.DataFrame()
key_link = pd.DataFrame()

try:
    # 尝试读取CSV文件
    core_node = pd.read_csv(csv_path + '核心资产.csv')
    key_link = pd.read_csv(csv_path + '关键链路.csv')
    # 如果成功读取文件，则继续执行后续操作
except FileNotFoundError:
    print("文件不存在，请检查文件路径是否正确。")
except pd.errors.EmptyDataError:
    print("文件为空，无法读取数据。")
except pd.errors.ParserError:
    print("文件格式不正确，无法解析。")
except Exception as e:
    print("发生未知错误:", e)
