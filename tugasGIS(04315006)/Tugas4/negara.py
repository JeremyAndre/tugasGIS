import mapnik
m = mapnik.Map(1080,720)
m.background = mapnik.Color('cyan')
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#f6ff00')
r.symbols.append(polygon_symbolizer) 

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('red'), 1)
line_symbolizer.stroke_width =  10.0
r.symbols.append(line_symbolizer)

basinsLabels = mapnik.TextSymbolizer(mapnik.Expression('[NAME]'), 'DejaVu Sans Bold' ,8,mapnik.Color('black'))
basinsLabels.halo_fill = mapnik.Color('blue')
basinsLabels.halo_radius = 1
r.symbols.append(basinsLabels)

point_sym = mapnik.PointSymbolizer()
point_sym.allow_overlap = True
r.symbols.append(point_sym)

s.rules.append(r)

highlight = mapnik.PolygonSymbolizer()
highlight.fill = mapnik.Color('red')
japan = mapnik.Rule()
japan.filter = mapnik.Expression("[NAME]='Japan'")
japan.symbols.append(highlight)
s.rules.append(japan)

m.append_style('My Style',s)
ds = mapnik.Shapefile(file="shp1/ne_110m_admin_0_countries.shp")
layer = mapnik.Layer('world')
layer.datasource = ds
layer.styles.append('My Style')
m.layers.append(layer)
m.zoom_all()
mapnik.render_to_file(m, 'negara.pdf', 'pdf')
print "rendered image to 'negara.pdf' "