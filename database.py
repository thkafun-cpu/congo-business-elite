import streamlit as st
from supabase import create_client, Client

class DatabaseService:
    def __init__(self):
        # Ces secrets devront être configurés dans Streamlit Cloud
        self.url = st.secrets["SUPABASE_URL"]
        self.key = st.secrets["SUPABASE_KEY"]
        self.supabase: Client = create_client(self.url, self.key)

    def inscrire_utilisateur(self, nom, prenom, email, tel):
        data = {
            "nom": nom,
            "prenom": prenom,
            "email": email,
            "telephone": tel
        }
        return self.supabase.table("utilisateurs").insert(data).execute()

    def enregistrer_entreprise(self, user_id, nom_biz, secteur, ville):
        data = {
            "user_id": user_id,
            "nom_business": nom_biz,
            "secteur": secteur,
            "ville": ville
        }
        return self.supabase.table("entreprises").insert(data).execute()
