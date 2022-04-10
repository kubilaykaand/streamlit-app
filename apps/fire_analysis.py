"""
The page for fire analysis page.
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
from . import rois  # Why i am getting pylint error? code works fine.

SENTINEL = "COPERNICUS/S2"
MAP_HEIGHT = 600
CRS = "epsg:4326"  # Coordinate Reference System
rgb_vis_params = {
    "bands": ["B4", "B3", "B2"],
}

false_color_vis_params = {
    "bands": ["B8", "B4", "B3"],
}


def map_search(folium_map: geemap.Map) -> None:  # sourcery skip: use-named-expression
    """
    The function to generate the search box above the map.
    """
    keyword = st.text_input("Bölge arayın:", "")
    if keyword:
        locations = geemap.geocode(keyword)
        if locations is not None and len(locations) > 0:
            str_locations = [str(g)[1:-1] for g in locations]
            location = st.selectbox("Bölge seçin:", str_locations)
            loc_index = str_locations.index(location)
            selected_loc = locations[loc_index]
            lat, lng = selected_loc.lat, selected_loc.lng
            folium.Marker(location=[lat, lng], popup=location).add_to(folium_map)
            folium_map.set_center(lng, lat, 12)
            st.session_state["zoom_level"] = 12


@st.cache
def uploaded_file_to_gdf(data):
    """
    The function to convert uploaded file to geodataframe.
    """
    _, file_extension = os.path.splitext(data.name)
    file_id = str(uuid.uuid4())
    file_path = os.path.join(tempfile.gettempdir(), f"{file_id}{file_extension}")

    with open(file_path, "wb") as file:
        file.write(data.getbuffer())

    if not file_path.lower().endswith(".kml"):
        return gpd.read_file(file_path)

    gpd.io.file.fiona.drvsupport.supported_drivers["KML"] = "rw"
    return gpd.read_file(file_path, driver="KML")


def app():
    """
    The main app that streamlit will render for fire analysis page.
    """

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

        pre_fire = date.today() - datetime.timedelta(days=1)
        post_fire = date.today()

        if selected_roi != "Yüklenilen GeoJSON":  # rois coming from fire_cases
            st.session_state["roi"] = rois.fire_cases[selected_roi]["region"]
            pre_fire = date.fromisoformat(
                rois.fire_cases[selected_roi]["date_range"][0]
            )
            post_fire = date.fromisoformat(
                rois.fire_cases[selected_roi]["date_range"][1]
            )

        elif data:  # rois coming from users
            gdf = uploaded_file_to_gdf(data)
            st.session_state["roi"] = geemap.gdf_to_ee(gdf)

        pre_fire_date = st.date_input("Yangın başlangıç tarihi", pre_fire)
        post_fire_date = st.date_input("Yangın bitiş tarihi", post_fire)

    with col1:
        st.info(
            "Adımlar: Harita üzerinde poligon çizin -> GeoJSON olarak export edin"
            "-> Uygulamaya upload edin"
            "-> Tarih aralığı seçin."
        )

        map_search(main_map)

        if st.session_state.get("roi"):
            main_map.center_object(st.session_state["roi"])
            main_map.add_layer(st.session_state["roi"], name="ROI", opacity=0.5)


        main_map.to_streamlit(height=600)
