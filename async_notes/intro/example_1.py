import requests

response = requests.get('https://www.example.com')
response2 = requests.get('https://www.example.com')

items = response.headers.items()

headers = [f'{key}: {header}' for key, header in items]

formatted_headers = '\n'.join(headers)

with open('headers.txt', 'w') as file:
    file.write(formatted_headers)

# Accept-Ranges: bytes
# Content-Type: text/html - format danych w jakiej odpowiedź została zwrócona
# ETag: "84238dfc8092e5d9c0dac8ef93371a07:1736799080.121134"
# Last-Modified: Mon, 13 Jan 2025 20:11:20 GMT
# Vary: Accept-Encoding
# Content-Encoding: gzip
# Content-Length: 648
# Cache-Control: max-age=1589
# Date: Sat, 22 Feb 2025 10:42:44 GMT
# Alt-Svc: h3=":443"; ma=93600,h3-29=":443"; ma=93600,h3-Q050=":443"; ma=93600,quic=":443"; ma=93600; v="46,43"
# Connection: keep-alive