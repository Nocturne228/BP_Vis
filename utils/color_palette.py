import matplotlib.colors as mcolors

# bright_colors = {
#     'Domain': '#6570ff',
#     'Whois_Phone': '#ff5b3f',
#     'Whois_Email': '#00f5b4',
#     'Whois_Name': '#ae65ff',
#     'IP': '#ffa15a',
#     'IP_C': '#72cd30',
#     'Cert': '#1addff',
#     'ASN': '#ff6692'
# }
#
# dark = {
#     'Domain': '#2c3263',
#     'Whois_Phone': '#64291a',
#     'Whois_Email': '#005a43',
#     'IP': '#4f3619',
#     'IP_C': '#224717',
#     'Cert': '#13455b',
#     'ASN': '#5c2e2e'
# }

label_colors = {
    'Domain': '#636EFA',
    'Whois_Phone': '#EF553B',
    'Whois_Email': '#00CC96',
    'Whois_Name': '#AB63FA',
    'IP': '#FFA15A',
    'IP_C': '#5fab28',
    'Cert': '#19D3F3',
    'ASN': '#FF6692'
}
edge_colors = {
    'r_cert': '#19D3F3',
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


def adjust_brightness(color_hex, factor=1.2):
    rgb_tuple = mcolors.hex2color(color_hex)
    hsv_tuple = mcolors.rgb_to_hsv(rgb_tuple)
    adjusted_hsv = (hsv_tuple[0], hsv_tuple[1], min(1, hsv_tuple[2] * factor))
    adjusted_rgb = mcolors.hsv_to_rgb(adjusted_hsv)
    adjusted_hex = mcolors.rgb2hex(adjusted_rgb)
    return adjusted_hex


def reduce_brightness(hex_color, factor=0.5):
    """
    输入一个十六进制的RGB色彩值，返回其变灰的颜色
    """
    if '#' in hex_color:
        hex_color = hex_color.lstrip('#')
    # Convert hex color to RGB
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)

    # Reduce brightness
    r_new = int(r * factor)
    g_new = int(g * factor)
    b_new = int(b * factor)

    # Ensure values are within valid range (0-255)
    r_new = min(max(r_new, 0), 255)
    g_new = min(max(g_new, 0), 255)
    b_new = min(max(b_new, 0), 255)

    # Convert RGB back to hex
    return '#{:02x}{:02x}{:02x}'.format(r_new, g_new, b_new)
