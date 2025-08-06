import streamlit as st
import leafmap.foliumap as leafmap
import requests
import os

# Establecer límite de tamaño para GeoJSON (0 para sin límite)
os.environ['OGR_GEOJSON_MAX_OBJ_SIZE'] = '0'

# Correr la aplicación con: streamlit run streamlit_app.py
APP_TITLE = "Cafe Map Visualizer"
APP_SUBTITLE = "Prueba Dashboard"

@st.cache_data
def load_geojson_url():
    """Carga el archivo GeoJSON desde URL con cache para mejorar rendimiento"""
    # URL para el archivo GeoJSON
    url = "https://github.com/Brryan12/DashBoard/blob/main/Data/cober_arborea_2021_dissolve_4326.geojson?raw=true"
    return url

def display_map():
    try:
        with st.spinner("Cargando mapa... esto puede tomar un momento para archivos grandes"):
            geojson_url = load_geojson_url()
            
            # Crear el mapa centrado en Costa Rica
            m = leafmap.Map(center=[9.7489, -83.7534], zoom=8, tiles="CartoDB positron")
            
            # Método alternativo para GeoJSON grandes
            try:
                # Agregar el GeoJSON desde URL
                m.add_geojson(
                    geojson_url,
                    layer_name="Cobertura Arbórea",
                    style={
                        "color": "blue",
                        "weight": 1,
                        "fillColor": "blue",
                        "fillOpacity": 0.3,
                        "interactive": False
                    }
                )
            except Exception as e:
                st.warning(f"Error al cargar con método estándar: {str(e)}")
            # Mostrar el mapa en Streamlit 
            m.to_streamlit(height=700)
        
    except Exception as e:
        st.error(f"Error al cargar el mapa: {str(e)}")
        st.info("""
        El archivo GeoJSON es demasiado grande (>50MB). Recomendaciones:
        1. Usa un GeoJSON más pequeño
        2. Simplifica la geometría con mapshaper.org
        """)

def main():
    st.set_page_config(page_title=APP_TITLE, layout="wide")
    st.title(APP_TITLE)
    st.caption(APP_SUBTITLE)
    
    # Sidebar con información
    # st.sidebar.title("Información")
    # st.sidebar.info("Visualizador de datos geoespaciales de cobertura arbórea en Costa Rica")
    
    # Mostrar mapa
    display_map()

if __name__ == "__main__":
    main()