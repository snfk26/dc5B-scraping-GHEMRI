from bs4 import BeautifulSoup
import requests
import pandas as pd

# Changez cette variable en fonction de votre recherche
search_term = "plombier"
location = "paris"
page_num = 2

# Créez l'URL de recherche
url = f"https://www.pagesjaunes.fr/annuaire/paris-75/electricien"

# Envoyer une requête GET pour récupérer le contenu de la page
response = requests.get(url)

# Analysez le contenu HTML avec BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Trouvez les éléments contenant les informations souhaitées (par exemple, le nom et l'adresse)
results = soup.find_all("section", class_="bi-bloc blocs clearfix")

# Créez un DataFrame pour stocker les résultats
data = []

for result in results:
    try:
        name = result.find("a", class_="denomination-links").get_text(strip=True)
    except AttributeError:
        name = None

    try:
        address = result.find("div", class_="adresse").get_text(strip=True)
    except AttributeError:
        address = None

    data.append({"name": name, "address": address})

df = pd.DataFrame(data)

# Exportez le DataFrame au format CSV
df.to_csv("pages_jaunes_reslts.csv", index=None, header=True)