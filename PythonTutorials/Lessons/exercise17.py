import requests

url = 'https://www.yahoo.com/'
r = requests.get(url)
r_html = r.text