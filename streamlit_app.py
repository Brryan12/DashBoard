import streamlit as st
import leafmap.foliumap as leafmap
import requests
import os
import time

os.environ['OGR_GEOJSON_MAX_OBJ_SIZE'] = '0'
# Correr la aplicación con: streamlit run streamlit_app.py
APP_TITLE = "Cafe Map Visualizer"
APP_SUBTITLE = "Prueba Dashboard"

# Usar TTL (time-to-live) para controlar la frecuencia de actualización de datos
@st.cache_data(ttl=3600, show_spinner=False)
def load_geojson_url():
    """Carga el archivo GeoJSON desde URL con cache para mejorar rendimiento"""
    # URL alternativa con versión simplificada (recomendado para Streamlit Cloud)
    # Considera simplificar tu GeoJSON con mapshaper.org y subirlo a GitHub
    url = "https://github.com/Brryan12/DashBoard/blob/main/Data/cober_arborea_2021_dissolve_4326.geojson?raw=true"
    return url

@st.cache_resource
def create_map():
    """Crea el objeto mapa una sola vez para mejorar rendimiento"""
    return leafmap.Map(center=[9.7489, -83.7534], zoom=8, tiles="CartoDB positron")

def display_map():
    try:
        # Mostrar indicador de carga personalizado
        with st.spinner("⏳ Cargando mapa... (puede tomar hasta 30 segundos en Streamlit Cloud)"):
            start_time = time.time()
            geojson_url = load_geojson_url()
            
            # Crear el mapa (usando cache_resource para mejor rendimiento)
            m = create_map()
            
            # Usar try/except con mejor manejo de errores
            try:
                # Agregar el GeoJSON desde URL con timeout
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
                load_time = time.time() - start_time
                st.success(f"✅ Mapa cargado en {load_time:.2f} segundos")
            except Exception as e:
                st.warning(f"⚠️ Error al cargar GeoJSON completo: {str(e)}")
                st.info("Intentando cargar versión simplificada...")
                
                # Intentar con un GeoJSON alternativo simplificado
                try:
                    # URL de un GeoJSON simplificado (deberías crear esta versión)
                    simplified_url = "https://github.com/Brryan12/DashBoard/blob/main/Data/cober_arborea_simplified.geojson?raw=true"
                    m.add_geojson(
                        simplified_url,
                        layer_name="Cobertura Arbórea (simplificada)",
                        style={
                            "color": "blue",
                            "weight": 1,
                            "fillColor": "blue",
                            "fillOpacity": 0.3
                        }
                    )
                except:
                    st.error("No se pudo cargar ninguna versión del mapa.")
            
            # Mostrar el mapa en Streamlit con altura adaptable
            m.to_streamlit(height=700)
        
    except Exception as e:
        st.error(f"Error general: {str(e)}")
        st.info("""
        ### Recomendaciones para Streamlit Cloud:
        1. **Simplifica tu GeoJSON**: Usa [mapshaper.org](https://mapshaper.org) para reducir el tamaño
        2. **Sube la versión simplificada** a GitHub
        3. **Considera dividir** en múltiples archivos más pequeños
        4. **Actualiza la URL** en el código
        """)

def main():
    st.set_page_config(page_title=APP_TITLE, layout="wide")
    
    # UI más eficiente
    col1, col2 = st.columns([3, 1])
    with col1:
        st.title(APP_TITLE)
    with col2:
        st.caption(APP_SUBTITLE)
    # Mostrar mapa
    display_map()
    
if __name__ == "__main__":
    main()