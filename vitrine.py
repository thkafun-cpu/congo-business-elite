import streamlit as st
import streamlit.components.v1 as components
import json

# --- SERVICE 1: DATA MICROSERVICE (Logique du server.ts) ---
class DataService:
    @staticmethod
    def get_businesses():
        return [
            {"id": "1", "name": "AgriCongo Solutions", "category": "Agriculture", "location": "Brazzaville", "image": "https://picsum.photos"},
            {"id": "2", "name": "Atelier Métal Pro", "category": "Petite Industrie", "location": "Pointe-Noire", "image": "https://picsum.photos"},
            {"id": "3", "name": "Élevage du Pool", "category": "Élevage", "location": "Kinkala", "image": "https://picsum.photos"},
            {"id": "4", "name": "Congo Services Plus", "category": "Services", "location": "Kinshasa", "image": "https://picsum.photos"}
        ]

    @staticmethod
    def get_news():
        return [
            {"id": "1", "title": "Forum d'Investissement 2026", "date": "25 Mars", "category": "Événements"},
            {"id": "2", "title": "Croissance Positive 4.2%", "date": "20 Mars", "category": "Économie"}
        ]

def afficher_vitrine():
    # Préparation des données pour le Frontend
    businesses = json.dumps(DataService.get_businesses())
    news = json.dumps(DataService.get_news())
    logo_url = "https://githubusercontent.com"

    # --- SERVICE 2 & 3: UI & STYLE (Fusion de App.tsx et index.css) ---
    html_code = f"""
    <div id="root"></div>
    
    <!-- Polices et Tailwind -->
    <link href="https://googleapis.com" rel="stylesheet">
    <script src="https://tailwindcss.com"></script>
    <script src="https://unpkg.com"></script>
    <script src="https://unpkg.com"></script>
    <script src="https://unpkg.com"></script>
    <script src="https://unpkg.com"></script>
    <script src="https://unpkg.com"></script>

    <style>
        :root {{ --font-serif: 'Cormorant Garamond', serif; --font-sans: 'Inter', sans-serif; }}
        .serif {{ font-family: var(--font-serif); }}
        body {{ background-color: #f0fdfa; color: #064e3b; font-family: var(--font-sans); margin: 0; }}
    </style>

    <script type="text/babel">
        const {{ motion, AnimatePresence }} = window.Motion;
        const {{ useState, useEffect }} = React;

        // --- COMPOSANT NAVBAR ---
        const Navbar = () => (
            <nav className="fixed top-0 w-full z-50 bg-white/95 backdrop-blur-md shadow-sm px-6 py-4 flex justify-between items-center">
                <div className="flex items-center gap-3">
                    <img src="{logo_url}" className="h-10 w-10 rounded-lg object-cover shadow-sm border border-amber-200" />
                    <span className="font-black text-emerald-900 tracking-tighter uppercase text-sm">Congo Business Elite</span>
                </div>
                <div className="hidden md:flex gap-8 text-[10px] font-bold uppercase tracking-widest text-emerald-800">
                    <a href="#" className="hover:text-amber-500">Accueil</a>
                    <a href="#" className="hover:text-amber-500">Annuaire</a>
                    <a href="#" className="bg-emerald-600 text-white px-5 py-2 rounded-full">Adhésion</a>
                </div>
            </nav>
        );

        // --- COMPOSANT HERO (Inspiré de votre App.tsx) ---
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
                        <div className="flex gap-4">
                            <button className="bg-amber-500 text-emerald-950 px-8 py-4 rounded-full font-bold uppercase text-xs tracking-widest hover:bg-white transition-all">
                                Explorer l'Annuaire
                            </button>
                        </div>
                    </motion.div>
                </div>
            </section>
        );

        // --- COMPOSANT MAIN APP ---
        const App = () => {{
            const businesses = {businesses};
            const news = {news};

            return (
                <div>
                    <Navbar />
                    <Hero />
                    
                    {/* Section Annuaire (Microservice Data) */}
                    <section className="py-24 max-w-7xl mx-auto px-6">
                        <h2 className="serif text-4xl text-emerald-900 mb-12">L'Élite Économique</h2>
                        <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
                            {{businesses.map(b => (
                                <div key={{b.id}} className="bg-white rounded-2xl overflow-hidden shadow-sm hover:shadow-xl transition-all border border-emerald-50">
                                    <img src={{b.image}} className="h-48 w-full object-cover" />
                                    <div className="p-5">
                                        <span className="text-[9px] font-bold text-amber-600 uppercase tracking-widest">{{b.category}}</span>
                                        <h3 className="font-bold text-emerald-900 mt-1">{{b.name}}</h3>
                                        <p className="text-xs text-slate-400 mt-2"><i className="fas fa-map-marker-alt"></i> {{b.location}}</p>
                                    </div>
                                </div>
                            ))}}
                        </div>
                    </section>
                </div>
            );
        }};

        const root = ReactDOM.createRoot(document.getElementById('root'));
        root.render(<App />);
    </script>
    """
    
    components.html(html_code, height=2000, scrolling=True)

if __name__ == "__main__":
    st.set_page_config(layout="wide")
    afficher_vitrine()
