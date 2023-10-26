"""
=======================AV2=======================
Visualização de Dados (Eletiva.)
NOME: Daniel Brown Rodrigues Mingozzi dos Passos
MATRICULA: 2213332136
"""
import branca.colormap
import folium
import numpy as np
from folium.plugins import HeatMap

mapa_calor = np.genfromtxt('dados_calor.csv', delimiter=",")
mapa = folium.Map([-22.811967, -43.413623], start_zoom=7)


nilo = r'nilópolis.TXT'  # município de nilópolis
folium.GeoJson(nilo).add_to(mapa)
folium.Marker([-22.811967, -43.413623], icon=folium.Icon(color='red')).add_to(mapa)

HeatMap(data=mapa_calor, radius=80, blur=100, min_opacity=20).add_to(mapa)

# mapa.save("mapa_calor_de_nilópolis.html")
mapa.show_in_browser()
