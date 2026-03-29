import streamlit as st
from langchain_groq import ChatGroq
from duckduckgo_search import DDGS

# --- FONCTION DE RECHERCHE WEB ---
def chercher_contexte_rdc(query):
    try:
        with DDGS() as ddgs:
            # Recherche ciblée sur l'actualité économique en RDC
            results = [r['body'] for r in ddgs.text(f"RDC économie business 2026 {query}", max_results=3)]
            return "\n".join(results)
    except:
        return "Données contextuelles locales non disponibles."

# --- SERVICE MS-INTELLIGENCE ---
def afficher_intelligence():
    st.markdown("<h2 style='color: #007FFF; text-align: center;'>🤖 MS-INTELLIGENCE : Expert Business RDC</h2>", unsafe_allow_html=True)
    st.info("Ce service utilise l'Intelligence Artificielle pour accompagner les PME congolaises dans leur structuration.")
    st.markdown("---")

    # Récupération sécurisée de la clé API
    GROQ_API_KEY = st.secrets.get("GROQ_API_KEY")
    if not GROQ_API_KEY:
        st.error("⚠️ Configuration requise : Clé API Groq manquante dans les Secrets Streamlit.")
        return

    # Menu des outils avec icônes
    col1, col2 = st.columns([1, 2])
    with col1:
        outil = st.radio("🛠️ Outil d'accompagnement :", [
            "⚖️ Expert Juridique OHADA", 
            "📊 Diagnostic de Maturité PME", 
            "💰 Pitch de Financement Elite"
        ])

    with col2:
        with st.form("form_ia"):
            st.markdown(f"**Action : {outil}**")
            user_input = st.text_area("Décrivez votre projet, votre problème ou vos objectifs :", height=200, placeholder="Ex: Je souhaite ouvrir une unité de transformation agricole à Lubumbashi...")
            submit = st.form_submit_button("Lancer l'Analyse Stratégique 🚀")

    if submit:
        if user_input:
            with st.spinner("🧠 L'IA de la Fondation BGM analyse les paramètres du marché congolais..."):
                try:
                    # 1. Initialisation du modèle Llama 3.3 (Dernière version)
                    llm = ChatGroq(
                        temperature=0.3, # Un peu plus bas pour plus de rigueur
                        groq_api_key=GROQ_API_KEY, 
                        model_name="llama-3.3-70b-spec-dec" 
                    )

                    # 2. Récupération du contexte frais
                    contexte = chercher_contexte_rdc(user_input)

                    # 3. Prompt de haute précision
                    prompt_system = f"""
                    Tu es l'Expert Conseil de la FONDATION BGM (Badiata Grâce Magaly). 
                    Ton rôle est de propulser l'excellence entrepreneuriale en RDC.
                    
                    MISSION ACTUELLE : {outil}
                    CONTEXTE ÉCONOMIQUE RÉEL (RDC) : {contexte}
                    DEMANDE DE L'ENTREPRENEUR : {user_input}
                    
                    DIRECTIVES DE RÉPONSE :
                    1. Ton : Professionnel, encourageant, précis et pragmatique.
                    2. Structure : 
                       - 📌 Analyse de la situation
                       - 💡 Recommandations stratégiques (adaptées à Kinshasa/Lubumbashi/Goma)
                       - ⚠️ Points de vigilance (climat des affaires, fiscalité DGI/DGRAD)
                       - 🚀 Prochaine étape concrète
                    3. Si c'est du PITCH : Utilise la méthode Hook-Problem-Solution-Market-Call to Action.
                    4. Si c'est l'OHADA : Cite les principes de sécurité juridique pour les investisseurs.
                    """

                    # 4. Exécution
                    reponse = llm.invoke(prompt_system)
                    
                    st.success("✅ Analyse terminée avec succès !")
                    
                    # Affichage élégant de la réponse
                    with st.container():
                        st.markdown("### 💎 Rapport Stratégique BGM")
                        st.markdown(reponse.content)
                        
                    # Bouton de téléchargement pro
                    st.download_button(
                        label="📥 Télécharger le rapport (Format Pro)", 
                        data=reponse.content, 
                        file_name=f"Rapport_BGM_{outil.replace(' ', '_')}.txt",
                        mime="text/plain"
                    )

                except Exception as e:
                    st.error(f"Une erreur technique est survenue : {e}")
        else:
            st.warning("Veuillez saisir des informations pour que l'IA puisse travailler.")

    # Pied de page spécifique
    st.markdown("---")
    st.caption("Note : Les analyses fournies sont des outils d'aide à la décision. Consultez toujours un expert local pour les démarches finales.")

