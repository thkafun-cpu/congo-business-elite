import streamlit as st
import streamlit.components.v1 as components
import json

def afficher_vitrine(entreprises, actualites):
    # Transformation des données en JSON pour JavaScript
    businesses_json = json.dumps(entreprises)
    logo_url = "https://githubusercontent.com"

    # NOTE : Pas de 'f' devant les guillemets ici pour éviter la SyntaxError des f-strings
    html_code = """
    <div id="root"></div>
    <script src="https://tailwindcss.com"></script>
    <script src="https://unpkg.com"></script>
    <script src="https://unpkg.com"></script>
    <script src="https://unpkg.com"></script>

    <script type="text/babel">
        const App = () => {
            const businesses = VAR_BUSINESSES;
            return (
                <div className="min-h-screen bg-slate-50 p-6 md:p-12 font-sans">
                    <nav className="flex justify-between items-center mb-12 bg-white p-6 rounded-2xl shadow-sm border border-slate-100">
                        <div className="flex items-center gap-4">
                            <img src="VAR_LOGO_URL" className="h-12 w-12 rounded-xl object-cover" />
                            <h1 className="font-black text-emerald-900 uppercase tracking-tighter">Congo Business Elite</h1>
                        </div>
                    </nav>

                    <div className="max-w-7xl mx-auto">
                        <h2 className="text-3xl font-bold text-emerald-950 mb-8 border-l-8 border-amber-500 pl-4 uppercase tracking-widest">
                            L'Élite Économique
                        </h2>
                        
                        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
                            {businesses.map(b => (
                                <div key={b.id} className="bg-white rounded-[2rem] overflow-hidden shadow-xl border border-emerald-50 p-4 transition-transform hover:-translate-y-2">
                                    <img src={b.image} className="h-56 w-full object-cover rounded-[1.5rem] mb-6 shadow-md" />
                                    <div className="px-2 pb-4">
                                        <span className="text-[10px] font-black text-amber-600 uppercase tracking-[0.2em]">{b.category}</span>
                                        <h3 className="font-bold text-emerald-950 text-2xl mt-1">{b.name}</h3>
                                        <p className="text-slate-400 font-medium text-sm mt-3 flex items-center gap-2">
                                            <span className="h-1 w-1 bg-slate-300 rounded-full"></span> {b.location}
                                        </p>
                                    </div>
                                </div>
                            ))}
                        </div>
                    </div>
                </div>
            );
        };

        const root = ReactDOM.createRoot(document.getElementById('root'));
        root.render(<App />);
    </script>
    """
    
    # Injection sécurisée des données sans f-strings
    html_code = html_code.replace("VAR_BUSINESSES", businesses_json).replace("VAR_LOGO_URL", logo_url)
    
    components.html(html_code, height=1500, scrolling=True)
