"""Third party libraries"""
import os
import ee
import datetime
import geopandas as gpd
import folium
import streamlit as st
import geemap.colormaps as cm
import geemap.foliumap as geemap

from .rois import fire_cases

# upload etmemizi salayacak fonksiyon lazım buraya


def app():

    """
    The main app that streamlit will render for fire analysis page.
    """

    today = datetime.date.today()

    st.title("Yangın analizi")

    st.markdown(
        """
        [Sentinel-2](https://developers.google.com/earth-engine/datasets/catalog/sentinel) verilerini kullanarak orman yangınlarının incelenmesini sağlayan web aplikasyonu. 
        Bu uygulama [streamlit](https://streamlit.io), [geemap](https://geemap.org) ve [Google Earth Engine](https://earthengine.google.com) kullanılarak oluşturuldu. Daha fazla bilgi için, streamlit [blog post](https://blog.streamlit.io/creating-satellite-timelapse-with-streamlit-and-earth-engine) sayfasını ziyaret edebilirsiniz. 
    """
    )

    row1_col1, row1_col2 = st.columns([2, 1])

    if st.session_state.get("zoom_level") is None:
        st.session_state["zoom_level"] = 4

    with row1_col1:
        m = geemap.Map(
            basemap="HYBRID",
            plugin_Draw=True,
            Draw_export=True,
            locate_control=True,
            plugin_LatLngPopup=False,
        )
        m.add_basemap("ROADMAP")

    with row1_col2:

        keyword = st.text_input("Bölge arayın:", "")
        if keyword:
            locations = geemap.geocode(keyword)
            if locations is not None and len(locations) > 0:
                str_locations = [str(g)[1:-1] for g in locations]
                location = st.selectbox("Bölge seçin:", str_locations)
                loc_index = str_locations.index(location)
                selected_loc = locations[loc_index]
                lat, lng = selected_loc.lat, selected_loc.lng
                folium.Marker(location=[lat, lng], popup=location).add_to(m)
                m.set_center(lng, lat, 12)
                st.session_state["zoom_level"] = 12

        sample_roi = st.selectbox(
            "Çalışılacak roi'yi seçin veya GeoJSON dosyası yükleyin.",
            ["Uploeded GeoJSON"]
            + list(fire_cases.keys()),  # roi importu liste şeklinde buraya gelecek
            index=0,
        )

    with row1_col1:

        with st.expander(
            "Adımlar: Harita üzerinde poligon çizin -> GeoJSON olarak export edin -> Uygulumaya upload edin -> Submit tuşuna tıklayın. Demo görmek için genişlerin 👉"
        ):
            video_empty = st.empty()

        data = st.file_uploader(
            "ROI olarak kullanmak için GeoJSON dosyası ekleyin 😇👇",
            type=["geojson", "kml", "zip"],
        )

        IMAGE_COLLECTION = "COPERNICUS/S2"
        crs = "epsg:4326"  # Coordinate Reference System

        if sample_roi == "Uploaded GeoJSON":
            pass  # 366

        if sample_roi != "Uploaded GeoJSON":
            pass  # 402

        m.to_streamlit(height=400)
