import json


with open(r"C:\Users\krbyk\Desktop\data.geojson","r") as f:
    data = json.loads(f.read())

print(data["features"][0]["geometry"]["coordinates"][0])
