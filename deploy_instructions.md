# Instrucciones para Desplegar la Aplicación Panel

## Opción 1: Panel Cloud (Gratuito y Fácil)

1. **Crear cuenta en Panel Cloud:**
   - Ve a https://panel.holoviz.org/
   - Crea una cuenta gratuita

2. **Preparar el proyecto:**
   ```bash
   # Crear requirements.txt específico para Panel
   echo "panel>=1.0.0
   geopandas>=0.12.0
   folium>=0.14.0
   pyproj>=3.4.0" > requirements_panel_cloud.txt
   ```

3. **Subir a GitHub:**
   - Sube tu código a un repositorio público en GitHub
   - Incluye el archivo requirements_panel_cloud.txt

4. **Desplegar en Panel Cloud:**
   - Conecta tu repositorio de GitHub
   - Selecciona el archivo panel_app_simple.py
   - Panel Cloud automáticamente detectará las dependencias

## Opción 2: Heroku (Gratuito con limitaciones)

1. **Instalar Heroku CLI**
2. **Crear archivos de configuración:**
   - Procfile
   - requirements.txt
   - runtime.txt

3. **Comandos de despliegue:**
   ```bash
   heroku create tu-app-name
   git push heroku main
   ```

## Opción 3: Railway (Recomendada para principiantes)

1. **Ve a railway.app**
2. **Conecta tu repositorio de GitHub**
3. **Railway detecta automáticamente que es una app Python**
4. **Configura la variable de entorno PORT**

## Opción 4: Streamlit Cloud (Si conviertes de vuelta a Streamlit)

1. **Ve a share.streamlit.io**
2. **Conecta tu repositorio**
3. **Despliegue automático**

## Opción 5: Servidor propio con túnel público

Usar ngrok o similar para exponer tu servidor local:

```bash
# Instalar ngrok
# Ejecutar tu app localmente
panel serve panel_app_simple.py --port 5007

# En otra terminal
ngrok http 5007
```

## Recomendación

Para tu caso específico, recomiendo **Railway** o **Panel Cloud** porque:
- Son gratuitos
- Fáciles de configurar
- Soportan archivos grandes como tu GeoJSON
- No requieren configuración compleja
