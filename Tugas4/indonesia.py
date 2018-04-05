import mapnik
m = mapnik.Map(800,400)
m.background = mapnik.Color('red')
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#f0ffff')
r.symbols.append(polygon_symbolizer) 

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('yellow'), 1)
line_symbolizer.stroke_width =  10.0

basinsLabels = mapnik.TextSymbolizer(mapnik.Expression('[Propinsi]'), 'DejaVu Sans Bold' ,10,mapnik.Color('black'))
basinsLabels.halo_fill = mapnik.Color('blue')
basinsLabels.halo_radius = 1
r.symbols.append(basinsLabels)

point_sym = mapnik.PointSymbolizer()
point_sym.allow_overlap = True
r.symbols.append(point_sym)

r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('My Style',s)
ds = mapnik.Shapefile(file="shp2/INDONESIA_PROP.shp")
layer = mapnik.Layer('world')
layer.datasource = ds
layer.styles.append('My Style')
m.layers.append(layer)

s = mapnik.Style()
r = mapnik.Rule()

line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('red'),1)
r.symbols.append(line_symbolizer)
s.rules.append(r)

m.zoom_all()
mapnik.render_to_file(m, 'indonesia.pdf', 'pdf')
print "rendered image to 'indonesia.pdf' "

