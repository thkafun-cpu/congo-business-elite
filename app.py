import streamlit as st
from data_service import DataService
from vitrine import afficher_vitrine

# Configuration de la page Streamlit (Microservice de Configuration)
def configurer_application():
    st.set_page_config(
        page_title="Congo Business Elite | Fondation BGM",
        page_icon="🇨🇩",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    # Suppression des éléments par défaut de Streamlit pour un look "Elite" pur
    st.markdown("""
        <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            .block-container {padding-top: 0rem; padding-bottom: 0rem; padding-left: 0rem; padding-right: 0rem;}
        </style>
    """, unsafe_allow_html=True)

def main():
    # 1. Initialisation de la configuration
    configurer_application()

    # 2. Appel au Microservice de Données
    # On récupère les data ici pour pouvoir les passer à la vitrine si besoin
    entreprises = DataService.obtenir_entreprises()
    actualites = DataService.obtenir_actualites()

    # 3. Lancement du Microservice d'Interface (Frontend)
    # Note : On peut passer les listes 'entreprises' et 'actualites' en paramètres 
    # pour que l'affichage soit toujours synchronisé avec les données.
    afficher_vitrine(entreprises, actualites)

if __name__ == "__main__":
    main()
