import requests

html = requests.get('htpps://robertsspaceindustries.com/ship-specs').content.decode()
print(html[:1000])