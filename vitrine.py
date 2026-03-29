import streamlit as st
import streamlit.components.v1 as components
import json

# --- SERVICE 1: DATA MICROSERVICE ---
class DataService:
    @staticmethod
    def get_businesses():
        return

    @staticmethod
    def get_news():
        return [
            {"id": "1", "title": "Forum d'Investissement 2026", "date": "25 Mars", "category": "Événements"},
            {"id": "2", "title": "Croissance Positive 4.2%", "date": "20 Mars", "category": "Économie"}
        ]

def afficher_vitrine():
    # Préparation des données
    businesses_json = json.dumps(DataService.get_businesses())
    news_json = json.dumps(DataService.get_news())
    logo_url = "https://githubusercontent.com"

    # --- SERVICE 2 & 3: UI & STYLE ---
    # Utilisation de triple guillemets SANS le 'f' au début pour éviter les erreurs d'accolades
    # Les variables sont injectées via .replace() pour plus de sécurité
    html_code = """
    <div id="root"></div>
    
    <link href="https://googleapis.com" rel="stylesheet">
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com"></script>
    <script src="https://unpkg.com"></script>
    <script src="https://unpkg.com"></script>
    <script src="https://unpkg.com"></script>

    <style>
        :root { --font-serif: 'Cormorant Garamond', serif; --font-sans: 'Inter', sans-serif; }
        .serif { font-family: var(--font-serif); }
        body { background-color: #f0fdfa; color: #064e3b; font-family: var(--font-sans); margin: 0; }
    </style>

    <script type="text/babel">
        const { motion, AnimatePresence } = window.Motion;
        const { useState, useEffect } = React;

        const Navbar = () => (
            <nav className="fixed top-0 w-full z-50 bg-white/95 backdrop-blur-md shadow-sm px-6 py-4 flex justify-between items-center">
                <div className="flex items-center gap-3">
                    <img src="VAR_LOGO_URL" className="h-10 w-10 rounded-lg object-cover shadow-sm border border-amber-200" />
                    <span className="font-black text-emerald-900 tracking-tighter uppercase text-sm">Congo Business Elite</span>
                </div>
                <div className="hidden md:flex gap-8 text-[10px] font-bold uppercase tracking-widest text-emerald-800">
                    <a href="#" className="hover:text-amber-500">Accueil</a>
                    <a href="#" className="hover:text-amber-500">Annuaire</a>
                    <a href="#" className="bg-emerald-600 text-white px-5 py-2 rounded-full">Adhésion</a>
                </div>
            </nav>
        );

        const Hero = () => (
            <section className="relative min-h-[80vh] flex items-center pt-20 overflow-hidden bg-emerald-950">
                <div className="absolute inset-0 opacity-40">
                    <img src="https://unsplash.com" className="w-full h-full object-cover" />
                </div>
                <div className="relative z-10 max-w-7xl mx-auto px-6">
                    <motion.div initial={{ opacity: 0, y: 30 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.8 }}>
                        <h1 className="serif text-5xl md:text-8xl text-white leading-none mb-6">
                            Le salon de <br /> <span className="italic text-amber-400">l'élite congolaise</span>
                        </h1>
                        <p className="text-emerald-100/80 uppercase tracking-[0.3em] text-xs font-bold border-l-4 border-amber-500 pl-4 mb-10">
                            Par BGM - Fondation Badiata Grâce Magaly
                        </p>
                    </motion.div>
                </div>
            </section>
        );

        const App = () => {
            const businesses = VAR_BUSINESSES;

            return (
                <div>
                    <Navbar />
                    <Hero />
                    <section className="py-24 max-w-7xl mx-auto px-6">
                        <h2 className="serif text-4xl text-emerald-900 mb-12 text-center underline decoration-amber-400 underline-offset-8">L'Élite Économique</h2>
                        <div className="grid grid-cols-1 md:grid-cols-4 gap-8">
                            {businesses.map(b => (
                                <motion.div 
                                    whileHover={{ y: -10 }}
                                    key={b.id} 
                                    className="bg-white rounded-3xl overflow-hidden shadow-lg border border-emerald-50"
                                >
                                    <img src={b.image} className="h-56 w-full object-cover" />
                                    <div className="p-6">
                                        <span className="text-[10px] font-bold text-amber-600 uppercase tracking-widest">{b.category}</span>
                                        <h3 className="font-bold text-emerald-950 text-lg mt-1 tracking-tight">{b.name}</h3>
                                        <div className="flex items-center gap-2 mt-4 text-emerald-600 font-semibold text-xs uppercase">
                                            <div className="h-1 w-4 bg-amber-400 rounded-full"></div>
                                            {b.location}
                                        </div>
                                    </div>
                                </motion.div>
                            ))}
                        </div>
                    </section>
                </div>
            );
        };

        const root = ReactDOM.createRoot(document.getElementById('root'));
        root.render(<App />);
    </script>
    """
    
    # Injection sécurisée des variables dans le HTML
    html_code = html_code.replace("VAR_BUSINESSES", businesses_json)
    html_code = html_code.replace("VAR_LOGO_URL", logo_url)
    
    components.html(html_code, height=2200, scrolling=True)

if __name__ == "__main__":
    st.set_page_config(layout="wide")
    afficher_vitrine()
