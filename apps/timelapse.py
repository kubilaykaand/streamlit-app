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
from . import utils


def app():
    pass
