You can access the project via [this link](https://share.streamlit.io/bauaai/streamlit-app/main)

The new streamlit badge [![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/bauaai/streamlit-app/main)


[Icons](https://icons.getbootstrap.com/)


#### Steps to create open the app locally

>You need the python 3.6 or higher version to run the app locally.

1. Clone the repository
```bash
git clone https://github.com/bauaai/streamlit-app.git
cd streamlit-app
```

2. Create a virtual environment (optional)
    1. on linux
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```
    2. on windows
    ```bash
    python -m venv .venv
    .venv\Scripts\activate.bat
    ```
3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run the app
```bash
python -m streamlit run streamlit_app.py
```
