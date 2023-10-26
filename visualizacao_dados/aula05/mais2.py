import folium
import folium as fl
import numpy as np
import pandas as pd
from folium.plugins import HeatMap

# lendo os dados do dataframe
cidades_visitadas = pd.read_csv('../av2/cidades_visitadas.csv')
calor = pd.read_csv('../av2/dados_calor.csv')
status = pd.read_csv('../av2/Status.csv')

cidade_rj = r'Limite_de_Bairros.geojson'
rocha = r'rocha'
nilo = r'nilópolis.TXT'

# minha variável principal
mapa = fl.Map([-22.9305, -43.5860686], start_zoom=8)
fl.GeoJson(rocha).add_to(mapa)

 # long e latitude quaisquer, busque no arquivo
fl.Marker([-43.337277251067633, -22.825956917366085], tooltip='Hudson', icon=fl.Icon()).add_to(mapa)

# fl.Map([0, 0])
# HeatMap(cidades_visitadas).add_to(mapa)

mapa.show_in_browser()
