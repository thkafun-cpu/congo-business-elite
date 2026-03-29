import streamlit as st
from data_service import DataService
from vitrine import afficher_vitrine

st.set_page_config(layout="wide", page_title="BGM Elite")

# Masquer l'interface Streamlit par défaut
st.markdown("<style>#MainMenu {visibility: hidden;} footer {visibility: hidden;}</style>", unsafe_allow_html=True)

# Récupération des données via le microservice
data = DataService.get_businesses()
news = DataService.get_news()

# Affichage
afficher_vitrine(data, news)
