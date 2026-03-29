# data_service.py
class DataService:
    @staticmethod
    def obtenir_entreprises():
        # Cette liste pourra être remplacée par une base de données ou un appel API
        return [
            {
                "id": "1",
                "nom": "AgriCongo Solutions",
                "secteur": "Agriculture",
                "ville": "Brazzaville",
                "img": "https://unsplash.com"
            },
            {
                "id": "2",
                "nom": "Atelier Métal Pro",
                "secteur": "Industrie",
                "ville": "Pointe-Noire",
                "img": "https://unsplash.com"
            },
            {
                "id": "3",
                "nom": "Congo Services Plus",
                "secteur": "Services",
                "ville": "Kinshasa",
                "img": "https://unsplash.com"
            }
        ]

    @staticmethod
    def obtenir_actualites():
        return [
            {"id": "1", "titre": "Sommet de l'Élite 2026", "date": "25 Mars", "tag": "Événement"},
            {"id": "2", "titre": "Transformation Numérique PME", "date": "12 Avril", "tag": "Innovation"}
        ]

