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
from . import rois, satellite_params, functions

CRS = "epsg:4326"  # Coordinate Reference System
DAY_WINDOW = 6
INITIAL_DATE_WINDOW = 6


def app():

    st.title("Timelapse")
    st.markdown("Belirlenmiş iki tarih arasında gif üreten sistem.")

    col1, col2 = st.columns([2, 1])

    if st.session_state.get("zoom_level") is None:
        st.session_state["zoom_level"] = 4

    main_map = geemap.Map(
        basemap="ROADMAP",
        plugin_Draw=True,
        Draw_export=True,
        locate_control=True,
        plugin_LatLngPopup=False,
    )

    with col2:
        data = st.file_uploader(
            "ROI olarak kullanmak için GeoJSON dosyası ekleyin 😇👇",
            type=["geojson", "kml", "zip"],
        )

        selected_roi = st.selectbox(
            "Çalışılacak roi'yi seçin veya GeoJSON dosyası yükleyin.",
            ["Yüklenilen GeoJSON"] + list(rois.fire_cases.keys()),
            index=0,
        )

        if selected_roi != "Yüklenilen GeoJSON":  # rois coming from fire_cases
            st.session_state["roi"] = rois.fire_cases[selected_roi]["region"]

        elif data:  # rois coming from users
            gdf = uploaded_file_to_gdf(data)
            st.session_state["roi"] = geemap.gdf_to_ee(gdf)

        selected_satellite = st.selectbox(
            "Çalışılacak uyduyu seçin", list(satellite_params.satellite.keys())
        )

        if selected_satellite == "sentinel-2":
            st.session_state["satellite"] = satellite_params.satellite["sentinel-2"]

        elif selected_satellite == "landsat-8":
            st.session_state["satellite"] = satellite_params.satellite["landsat-8"]

        selected_rgb = st.selectbox(
            "Görüntülenme rengini seçin", ["True Color", "False Color", "dNBR"]
        )

        if selected_rgb == "True Color":
            st.session_state["vis_params"] = "True Color"

        elif selected_rgb == "False Color":
            st.session_state["vis_params"] = "False Color"

        elif selected_rgb == "dNBR":
            st.session_state["vis_params"] = "dNBR"

        slider_date = st.slider(
            "Tarih Aralığı",
            value=[st.session_state["satellite"]["launch"], date.today()],
        )

        slider_fps = st.slider("FPS", min_value=1, max_value=60)

        the_button = st.button("Submit")

        if the_button:
            pass

        pre_fire = date.today() - datetime.timedelta(days=INITIAL_DATE_WINDOW)
        post_fire = date.today()
