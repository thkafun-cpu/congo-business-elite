import streamlit as st

# --- CONFIGURATION GLOBALE ---
# Utilisation du drapeau RDC correct (CD) et layout large
st.set_page_config(
    page_title="Congo Business Elite - Fondation BGM", 
    page_icon="🇨🇩", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- STYLE CSS PERSONNALISÉ POUR LA SIDEBAR ---
st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            background-color: #001f3f; /* Bleu nuit pour le côté Elite */
            color: white;
        }
        [data-testid="stSidebar"] .stRadio > label {
            color: #F7D618 !important; /* Jaune or pour les titres */
            font-weight: bold;
        }
        .st-emotion-cache-16idsys p {
            color: #ffffff;
        }
    </style>
""", unsafe_allow_html=True)

# --- IMPORTATION SÉCURISÉE DES MICROSERVICES ---
try:
    from vitrine import afficher_vitrine
    from intelligence import afficher_intelligence
except ImportError as e:
    st.error(f"❌ Erreur de structure : {e}")
    st.warning("⚠️ Vérifiez que 'vitrine.py' et 'intelligence.py' sont bien présents dans votre dépôt GitHub.")
    st.stop()

# --- BARRE LATÉRALE (NAVIGATION & BRANDING) ---

# 1. Affichage du Logo (Utilisez votre lien direct ici)
# Si vous avez l'image en local, remplacez par : st.sidebar.image("logo.jpg")
st.sidebar.markdown("<h2 style='text-align: center; color: #F7D618;'>BGM</h2>", unsafe_allow_html=True)
st.sidebar.image(
    "https://githubusercontent.com", # À REMPLACER PAR VOTRE LIEN RÉEL
    caption="Elite Business Portal",
    use_container_width=True
)

st.sidebar.title("💎 Navigation")
st.sidebar.markdown("---")

# Menu de navigation amélioré
page = st.sidebar.radio(
    "MENU PRINCIPAL", 
    [
        "🏠 Accueil & Vision", 
        "🤖 Intelligence Artificielle", 
        "🤝 Accompagnement (Data)"
    ],
    index=0
)

# --- ROUTAGE DES PAGES ---

if page == "🏠 Accueil & Vision":
    try:
        # Affiche la nouvelle vitrine React/Tailwind
        afficher_vitrine()
    except Exception as e:
        st.error(f"Erreur d'affichage : {e}")

elif page == "🤖 Intelligence Artificielle":
    st.markdown("<h1 style='color: #007FFF;'>🤖 Assistant IA BGM</h1>", unsafe_allow_html=True)
    try:
        afficher_intelligence()
    except Exception as e:
        st.error(f"Le service Intelligence est indisponible : {e}")

elif page == "🤝 Accompagnement (Data)":
    st.title("🤝 Accompagnement Stratégique")
    st.subheader("Phase de déploiement 3")
    
    col1, col2 = st.columns(2)
    with col1:
        st.info("Ce module permettra la mise en relation directe entre PME et investisseurs.")
        st.write("✅ Audit de maturité numérique")
        st.write("✅ Base de données des TPE/PME")
        st.write("✅ Visibilité publicitaire")
    with col2:
        st.image("https://unsplash.com", caption="Collaboration & Croissance")

# --- PIED DE PAGE (SIDEBAR) ---
st.sidebar.markdown("---")
st.sidebar.info(
    "📍 **Fondation BGM**\n\n"
    "Visionnaire : **Badiata Grâce Magaly**\n\n"
    "Développeur : **Thierry Kafun**"
)
st.sidebar.caption("© 2026 | Congo Business Elite")

