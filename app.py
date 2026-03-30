import streamlit as st
import streamlit.components.v1 as components

# 1. CONFIGURATION DE LA PAGE (Style Studio)
st.set_page_config(
    page_title="BGM Elite | AI Studio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. DESIGN PERSONNALISÉ (STYLE GOOGLE AI STUDIO)
st.markdown("""
    <style>
    /* Global Background */
    .stApp {
        background-color: #F8F9FA;
    }
    
    /* Sidebar Style */
    [data-testid="stSidebar"] {
        background-color: #FFFFFF;
        border-right: 1px solid #E0E0E0;
    }
    
    /* Titres et polices */
    h1, h2, h3 {
        color: #202124;
        font-family: 'Google Sans', sans-serif;
    }

    /* Style des onglets (Tabs) comme dans Studio */
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
        background-color: transparent;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        background-color: transparent;
        border-bottom: 2px solid transparent;
        color: #5F6368;
        font-weight: 500;
    }
    .stTabs [aria-selected="true"] {
        border-bottom: 2px solid #1A73E8 !important;
        color: #1A73E8 !important;
    }

    /* Style des boutons (Primary Google Blue) */
    div.stButton > button:first-child {
        background-color: #1A73E8;
        color: white;
        border-radius: 4px;
        border: none;
        padding: 10px 24px;
        font-weight: 500;
        transition: 0.3s;
    }
    div.stButton > button:hover {
        background-color: #1765CC;
        box-shadow: 0 1px 3px rgba(60,64,67,0.3);
    }

    /* Zone d'entrée de texte */
    .stTextInput > div > div > input {
        border-radius: 8px;
        border: 1px solid #DADCE0;
        background-color: white;
    }
    </style>
    """, unsafe_allow_html=True)

def afficher_navigation():
    """Barre de navigation latérale style Studio"""
    with st.sidebar:
        st.image("https://gstatic.com", width=50) # Icône type Studio
        st.title("BGM Elite")
        st.caption("AI Management System")
        st.markdown("---")
        
        menu = st.radio(
            "WORKSPACE",
            ["🏠 Accueil & Vision", "🏭 L'Usine à Business (IA)", "🤝 Marketplace Annuaire", "📅 Événements & Blog"],
            index=0
        )
        
        st.markdown("---")
        with st.expander("⚙️ Paramètres IA"):
            st.slider("Température", 0.0, 1.0, 0.7)
            st.selectbox("Modèle", ["Gemini 1.5 Pro", "Gemini 1.5 Flash"])
        
        st.info("🚀 **Mode RDC** optimisé.")
    
    return menu

def rendu_accueil():
    """Service Vitrine avec Hero Section modernisée"""
    html_hero = """
    <script src="https://tailwindcss.com"></script>
    <div class="bg-white p-8 rounded-xl border border-gray-200 shadow-sm mb-8">
        <div class="flex items-center gap-4 mb-4">
            <span class="bg-blue-100 text-blue-700 px-3 py-1 rounded-full text-xs font-bold uppercase">Vision RDC 2030</span>
        </div>
        <h1 class="text-3xl md:text-5xl font-bold text-gray-900 leading-tight">Congo Business Elite</h1>
        <p class="text-gray-600 mt-4 text-lg max-w-2xl">
            "Le numérique au service du miracle économique congolais." 
            <br><span class="text-blue-600 font-semibold">— Badiata Grâce Magaly (BGM)</span>
        </p>
    </div>
    """
    components.html(html_hero, height=280)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="PME Accompagnées", value="124", delta="+12")
    with col2:
        st.metric(label="Projets IA", value="18", delta="Nouveau")
    with col3:
        st.metric(label="Régions RDC", value="6", delta="Stable")

def rendu_usine_ia():
    """L'interface de travail (The Playground)"""
    st.markdown("### 🏭 L'Usine à Business")
    st.write("Sélectionnez un outil pour commencer à générer du contenu.")
    
    tab1, tab2, tab3 = st.tabs(["⚖️ Assistant OHADA", "📝 Générateur de Pitch", "🔍 Diagnostic Digital"])
    
    with tab1:
        st.markdown("#### Assistant Juridique OHADA")
        query = st.text_input("Posez votre question sur la création d'entreprise...", placeholder="Ex: Quelles conditions pour une succursale ?")
        if query:
            st.write("🔍 *Analyse du référentiel OHADA en cours...*")
        
    with tab2:
        st.markdown("#### Structureur de Pitch")
        colA, colB = st.columns(2)
        with colA:
            nom = st.text_input("Nom du projet")
            secteur = st.selectbox("Secteur", ["Agrobusiness", "Tech", "Mines", "Services"])
        with colB:
            description = st.text_area("Description courte")
        
        if st.button("✨ Générer mon Pitch"):
            st.success("Pitch généré avec succès (Simulé)")

def rendu_annuaire():
    st.markdown("### 🤝 Marketplace de Visibilité")
    st.info("Recherchez des partenaires certifiés BGM Elite.")
    st.text_input("🔍 Rechercher une PME (ex: Kinshasa, Transport...)")
    st.warning("⚠️ Connexion Supabase requise pour les données réelles.")

def afficher_vitrine():
    choix = afficher_navigation()
    
    # Conteneur principal pour centrer le contenu comme dans Studio
    main_container = st.container()
    
    with main_container:
        if choix == "🏠 Accueil & Vision":
            rendu_accueil()
        elif choix == "🏭 L'Usine à Business (IA)":
            rendu_usine_ia()
        elif choix == "🤝 Marketplace Annuaire":
            rendu_annuaire()
        else:
            st.title("📅 Événements & Blog")
            st.write("Prochains webinaires sur l'IA en RDC...")

if __name__ == "__main__":
    afficher_vitrine()
