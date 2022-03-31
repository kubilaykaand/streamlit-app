"""
Home page
"""
import streamlit as st


def app():
    """
    Main app that streamlit will render.
    """
    st.title("TEMA işbirliği ile yapıldı")

    st.markdown(
        r"""
        ## BAU AAI - TEMA işbirliği ile oluşturulmuş bir script bu

        BLA, *BLA*, **BLA**
        $$\text{Is latex working} = \frac{\text{test}}{\text{denemesi}}$$
        ## Merhabalar streamlit markdown latex destekliyormuş.
        Ve buraya eklenilecek gifleri ve resimleri tasarımın son aşamasına
        bırakalım diyorum ama isteyen vakti olduğu zaman yapabilir.
        """
    )
