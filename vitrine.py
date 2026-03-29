import streamlit as st
import streamlit.components.v1 as components

def afficher_vitrine():
    # Construction de l'URL brute pour le logo GitHub
    # Utilisateur: thkafun-cpu | Repo: congo-business-elite | Branche: main | Fichier: logo_bgm.jpeg
    logo_url = "https://githubusercontent.com"

    html_code = f"""
    <div id="root"></div>
    <script src="https://unpkg.com"></script>
    <script src="https://unpkg.com"></script>
    <script src="https://unpkg.com"></script>
    <script src="https://tailwindcss.com"></script>
    <link href="https://cloudflare.com" rel="stylesheet">

    <script type="text/babel">
        const {{ useState }} = React;

        const GalleryCard = ({{ img, title }}) => (
            <div className="group bg-white rounded-2xl overflow-hidden shadow-md hover:shadow-2xl transition-all duration-500 border-b-4 border-blue-600 transform hover:-translate-y-2">
                <div className="relative overflow-hidden">
                    <img src={{img}} alt={{title}} className="w-full h-64 object-cover transition-transform duration-700 group-hover:scale-110" />
                    <div className="absolute inset-0 bg-gradient-to-t from-blue-900/80 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-end p-6">
                        <span className="text-white text-xs font-bold uppercase tracking-widest border-b border-blue-400 pb-1">Impact Foundation</span>
                    </div>
                </div>
                <div className="p-6 text-center font-bold text-slate-800 uppercase tracking-widest text-xs">
                    {{title}}
                </div>
            </div>
        );

        const VitrineBGM = () => {{
            return (
                <div className="min-h-screen bg-slate-50 font-sans selection:bg-blue-100">
                    {/* Navigation */}
                    <nav className="bg-white/95 backdrop-blur-md shadow-sm p-4 sticky top-0 z-50 border-b border-slate-100">
                        <div className="max-w-6xl mx-auto flex justify-between items-center">
                            <div className="flex items-center space-x-4">
                                <div className="h-14 w-14 rounded-full flex items-center justify-center overflow-hidden border-2 border-amber-400 shadow-lg bg-slate-100">
                                    <img src="{logo_url}" alt="Logo BGM" className="h-full w-full object-cover" onerror="this.innerHTML='BGM'"/>
                                </div>
                                <div className="flex flex-col">
                                    <span className="font-black text-xl tracking-tighter text-slate-900 leading-none">CONGO <span className="text-blue-600">BUSINESS</span></span>
                                    <span className="text-[10px] uppercase tracking-[0.3em] font-bold text-slate-500 mt-1 italic">Elite Foundation</span>
                                </div>
                            </div>
                            <div className="hidden md:flex items-center space-x-8 font-bold text-[10px] uppercase tracking-[0.2em] text-slate-600">
                                <a href="#" className="hover:text-blue-600 transition-colors">Vision</a>
                                <a href="#" className="hover:text-blue-600 transition-colors">Écosystème</a>
                                <a href="#" className="bg-blue-600 text-white px-6 py-3 rounded-full hover:bg-blue-700 transition-all shadow-lg shadow-blue-200">Rejoindre l'élite</a>
                            </div>
                        </div>
                    </nav>

                    {/* Hero Section */}
                    <header className="relative bg-slate-950 py-32 px-6 overflow-hidden">
                        <div className="absolute inset-0 opacity-10 bg-[url('https://transparenttextures.com')]"></div>
                        <div className="max-w-4xl mx-auto text-center relative z-10">
                            <span className="inline-block py-1 px-4 rounded-full bg-blue-500/10 text-blue-400 text-[10px] font-black uppercase tracking-[0.3em] mb-8 border border-blue-500/20">
                                Leadership & Innovation
                            </span>
                            <h1 className="text-5xl md:text-7xl font-black text-white mb-8 leading-[1.1] tracking-tight">
                                Le digital au service du <br/>
                                <span className="text-transparent bg-clip-text bg-gradient-to-r from-blue-400 via-indigo-400 to-emerald-400">miracle congolais</span>
                            </h1>
                            <div className="h-1.5 w-24 bg-gradient-to-r from-amber-400 to-yellow-500 mx-auto rounded-full shadow-lg shadow-amber-500/20"></div>
                        </div>
                    </header>

                    {/* Vision Section */}
                    <section className="max-w-5xl mx-auto -mt-16 px-6 relative z-20">
                        <div className="bg-white p-10 md:p-20 rounded-[2.5rem] shadow-2xl border-l-[16px] border-red-600 ring-1 ring-black/5">
                            <div className="space-y-8">
                                <div className="flex items-center space-x-4 text-blue-600">
                                    <div className="h-px w-12 bg-blue-600"></div>
                                    <span className="font-black uppercase tracking-[0.3em] text-xs">Notre Vision</span>
                                </div>
                                <p className="text-xl md:text-3xl text-slate-800 leading-relaxed font-light italic text-justify">
                                    "Sous l'impulsion de <span className="text-slate-950 font-black not-italic underline decoration-amber-400 decoration-4 underline-offset-4">Madame Badiata Grâce Magaly</span>, la fondation BGM lance ce portail comme un levier de transformation radicale pour les TPE/PME en RDC."
                                </p>
                                <p className="text-slate-500 text-lg leading-relaxed max-w-3xl">
                                    Nous bâtissons un écosystème où le numérique rencontre l'entrepreneuriat local pour briser les barrières de croissance. De <strong>Kinshasa à Goma</strong>, faisons du digital le moteur d'une économie résiliente.
                                </p>
                            </div>
                        </div>
                    </section>

                    {/* Impact Section */}
                    <section className="max-w-6xl mx-auto py-32 px-6">
                        <div className="flex flex-col md:flex-row md:items-end justify-between mb-16 gap-6">
                            <div className="max-w-xl">
                                <h2 className="text-4xl font-black text-slate-900 tracking-tighter uppercase mb-4">Actions en Action</h2>
                                <p className="text-slate-500 font-medium border-l-4 border-amber-400 pl-4">Déploiement stratégique sur l'ensemble du territoire national.</p>
                            </div>
                            <div className="flex space-x-2">
                                <div className="h-3 w-3 rounded-full bg-blue-600"></div>
                                <div className="h-3 w-12 rounded-full bg-slate-200"></div>
                            </div>
                        </div>
                        <div className="grid grid-cols-1 md:grid-cols-3 gap-10">
                            <GalleryCard img="https://unsplash.com" title="Accompagnement Terrain" />
                            <GalleryCard img="https://unsplash.com" title="Atelier Digital PME" />
                            <GalleryCard img="https://unsplash.com" title="Soutien à l'Industrie" />
                        </div>
                    </section>

                    {/* Footer */}
                    <footer className="bg-slate-950 text-slate-500 py-20 px-6 text-center border-t border-slate-900">
                        <div className="max-w-4xl mx-auto">
                            <div className="flex justify-center space-x-8 mb-12">
                                <a href="#" className="hover:text-blue-400 transition-colors"><i className="fab fa-linkedin-in text-xl"></i></a>
                                <a href="#" className="hover:text-blue-400 transition-colors"><i className="fab fa-instagram text-xl"></i></a>
                                <a href="#" className="hover:text-blue-400 transition-colors"><i className="fab fa-twitter text-xl"></i></a>
                            </div>
                            <p className="text-[10px] font-black tracking-[0.5em] mb-6 uppercase text-slate-400">© 2026 Fondation BGM | Vision Badiata Grâce Magaly</p>
                            <div className="h-px w-20 bg-slate-800 mx-auto mb-6"></div>
                            <p className="text-[9px] uppercase tracking-[0.4em] font-medium">Développé avec excellence par <span className="text-white">Thierry Kafun</span></p>
                        </div>
                    </footer>
                </div>
            );
        }};

        const root = ReactDOM.createRoot(document.getElementById('root'));
        root.render(<VitrineBGM />);
    </script>
    """
    
    # Rendu avec hauteur adaptée
    components.html(html_code, height=2400, scrolling=False)

if __name__ == "__main__":
    st.set_page_config(page_title="Congo Business Elite", layout="wide")
    afficher_vitrine()
