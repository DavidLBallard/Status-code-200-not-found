
import requests

r = requests.get('', timeout=5)

if r.status_code != 200:
