import xml.etree.ElementTree as et
from lxml import etree
import os
import zipfile

file_path = r"C:\Users\krbyk\Desktop\Dortyol_Yangin.kmz"

in_kmz = os.path.abspath(file_path)
out_dir = os.path.dirname(in_kmz)
out_kml = os.path.join(out_dir, "doc.kml")
with zipfile.ZipFile(in_kmz, "r") as zip_ref:
    zip_ref.extractall(out_dir)



root = etree.parse(out_kml)

for e in root.iter():
    path = root.getelementpath(e).split("}")[0] + "}"

tree = et.parse(out_kml)
root = tree.getroot()

name = root.find(f".//*{path}coordinates")
geolist = name.text.strip().split(" ")

geometry = []

for i in geolist:
    current = i.split(",")
    # en az 3 point içermesi lazım yoksa EEException error veriyor.
    geometry.append([float(current[0]), float(current[1])])

print(geometry)
