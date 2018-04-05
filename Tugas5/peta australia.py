import mapnik
m = mapnik.Map(800,400)
m.background = mapnik.Color('cyan')
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#f0ffff')
r.symbols.append(polygon_symbolizer) 

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('yellow'), 1)
line_symbolizer.stroke_width =  10.0

basinsLabels = mapnik.TextSymbolizer(mapnik.Expression('[NAME_1]'), 'DejaVu Sans Bold' ,8,mapnik.Color('black'))
basinsLabels.halo_fill = mapnik.Color('pink')
basinsLabels.halo_radius = 2
r.symbols.append(basinsLabels)

point_sym = mapnik.PointSymbolizer()
point_sym.allow_overlap = True
r.symbols.append(point_sym)

r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('My Style',s)
ds = mapnik.Shapefile(file="AUS_administrasi/AUS_adm2.shp")
layer = mapnik.Layer('aus-administrasi')
layer.datasource = ds
layer.styles.append('My Style')
m.layers.append(layer)

#Daerah Perairan di Australia
s = mapnik.Style()
r = mapnik.Rule()

line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('blue'),1)
r.symbols.append(line_symbolizer)
s.rules.append(r)

m.append_style('My Style2',s)
ds = mapnik.Shapefile(file="AUS_perairan/AUS_water_lines_dcw.shp")
layer = mapnik.Layer('aus-pantai')
layer.datasource = ds
layer.styles.append('My Style2')
m.layers.append(layer)

#Jalan Protokol di Australia
s = mapnik.Style()
r = mapnik.Rule()

line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('red'),1)
r.symbols.append(line_symbolizer)
s.rules.append(r)

m.append_style('My Style3',s)
ds = mapnik.Shapefile(file="AUS_roads/AUS_roads.shp")
layer = mapnik.Layer('aus-roads')
layer.datasource = ds
layer.styles.append('My Style3')
m.layers.append(layer)

#Jalur Kereta Api di Australia
s = mapnik.Style()
r = mapnik.Rule()

line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('black'),1)
r.symbols.append(line_symbolizer)
s.rules.append(r)

m.append_style('My Style4',s)
ds = mapnik.Shapefile(file="AUS_railroads/AUS_rails.shp")
layer = mapnik.Layer('aus-railroads')
layer.datasource = ds
layer.styles.append('My Style4')
m.layers.append(layer)

#Batas Wilayah di Australia
s = mapnik.Style()
r = mapnik.Rule()

line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('green'),1)
r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('My Style5',s)
ds = mapnik.Shapefile(file="AUS_administrasi/AUS_adm1.shp")
layer = mapnik.Layer('aus-administrasi')
layer.datasource = ds
layer.styles.append('My Style5')
m.layers.append(layer)

m.zoom_all()
mapnik.render_to_file(m, 'peta australia.pdf', 'pdf')
print "rendered image to 'peta australia.pdf' "