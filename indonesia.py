import mapnik
m = mapnik.Map(800,400)
m.background = mapnik.Color('red')
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#f6ff00')
r.symbols.append(polygon_symbolizer) 

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('blue'), 1)
line_symbolizer.stroke_width =  6.0

r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('My Style',s)
ds = mapnik.Shapefile(file="shp2/INDONESIA_PROP.shp")
layer = mapnik.Layer('world')
layer.datasource = ds
layer.styles.append('My Style')
m.layers.append(layer)
m.zoom_all()
mapnik.render_to_file(m, 'indonesia.jpeg', 'jpeg')
print "rendered image to 'indonesia.jpeg' "

