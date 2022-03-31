"""
The page for fire analysis page.
"""
import random
import streamlit as st
import geemap.foliumap as geemap
import ee
import geopandas as gpd  # to change rois to geojson types

from .rois import fire_cases  # Why i am getting pylint error? code works fine.

IMAGE_COLLECTION = "COPERNICUS/S2"
MAP_WIDTH = 950
MAP_HEIGHT = 600
CRS = "epsg:4326"  # Coordinate Reference System


def app():
    """
    The main app that streamlit will render for fire analysis page.
    """
    st.title("Yangın analizi")

    main_map = geemap.Map(
        basemap="ROADMAP",
        plugin_Draw=True,
        Draw_export=True,
        locate_control=True,
        plugin_LatLngPopup=False,
    )
    name, value = random.choice(list(fire_cases.items()))

    region = gpd.GeoDataFrame(index=[0], crs=CRS, geometry=[value["region"]])
    main_map.add_gdf(region)

    st.markdown(name)
    main_map.to_streamlit(MAP_WIDTH, MAP_HEIGHT)
