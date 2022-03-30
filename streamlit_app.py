import streamlit as st
from streamlit_option_menu import option_menu
from apps import fire_analysis, home

st.set_page_config(page_title="Yangın Analizi", page_icon="🔥", layout="wide")


apps = {
    "home": {"title": "Home", "icon": "house"},
    "fire_analysis": {"title": "Fire Analysis", "icon": "geo-alt"},
}

titles = [app["title"] for app in apps.values()]
icons = [app["icon"] for app in apps.values()]

params = st.experimental_get_query_params()

if "page" in params:
    default_index = titles.index(params["page"][0].lower())
else:
    default_index = 0

with st.sidebar:
    selected = option_menu(
        "Main Menu",
        options=titles,
        icons=icons,
        menu_icon="list",
        default_index=default_index,
    )

    st.sidebar.title("About")
    st.sidebar.info(
        """
        This web [app](https://share.streamlit.io/bauaai/streamlit-app/main) is maintained by \\
        [Osman](https://github.com/osbm), [Efe](https://github.com/EFCK) and [Bilal](https://github.com/qimenez). 
        
        [ADD APPLICATION SUMMARY HERE]
    """
    )

for app in apps:
    if apps[app]["title"] == selected:
        eval(f"{app}.app()")
        break
