"""
Home page
"""
import streamlit as st


def app():
    """
    Main app that streamlit will render.
    """
    st.title("Uzaktan Algılama Verilerine Dayalı Orman Tahribatı İzleme Sistemi")

    st.markdown(
        """
        Bu web aplikasyonu [streamlit](https://streamlit.io) kullanılarak orman tarhibatının izlenmesi ve analiz edilebilmesi için TEMA işbirliğiyle, 
        [google earth engine](https://earthengine.google.com) verilerini esas alarak yapılmıştır. Çalışmada [leafmap](https://leafmap.org), 
        [geemap](https://geemap.org) gibi açık kaynak haritalama kütüphaneleri kullanılmıştır.
        """
    )

    st.subheader("Örnek Analizler")
    st.markdown(
        """
        Alt taraftaki çalışmalar Yangın Analizi web sayfası kullanılarak yapıldı. 
        Kendi Çalışmalarınızı yaratmak için sol taraftaki menüden `Yangın Analizi` 
        sekmesine tıklayınız.
    """
    )

    row1_col1, row1_col2 = st.columns(2)
    with row1_col1:
        st.image("https://github.com/bauaai/streamlit-app/blob/29-ana-sayfa-düzenlenilmeli/assets/yangın_öncesi_rgb.png")
        st.image("https://github.com/bauaai/streamlit-app/blob/29-ana-sayfa-düzenlenilmeli/assets/yangın_sonrası_rgb.png")


    with row1_col2:
        st.image("https://github.com/giswqs/data/raw/main/timelapse/goes.gif")
        st.image("https://github.com/bauaai/streamlit-app/blob/29-ana-sayfa-düzenlenilmeli/assets/lejant.png")