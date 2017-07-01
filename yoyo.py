import folium

map_5 = folium.Map(location=[-7.2604914, 112.79704], zoom_start=13, tiles='Stamen Terrain')


# menambahkan marker icon untuk polygon brapa segi number_of_sides
folium.RegularPolygonMarker(location=[-7.2818592, 112.7922268], popup='ITS',
                   fill_color='#132b5e', number_of_sides=3, radius=10).add_to(map_5)
folium.Marker([-7.2880833, 112.7764523], popup='Universitas Narotama', icon = folium.Icon(icon = 'cloud', angle=90)).add_to(map_5)
folium.RegularPolygonMarker(location=[-7.2722831, 112.758034], popup='Universitas Airlangga',
                   fill_color='#769d96', number_of_sides=6, radius=10).add_to(map_5)
folium.RegularPolygonMarker(location=[-7.2926871, 112.7912904], popup='Universitas Hang Tuah',
                   fill_color='#769d96', number_of_sides=8, radius=10).add_to(map_5)
map_5.save('example5.html')
