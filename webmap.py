import folium
map=folium.Map(location=[30.517683,76.659473],zoom_start=17)
lat=[30.514845,30.515752,30.515147,30.516566,29.917286]
lon=[76.660143,76.660685,76.659795,76.660484,73.847672]
loc=["You are at TQ ","You are at Central Library","You are at Square One ","You are at Turing Block ","Manish Panwar house"]

def color(latitude):
    if latitude<30:
        return "orange"
    else :
        return "darkpurple"

for lt,ln,lc in zip(lat,lon,loc):
    map.add_child(folium.Marker(location=[lt,ln],popup="Hello "+lc,icon=folium.Icon(color=color(lt))))

map.save("C_Map.html")
