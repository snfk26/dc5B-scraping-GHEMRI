from bs4 import BeautifulSoup
import pandas as pd
import requests

#Numéro de page plus extraction 

def npage(page_num):
    URL = 'https://www.scrapethissite.com/pages/forms/?page_num='
    session = requests.Session()
   
    r = session.get(URL + str(page_num))
    soup = BeautifulSoup(r.text, "html.parser")
    scrap = soup.find_all('table')[0]
    df = pd.read_html(str(scrap), header=0)[0]

    return df

#Fusion des dataframe
dtable = []
for page_num in range(1, 10):
    df_fi = npage(page_num)
    dtable.append(df_fi)
    df_fusion = pd.concat(dtable, ignore_index=True)
    pd.DataFrame(df_fusion, columns=['Team Name', 'Win %', 'Losses', 'Goals For (GF)','Goals Against (GA)', '+ / -'])


Dif = "+ / -"
Encaisse = 'Goals Against (GA)'

#Conversion en numérique avant filtrage
df_fusion[Dif] = pd.to_numeric(df_fusion[Dif], errors='coerce')
df_fusion[Encaisse] = pd.to_numeric(df_fusion[Encaisse], errors='coerce')

#Filtrage
filtered_df = df_fusion[(df_fusion[Dif] > 0) & (df_fusion[Encaisse] < 300)]
#Export en csv
filtered_df.to_csv(r"teams.csv", index=None, header=True)

