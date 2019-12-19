import urllib, json
url = "http://127.0.0.1:8000/:"
response = urllib.urlopen(url);
data = json.loads(response.read())
for d in data:
    print d['nombre']

print data
