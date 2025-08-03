import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

APP_TITLE = "Cafe Map Visualizer"
APP_SUBTITLE = "Pruba Dashboard"

def display_map():
    map = folium.Map(location=[9.7489, -83.7534], zoom_start=8, tiles="CartoDB positron")
    choropleth = folium.Choropleth(
        geo_data='Data/cober_arborea_2021_dissolve_4326.geojson'
    )
    choropleth.geojson.add_to(map)
    st_map = st_folium(map, width=850, height=600)


def main():
    st.set_page_config(page_title=APP_TITLE)
    st.title(APP_TITLE)
    st.caption(APP_SUBTITLE)
    
    display_map()

if __name__ == "__main__":
    main()