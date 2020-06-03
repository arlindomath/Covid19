import folium
from folium.plugins import HeatMap
import pandas as pd

##Dados da Plataforma Brasil.io
dados_covid19 = pd.read_csv('https://raw.githubusercontent.com/wcota/covid19br/master/cases-gps.csv')

mapa = folium.Map (location=[-15.77972, -47.92972], zoom_start=4, min_zoom=4, control_scale=True)

locais = dados_covid19 [["lat","lon"]].values.tolist()

HeatMap (locais, radius=13).add_to(mapa)
mapa.save('mapa.html')

