import requests
url = "https://v3-cinemeta.strem.io/catalog/movie/top.json"
def recuperer_films():
    try:
        reponse = requests.get(url,timeout=10)
    except requests.exceptions.RequestException:
        print("pas de connexion au réseau.")
        return[]
    if reponse.status_code == 200:
        data = reponse.json()
        if "metas" in data:
            films_api  = data["metas"]
            films = []
            for film in films_api:
                element = {
                    "id": film.get("id")
                    "titre": film.get("name")
                    "annee": film.get("releaseInfo")
                    "genre": film.get("genres")
                    "resume": film.get("description")
                    "notes": film.get("poster")

                }
                films.append(element)
            return films
        else:
            print("aucun catalogue trouvé")
            return []
    else:
        print("erreur serveur:"reponse.statuts_code)
        return []
if __name___ =="__main__":
    resultats=recuperer_films()
    for film in resultats:
        print("Titre:",film["titre"])
        print("Année:",film["année"])
        print("Genre:",film["genre"])
        print("Résumé:",film["note"])
       print("Titre:",film["titre"])
       print("Affiche:",film["affiche"])
       print("_"*40)
