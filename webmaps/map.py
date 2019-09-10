import folium
import pandas
import json
map = folium.Map(location=[38.58,-99.09], zoom_start=6)

def color_prod(elev):
    if elev > 1000:
        return "green"
    elif 1000 <= elev < 2500:
        return 'black'
    else:
        return "red"

data = pandas.read_csv(r"C:\Users\hp.1\PycharmProjects\webmaps\webmaps\Resources\volc.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
fgv = folium.FeatureGroup(name="Volcanoes")
# for x,y,z in zip(lat,lon, elev):
#     fg.add_child(folium.Marker(location=[x,y], popup=str(z)+"m",icon=folium.Icon(color=color_prod(z))))

for x,y,z in zip(lat,lon, elev):
    fgv.add_child(folium.CircleMarker(location=[x,y], radius=6, popup=str(z)+"m",fill_color=color_prod(z), color='grey',fill_opacity=0.7))
dat = pandas.read_csv(r"C:\Users\hp.1\PycharmProjects\webmaps\webmaps\Resources\world.json")

fgp = folium.FeatureGroup(name="POP")

fgp.add_child(folium.GeoJson(data=open(dat, encoding="cp1252"),
                            style_function=lambda x : {'fillColor':'y ellow'}))



map.add_child(fgv)
map.add_child(folium.LayerControl())
map.save("Map1.html")
