"""
The page for fire analysis page.
"""
from io import StringIO
import datetime
from datetime import date

import streamlit as st
import geemap.colormaps as cm
import geemap.foliumap as geemap
import ee
import geopandas as gpd  # to change rois to geojson types
import folium


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

    st.markdown(
        """
        [Sentinel-2](https://developers.google.com/earth-engine/datasets/catalog/sentinel)
        verilerini kullanarak orman yangınlarının incelenmesini sağlayan web aplikasyonu.
        Bu uygulama [streamlit](https://streamlit.io), [geemap](https://geemap.org) ve
        [Google Earth Engine](https://earthengine.google.com) kullanılarak oluşturuldu.
        Daha fazla bilgi için, streamlit
        [blog post](https://blog.streamlit.io/creating-satellite-timelapse-with-streamlit-and-earth-engine)
        sayfasını ziyaret edebilirsiniz.
    """
    )

    row1_col1, row1_col2 = st.columns([2, 1])

    if st.session_state.get("zoom_level") is None:
        st.session_state["zoom_level"] = 4

    main_map = geemap.Map(
        basemap="HYBRID",
        plugin_Draw=True,
        Draw_export=True,
        locate_control=True,
        plugin_LatLngPopup=False,
    )
    main_map.add_basemap("ROADMAP")

    with row1_col1:
        st.info(
            "Adımlar: Harita üzerinde poligon çizin -> GeoJSON olarak export edin"
            "-> Uygulumaya upload edin"
            "-> Submit tuşuna tıklayın."
        )

        keyword = st.text_input("Bölge arayın:", "")
        if keyword:
            locations = geemap.geocode(keyword)
            if locations is not None and len(locations) > 0:
                str_locations = [str(g)[1:-1] for g in locations]
                location = st.selectbox("Bölge seçin:", str_locations)
                loc_index = str_locations.index(location)
                selected_loc = locations[loc_index]
                lat, lng = selected_loc.lat, selected_loc.lng
                folium.Marker(location=[lat, lng], popup=location).add_to(main_map)
                main_map.set_center(lng, lat, 12)
                st.session_state["zoom_level"] = 12

        main_map.to_streamlit(height=400)

    with row1_col2:
        data = st.file_uploader(
            "ROI olarak kullanmak için GeoJSON dosyası ekleyin 😇👇",
            type=["geojson", "kml", "zip"],
        )
        # print(data)
        selected_roi = st.selectbox(
            "Çalışılacak roi'yi seçin veya GeoJSON dosyası yükleyin.",
            ["Yüklenilen GeoJSON"]
            + list(fire_cases.keys()),  # roi importu liste şeklinde buraya gelecek
            index=0,
        )

        geometry = None
        if selected_roi == "Yüklenilen GeoJSON":
            pre_fire_date = st.date_input(
                "Yangın başlangıç tarihi", date.today() - datetime.timedelta(days=1)
            )

            post_fire_date = st.date_input("Yangın bitiş tarihi", date.today())
            if data:
                geojson = StringIO(data.getvalue().decode("utf-8"))
                geometry = ee.Geometry(geojson)

        else:
            geometry = fire_cases[selected_roi]["region"]
            pre_fire_date = fire_cases[selected_roi]["date_range"][0]
            post_fire_date = fire_cases[selected_roi]["date_range"][1]

    # now we have geometry and dates
    # also we need the geometry as ee.Geometry
    if selected_roi == "Yüklenilen GeoJSON":  # rois coming from the user
        # raise NotImplemented
        pass
    else:  # rois coming from fire_cases
        # raise NotImplemented
        pass

    print(geometry, pre_fire_date, post_fire_date)
    image_collection = ee.ImageCollection(IMAGE_COLLECTION)
