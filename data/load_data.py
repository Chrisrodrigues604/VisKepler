from os import listdir
import os
from os.path import isfile, join
import geopandas as gpd

def read_geojsons(directory):
    geojsons = {}
    for geojson_file in os.listdir(directory):
        if geojson_file.endswith('.geojson'):
            file_path = os.path.join(directory, geojson_file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    geojsons[geojson_file] = gpd.read_file(f)
            except UnicodeDecodeError as e:
                print(f"Error decoding file {file_path}: {e}")
            except Exception as e:
                print(f"Error reading file {file_path}: {e}")
    return geojsons