#get the geometry input from the user
geometry= ee.Geometry.Polygon(
  [
    [ // exterior ring
      [100.0, 0.0],
      [103.0, 0.0],
      [103.0, 3.0],
      [100.0, 3.0],
      [100.0, 0.0]  // matching the first vertex is optional
    ],
    [ // interior ring
      [101.0, 1.0],
      [102.0, 2.0],
      [102.0, 1.0]
    ]
  ]
)
Map.addLayer(geometry, {}, 'geometry.json');

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