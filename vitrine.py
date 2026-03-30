import streamlit as st
import streamlit.components.v1 as components

def afficher_navigation():
    """Barre de navigation latérale style Dashboard Elite"""
    st.sidebar.image("https://githubusercontent.com", width=100)
    st.sidebar.title("BGM Elite")
    st.sidebar.markdown("---")
    
    menu = st.sidebar.radio(
        "Navigation",
        ["🏠 Accueil & Vision", "🏭 L'Usine à Business (IA)", "marketplace Annuaire PME", "📅 Événements & Blog"],
        index=0
    )
    
    st.sidebar.markdown("---")
    st.sidebar.info("🚀 **Mode Basse Bande Passante** activé par défaut pour la RDC.")
    
    return menu

def rendu_accueil():
    """Service Vitrine : Branding & Vision"""
    html_hero = """
    <script src="https://tailwindcss.com"></script>
    <div class="bg-emerald-950 p-10 rounded-3xl text-white mb-10 border-l-8 border-amber-500 shadow-2xl">
        <span class="text-amber-400 font-bold uppercase tracking-widest text-xs">Vision RDC 2030</span>
        <h1 class="text-4xl md:text-6xl font-black mt-4 leading-tight">Congo Business Elite</h1>
        <p className="text-emerald-100/80 mt-6 text-lg italic">
            "Le numérique au service du miracle économique congolais." 
            <br>— <b>Badiata Grâce Magaly (BGM)</b>
        </p>
    </div>
    """
    components.html(html_hero, height=350)
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🎯 Notre Mission")
        st.write("Connecter les leaders des TPE/PME au marché africain via l'IA et l'automatisation.")
    with col2:
        st.subheader("📊 Impact en Direct")
        st.metric(label="PME Accompagnées", value="124", delta="+12 ce mois")

def rendu_usine_ia():
    """Service Intelligence : Outils IA"""
    st.title("🏭 L'Usine à Business")
    st.caption("Outils d'IA générative pour booster votre structure.")
    
    tab1, tab2, tab3 = st.tabs(["⚖️ Assistant OHADA", "📝 Générateur de Pitch", "🔍 Diagnostic Digital"])
    
    with tab1:
        st.info("Posez vos questions juridiques sur la création d'entreprise en RDC.")
        # Ici on appellera le futur Microservice Intelligence
        st.text_input("Votre question (ex: Quel statut pour une SARL ?)")
        
    with tab2:
        st.write("Structurez votre recherche de financement en 2 minutes.")
        st.button("Générer mon Pitch")

def rendu_annuaire():
    """Service Marketplace : Visibilité"""
    st.title("🤝 Marketplace de Visibilité")
    st.write("Faites la promotion de votre savoir-faire.")
    # Logique de récupération des données Supabase à venir
    st.warning("Connectez-vous à Supabase pour voir l'annuaire dynamique.")

def afficher_vitrine():
    """Point d'entrée principal du service Vitrine"""
    choix = afficher_navigation()
    
    if choix == "🏠 Accueil & Vision":
        rendu_accueil()
    elif choix == "🏭 L'Usine à Business (IA)":
        rendu_usine_ia()
    elif choix == "marketplace Annuaire PME":
        rendu_annuaire()
    else:
        st.title("📅 Événements & Blog")
        st.write("Contenu en cours de rédaction...")

if __name__ == "__main__":
    afficher_vitrine()
