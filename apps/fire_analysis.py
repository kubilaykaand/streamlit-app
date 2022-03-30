"""Trird party libraries"""
import streamlit as st
import geemap.foliumap as geemap


def app():
    """
    The main app that streamlit will render for fire analysis page.
    """
    st.title("Yangın analizi")

    width = 950
    height = 600

    main_map = geemap.Map()
    main_map.to_streamlit(width, height)
