import streamlit as st
import streamlit.components.v1 as components

def afficher_vitrine():
    # Intégration de React et Tailwind CSS pour un rendu "Elite"
    # Note: Le logo utilise un placeholder, remplacez-le par votre lien GitHub direct
    
    html_code = """
    <div id="root"></div>
    <script src="https://unpkg.com"></script>
    <script src="https://unpkg.com"></script>
    <script src="https://unpkg.com"></script>
    <script src="https://tailwindcss.com"></script>

    <script type="text/babel">
        const { useState } = React;

        const GalleryCard = ({ img, title }) => (
            <div className="bg-white rounded-xl overflow-hidden shadow-lg hover:shadow-2xl transition-shadow duration-300 border-b-4 border-blue-600">
                <img src={img} alt={title} className="w-full h-56 object-cover" />
                <div className="p-4 text-center font-bold text-blue-800 uppercase tracking-wide text-sm">
                    {title}
                </div>
            </div>
        );

        const VitrineBGM = () => {
            return (
                <div className="min-h-screen bg-slate-50 font-sans">
                    {/* Header avec Logo BGM */}
                    <nav className="bg-white shadow-md p-4 sticky top-0 z-50">
                        <div className="max-w-6xl mx-auto flex justify-between items-center">
                            <div className="flex items-center space-x-3">
                                {/* REMPLACER LE LIEN CI-DESSOUS PAR VOTRE IMAGE GITHUB */}
                                <div className="h-16 w-16 bg-slate-900 rounded-full flex items-center justify-center overflow-hidden border-2 border-yellow-500">
                                    <span className="text-yellow-500 font-bold text-xs">LOGO BGM</span>
                                </div>
                                <span className="font-black text-xl tracking-tighter text-slate-800">CONGO <span className="text-blue-600">BUSINESS</span> ELITE</span>
                            </div>
                            <div className="hidden md:flex space-x-6 font-medium text-slate-600">
                                <a href="#" className="hover:text-blue-600">Accueil</a>
                                <a href="#" className="hover:text-blue-600">Vision</a>
                                <a href="#" className="bg-blue-600 text-white px-4 py-2 rounded-lg">Rejoindre</a>
                            </div>
                        </div>
                    </nav>

                    {/* Hero Section */}
                    <header className="relative bg-slate-900 py-24 px-6 overflow-hidden">
                        <div className="absolute inset-0 opacity-20 bg-[url('https://transparenttextures.com')]"></div>
                        <div className="max-w-4xl mx-auto text-center relative z-10">
                            <h1 className="text-4xl md:text-6xl font-extrabold text-white mb-6 leading-tight">
                                Le numérique au service du <span className="text-blue-400">miracle économique</span> congolais
                            </h1>
                            <div className="h-2 w-32 bg-yellow-400 mx-auto rounded-full"></div>
                        </div>
                    </header>

                    {/* Vision Section */}
                    <section className="max-w-4xl mx-auto -mt-12 px-6 relative z-20">
                        <div className="bg-white p-8 md:p-12 rounded-2xl shadow-2xl border-l-[12px] border-red-600">
                            <p className="text-lg md:text-xl text-slate-700 leading-relaxed text-justify">
                                Sous l'impulsion de <span className="text-blue-600 font-bold">Madame Badiata Grâce Magaly (BGM)</span>, la <strong>fondation BGM</strong> lance ce portail comme un levier de transformation pour les TPE/PME en RDC. 
                                <br/><br/>
                                Notre vision dépasse la simple information. Nous voulons bâtir un écosystème où le numérique rencontre l'entrepreneuriat local pour briser les barrières de croissance. De <strong>Kinshasa à Goma</strong>, faisons du digital le moteur d'une économie résiliente.
                            </p>
                        </div>
                    </section>

                    {/* Galerie Section */}
                    <section className="max-w-6xl mx-auto py-20 px-6">
                        <h2 className="text-3xl font-bold text-center text-slate-800 mb-12 uppercase tracking-widest">
                            La Fondation BGM en Action
                        </h2>
                        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
                            <GalleryCard img="https://unsplash.com" title="Accompagnement Terrain" />
                            <GalleryCard img="https://unsplash.com" title="Atelier Digital PME" />
                            <GalleryCard img="https://unsplash.com" title="Soutien à l'Industrie" />
                        </div>
                    </section>

                    {/* Footer */}
                    <footer className="bg-slate-900 text-slate-400 py-12 px-6 text-center border-t-4 border-yellow-500">
                        <p className="mb-2">© 2026 Fondation BGM | Vision Badiata Grâce Magaly</p>
                        <p className="text-xs uppercase tracking-widest">Développé avec excellence par <span className="text-white">Thierry Kafun</span></p>
                    </footer>
                </div>
            );
        };

        const root = ReactDOM.createRoot(document.getElementById('root'));
        root.render(<VitrineBGM />);
    </script>
    """
    
    # Rendu du composant avec une hauteur ajustée pour le nouveau design
    components.html(html_code, height=1800, scrolling=True)

