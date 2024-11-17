def magic(**kwargs):
    styles = "".join(f'{key}: {value}; ' for key, value in kwargs.items())
    html = f'<p style="{styles}"></p> '
    print(html)


css_dict = {
    "color": "peru",
    "text-decoration": "underline",
    "font-size": "2rem"
}

magic(**css_dict)