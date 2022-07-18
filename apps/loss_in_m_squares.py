import ee
ee.authenticate()
import geemap
import geopandas
from shapely.geometry import Polygon

roi=ee.Geometry.Polygon()
#get the geometry input from the user
geometry= ee.Geometry.Polygon(roi)
Map.addLayer(geometry, {}, 'geometry.json')
#get the geometry input from the user

#get the forest loss image provided from hansen datasets
gfc2014= ee.Image('UMD/hansen/global_forest_change_2015')
lossImage = gfc2014.select(['loss'])
areaImage = lossImage.multiply(ee.Image.pixelArea())

#sum the values of forest loss pixels into the added geometry
stats= areaImage.reduceRegion({
    reducer:ee.Reducer.sum(),
    geometry:geometry,
    scale:30,
    maxPixels: 1e9
})
print('pixels representing loss: ', stats.get('loss'),'square meters')
print('pixels representing loss: ', stats.get('loss'),'square meters')
