def get_node_label(node_id):
    node_label_list = ['Domain', 'IP', 'Cert', 'Whois_Name', 'Whois_Phone', 'Whois_Email', 'IP_C', 'ASN']
    if 'IP_C' in node_id:
        return 'IP_C'

    for label in node_label_list:
        if label != 'IP_C' and label in node_id:
            return label

    return None  # 如果未找到对应的标签，返回 None
