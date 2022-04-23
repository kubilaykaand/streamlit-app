"""
The page for create timelapse
"""
# Standard libraries
import datetime
from datetime import date
import tempfile
import os
import uuid

# Third party libraries
import streamlit as st
import geemap.foliumap as geemap
import ee
import folium
import geopandas as gpd

# Local libraries
from . import rois
from .functions import *

CRS = "epsg:4326"  # Coordinate Reference System
DAY_WINDOW = 6
INITIAL_DATE_WINDOW = 6

def app():

    st.title("Timelapse")
    st.markdown("Belirlenmiş iki tarih arasında gif üreten sistem.")
