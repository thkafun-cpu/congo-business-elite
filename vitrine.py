import streamlit as st
import streamlit.components.v1 as components
import json

def afficher_vitrine(entreprises, actualites):
    businesses_json = json.dumps(entreprises)
    logo_url = "https://githubusercontent.com"

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
                <div className="min-h-screen bg-slate-50 p-10 font-sans">
                    <nav className="flex justify-between items-center mb-20 bg-white p-6 rounded-2xl shadow-sm">
                        <div className="flex items-center gap-4">
                            <img src="VAR_LOGO_URL" className="h-12 w-12 rounded-lg" />
                            <h1 className="font-black text-emerald-900 uppercase">Congo Business Elite</h1>
                        </div>
                    </nav>
                    <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
                        {businesses.map(b => (
                            <div key={b.id} className="bg-white rounded-3xl overflow-hidden shadow-lg border border-emerald-50 p-4">
                                <img src={b.image} className="h-48 w-full object-cover rounded-2xl mb-4" />
                                <h3 className="font-bold text-emerald-950 text-xl">{b.name}</h3>
                                <p className="text-amber-600 font-bold text-xs uppercase mt-2">{b.category} • {b.location}</p>
                            </div>
                        ))}
                    </div>
                </div>
            );
        };
        const root = ReactDOM.createRoot(document.getElementById('root'));
        root.render(<App />);
    </script>
    """
    html_code = html_code.replace("VAR_BUSINESSES", businesses_json).replace("VAR_LOGO_URL", logo_url)
    components.html(html_code, height=1200, scrolling=True)
