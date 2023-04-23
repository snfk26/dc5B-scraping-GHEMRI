from bs4 import BeautifulSoup
import pandas as pd
import requests

#bs
URL = 'https://www.scrapethissite.com/pages/simple/'

r = requests.post(URL)
soup = BeautifulSoup(r.content, "html.parser")
pays = soup.find_all('div', class_='country')

#Récup des éléments par balise de la page
for content in pays: 
    nom = content.find('h3').text
    capitale = content.find('span', class_='country-capital').text.encode('utf-8')
    pop = content.find('span', class_='country-population').text
    superficie = content.find('span', class_='country-area').text
#affichage
    print('Pays :', nom.strip())
    print('Population :', pop.strip(), 'Habitants')
    print('Superficie :', superficie, ' km2')

#Gestion du décodage en UTF-8 pour éviter le caractère b devant chaque nom de capitale
#print('Capitale: ', capitale.strip()) cette ligne fonctionne mais affiche un b du fait de l'encodage
decoded_capitale = capitale.decode('utf-8')
trimmed_capitale = decoded_capitale.strip()
print('Capitale: ', trimmed_capitale)

