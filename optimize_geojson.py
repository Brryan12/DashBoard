#!/usr/bin/env python3
"""
Script para optimizar el archivo GeoJSON reduciendo su tamaño
"""
import json
import os

def optimize_geojson(input_file, output_file, precision=4):
    """
    Optimiza un archivo GeoJSON reduciendo la precisión de las coordenadas
    y eliminando propiedades innecesarias
    """
    print(f"Cargando {input_file}...")
    with open(input_file, 'r') as f:
        data = json.load(f)
    
    print(f"Archivo original: {os.path.getsize(input_file) / (1024*1024):.2f} MB")
    
    def round_coordinates(coords, precision):
        """Redondea coordenadas recursivamente"""
        if isinstance(coords, list):
            if len(coords) > 0 and isinstance(coords[0], (int, float)):
                # Es una coordenada [lon, lat]
                return [round(coord, precision) for coord in coords]
            else:
                # Es una lista de coordenadas
                return [round_coordinates(coord, precision) for coord in coords]
        return coords
    
    # Optimizar cada feature
    for feature in data.get('features', []):
        # Redondear coordenadas de geometría
        if 'geometry' in feature and 'coordinates' in feature['geometry']:
            feature['geometry']['coordinates'] = round_coordinates(
                feature['geometry']['coordinates'], precision
            )
        
        # Mantener solo propiedades esenciales
        if 'properties' in feature:
            # Puedes ajustar esto según qué propiedades necesites
            essential_props = {}
            for key, value in feature['properties'].items():
                # Mantener solo propiedades que no sean None y que sean útiles
                if value is not None and key.lower() not in ['objectid', 'shape_leng', 'shape_area']:
                    essential_props[key] = value
            feature['properties'] = essential_props
    
    # Guardar archivo optimizado
    print(f"Guardando archivo optimizado en {output_file}...")
    with open(output_file, 'w') as f:
        json.dump(data, f, separators=(',', ':'))  # Sin espacios para reducir tamaño
    
    print(f"Archivo optimizado: {os.path.getsize(output_file) / (1024*1024):.2f} MB")
    reduction = (1 - os.path.getsize(output_file) / os.path.getsize(input_file)) * 100
    print(f"Reducción de tamaño: {reduction:.1f}%")

if __name__ == "__main__":
    input_file = "Data/cober_arborea_2021_dissolve_4326.geojson"
    output_file = "Data/cober_arborea_2021_optimized.geojson"
    
    if os.path.exists(input_file):
        optimize_geojson(input_file, output_file, precision=3)
        print("\n¡Optimización completada!")
        print(f"Usa el archivo optimizado: {output_file}")
    else:
        print(f"Error: No se encontró el archivo {input_file}")
