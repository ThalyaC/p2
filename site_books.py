"""
Projet 2 Phase 3
1. Interroger le site "Books to scrappe"; 
2. Récupérer toutes les catégories ;
3. Créer un fichier csv contenant tous les livres.
"""


import requests
from bs4 import BeautifulSoup
import category


#1. Interroger le site "Books to scrappe"

url="http://books.toscrape.com/"

#2. Récupérer toutes les catégories (nouvelle définition puisque 
# "infex.html" ne figure pas dans le menu home" - 
# !!! Question : books1 présente l'ensemble des livres, doit-il figurer dans les catégories, 
# parti pris: non)

def base_category1(url):                              #ok, 05/10/2023
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    recherche_col=soup.find("ul",class_="nav nav-list")
    #print(recherche_col)
    liste_category0=[]
    for lien in recherche_col.findAll("a"):
        liste_category0.append(lien.get('href'))
        #exple : lien='catalogue/category/books/philosophy_7/index.html'
    liste_category0.pop(0)
    #print(liste_category0)
    return(liste_category0)

def category1(url):                                    #ok, 05/10/2023
    liste_category0=base_category1(url)
    liste_category2=[]
    for lien in liste_category0:
        lien1=lien.split('/')
        lien1.pop()
        nom_category=lien1[3]
        liste_category2.append(nom_category)
        #exple : nom_category='science-fiction_16'
    #print("liste des catégories",len(liste_category), liste_category)
    return(liste_category2)

def adresse_category(url):                              #ok, 05/10/2023
    liste_category0=base_category1(url)
    liste_adresse_category=[]
    for lien_partiel in liste_category0:
        adresse_category=url+lien_partiel
        liste_adresse_category.append(adresse_category)
        # exple : adresse_category='http://books.toscrape.com/catalogue/category/books/romance_8/index.html'
    #print(liste_adresse_category)
    return(liste_adresse_category)


#3. Créer un fichier csv contenant tous les livres.

def creation_noms_fichiers_text(url): #ok,05/10/2023
    liste_noms_fichiers_txt=[]
    liste_category=category1(url)  
    for nom_category in liste_category:
        nom_category_text="p2_ph3_"+nom_category+".text"
        liste_noms_fichiers_txt.append(nom_category_text)
    #print(liste_noms_fichiers_txt,len(liste_noms_fichiers_txt))
    return(liste_noms_fichiers_txt) 

def creation_noms_fichiers_csv(url): #ok, 05/10/2023
    liste_noms_fichiers_csv=[]
    liste_category=category1(url)  
    for nom_category in liste_category:
        nom_category_csv="p2_ph3_"+nom_category+".csv"
        liste_noms_fichiers_csv.append(nom_category_csv)
    #print(liste_noms_fichiers_csv,len(liste_noms_fichiers_csv))
    return(liste_noms_fichiers_csv) 
  
def creation_fichiers_par_categorie(url):
    liste_fichiers_txt=creation_noms_fichiers_text(url)
    liste_fichiers_csv=creation_noms_fichiers_csv(url)
    liste_categories=adresse_category(url)
    for lien in liste_categories:
        for fichier1_text in liste_fichiers_txt:
            for fichier2_csv in liste_fichiers_csv:
                ph2.creation_fichiers(lien, fichier1_text,fichier2_csv)


#creation_fichiers_par_categorie(url)
liste_fichiers_txt=creation_noms_fichiers_text(url)
liste_fichiers_csv=creation_noms_fichiers_csv(url)
liste_categories=adresse_category(url)
liste_parametre = list(zip(liste_categories, liste_fichiers_txt,liste_fichiers_csv))
#exple : liste_parametre[0]='http://books.toscrape.com/catalogue/category/books/travel_2/index.html', 'p2_ph3_travel_2.text', 'p2_ph3_travel_2.cvs'
#print(liste_parametre[0])

for paramet in liste_parametre:
    url1=str(paramet[0])
    fichier1_txt=str(paramet[1])
    fichier2_csv=str(paramet[2])
    print(paramet,"\n", "1.",url1,"\n","2.",fichier1_txt,"\n","3.",fichier2_csv)
    ph2.creation_fichiers(url1,fichier1_txt,fichier2_csv)
    #time.sleep(1)

"""
def creation_fichiers_par_cat(url,fichier1_txt,fichier2_csv):
    for adresse in toutes_les_pages(url):
        url=adresse
        page = requests.get(url) 
        if page.ok:
            BeautifulSoup(page.content, 'html.parser')
            livres=liste_livres(url)
            print(adresse,len(livres)) #ok
            #enregistrement d'un fichier txt contenant tous les liens des livres d'une catégorie
            with open (fichier1_txt,'a') as cat5: #ok
                for livre in livres:
                    cat5.write(livre+'\n')

    url_livre1=liste_livres(url)[0]
    ph1.en_tete_csv(url_livre1,fichier2_csv)
        
    with open (fichier1_txt,'r') as cat5:
        for ligne in cat5:
            url=ligne.strip()
            response=requests.get(url)
            if response.ok:
                valeurs_client=ph1.valeurs_tableau(url)
                with open(fichier2_csv,'a') as fich_cat5:
                    ligne = valeurs_client
                    writer = csv.writer(fich_cat5, delimiter=',')
                    writer.writerow(ligne)
"""