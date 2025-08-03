import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import os

APP_TITLE = "Cafe Map Visualizer"
APP_SUBTITLE = "Prueba Dashboard"

@st.cache_data
def load_geojson():
    """Carga el archivo GeoJSON con cache para mejorar rendimiento"""
    # Usar el archivo optimizado primero, luego el original como respaldo
    optimized_path = 'Data/cober_arborea_2021_optimized.geojson'
    original_path = 'Data/cober_arborea_2021_dissolve_4326.geojson'
    
    if os.path.exists(optimized_path):
        return optimized_path
    elif os.path.exists(original_path):
        st.warning("Usando archivo original. Se recomienda usar el archivo optimizado para mejor rendimiento.")
        return original_path
    else:
        st.error("No se encontró ningún archivo GeoJSON")
        return None

def display_map():
    try:
        geojson_path = load_geojson()
        if geojson_path is None:
            st.error("No se puede cargar el mapa sin el archivo GeoJSON")
            return
        
        map = folium.Map(location=[9.7489, -83.7534], zoom_start=8, tiles="CartoDB positron")
        
        # Agregamos manejo de errores para la carga del GeoJSON
        choropleth = folium.Choropleth(
            geo_data=geojson_path,
            line_weight=1,
            line_opacity=0.7,
            fill_opacity=0.5
        )
        choropleth.geojson.add_to(map)
        st_map = st_folium(map, width=850, height=600)
        
    except Exception as e:
        st.error(f"Error al cargar el mapa: {str(e)}")
        st.info("Esto puede deberse al tamaño del archivo GeoJSON (212MB). Considera optimizar el archivo.")


def main():
    st.set_page_config(page_title=APP_TITLE)
    st.title(APP_TITLE)
    st.caption(APP_SUBTITLE)
    
    display_map()

if __name__ == "__main__":
    main()