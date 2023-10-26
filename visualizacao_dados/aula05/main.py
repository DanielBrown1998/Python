import folium as fl
import numpy as np
import pandas as pd
from folium.plugins import HeatMap

# lendo os dados
cidades = pd.read_csv('../av2/cidades_visitadas.csv')
calor = pd.read_csv('../av2/dados_calor.csv')
status = pd.read_csv('../av2/Status.csv')

# cria um mapa ([longitude, latitude])
mapa = fl.Map([-22.9305, -43.5860686], start_zoom=8)
# delimitar o municipio de sua escolha...vá em 'json rio de janeiro no primeiro link'
# vá em raw
# pegue a URL(copie)

geoRJ = 'https://raw.githubusercontent.com/tbrugz/geodata-br/master/geojson/geojs-33-mun.json'

# RJ inteiro
# fl.GeoJson(geoRJ).add_to(mapa)

# na pag ue vc buscou, copie alguns dados entre os colchetes e adicione-os em um arquivo .txt

angra = 'angra.TXT'
nilo = 'nilópolis.TXT'

# adicionado angra dos reis e nilópolis

fl.GeoJson(angra).add_to(mapa)
fl.GeoJson(nilo).add_to(mapa)
# mostrando no browser
mapa.show_in_browser()
