import folium
import pandas



map = folium.Map(location= [24.680413, 80.482510],zoom_start= 2, tiles = "CartoDB dark_matter")

fg = folium.FeatureGroup(name = "Confirmed Cases")

data = pandas.read_csv("confirmcase.csv")


print(data)
lat = list(data["Lat"])
lon = list(data["Long"])
no= list(data["6/13/20"])
print(type(no))


def color_producer(no):
    if no>1000:
        return "darkred"
    elif 100<=no<1000:
        return "orange"
    else:
        return "green"
   

for lat , lon ,no in zip(lat , lon, no):
    fg.add_child(folium.CircleMarker(location=[lat, lon] ,radius=6, popup= "Total Cases : %s"%no, fill_color =color_producer(no), color ="grey", fill_opacity= 0.7 ))


# fg.add_child(folium.GeoJson(data=(open('world.json', 'r', encoding='utf-8-sig').read())))

map.add_child(fg)
map.add_child(folium.LayerControl())
map.save("Map1.html")