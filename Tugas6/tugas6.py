import mapnik
m = mapnik.Map(800,480)
m.background = mapnik.Color('cyan')
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#FFFFFF')
r.symbols.append(polygon_symbolizer) 

#######
line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('yellow'), 0.2)
line_symbolizer.stroke_width =  5.0

r.symbols.append(line_symbolizer) 

#point_sym = mapnik.PointSymbolizer()
#point_sym.allow_overlap = True
#r.symbols.append(point_sym) 

s.rules.append(r)

r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('My Style',s)
ds = mapnik.Shapefile(file="shp2/INDONESIA_PROP.shp")
layer = mapnik.Layer('indonsesia')
layer.datasource = ds
layer.styles.append('My Style')
m.layers.append(layer)


#######
#r.symbols.append(line_symbolizer) 

#point_sym = mapnik.PointSymbolizer()
#point_sym = mapnik.MarkersSymbolizer()
#point_sym.filename = 'simbol2.png'
#point_sym.allow_overlap = True
#point_sym.transform = "scale(0.5, 0.5)"
#r.symbols.append(point_sym) 

#s.rules.append(r)

#m.append_style('My Style1',s)
#ds = mapnik.Shapefile(file="SHP_Dataran_tinggi_Bali/DataranTinggi.shp")
#layer = mapnik.Layer('DataranTinggi')
#layer.datasource = ds
#layer.styles.append('My Style1')
#m.layers.append(layer)


#######
r.symbols.append(line_symbolizer) 

point_sym = mapnik.PointSymbolizer()
point_sym = mapnik.MarkersSymbolizer()
point_sym.allow_overlap = True
point_sym.transform = "scale(0.5, 0.5)"
r.symbols.append(point_sym) 

s.rules.append(r)

m.append_style('My Style2',s)
ds = mapnik.Shapefile(file="shpgunungpulaujawa/gunungpulaujawa.shp")
layer = mapnik.Layer('gunungjawa')
layer.datasource = ds
layer.styles.append('My Style2')
m.layers.append(layer)


#######
m.zoom_all()
mapnik.render_to_file(m, 'gunungjawa.pdf', 'pdf')
print "rendered image to 'JOSS ISOK' "
