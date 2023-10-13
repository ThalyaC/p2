"""
Projet 2 Phase 3
1. Interroger le site "Books to scrappe"; 
2. Récupérer toutes les catégories ;
3. Demande du 6/10/2023 : creation pour chaque catégorie d'un dossier devant accueillir en phase 4, les images
4. Créer un fichier csv contenant tous les livres par catégorie dans le dossier qui lui est attittré.
"""


import requests
from bs4 import BeautifulSoup
from category import creation_fichiers_csv
from os import mkdir, replace

#1. Interroger le site "Books to scrappe"

url="http://books.toscrape.com/"

#2. Récupérer toutes les catégories (nouvelle définition de "category" par rapport au fichier category puisque 
# "infex.html" ne figure pas dans le menu "home" - 
# sortir "books" qui n'est pas une catégorie, mais l'ensemble des livres du site.

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

def category1(url):                                  #ok, 05/10/2023, modifié le 13/10/23 *2
    liste_category2=[]
    for lien in base_category1(url):
        lien1=lien.split('/')
        lien1.pop()
        nom_category=lien1[3]
        nom_category1=nom_category.split('_')
        nom_category1.pop()
        nom_category2=nom_category1[0]
        liste_category2.append(nom_category2)
        #exple : nom_category='science-fiction'
    print("liste des catégories",len(liste_category2), liste_category2)
    return(liste_category2)

def adresse_category(url):                              #ok, 05/10/2023
    liste_adresse_category=[]
    for lien_partiel in base_category1(url):
        adresse_category=url+lien_partiel
        liste_adresse_category.append(adresse_category)
        # exple : adresse_category='http://books.toscrape.com/catalogue/category/books/romance_8/index.html'
    print(liste_adresse_category)
    return(liste_adresse_category)


#3. & 4. Créer un fichier csv par catégorie dans un dossier contenant tous les livres.

def creation_noms_dossiers(url): #ok 12/10/13
    liste_noms_dossiers=[]
    liste_category=category1(url)  
    for nom_category in liste_category:
        nom_category_dossier=nom_category
        liste_noms_dossiers.append(nom_category_dossier)
    #print(liste_noms_dossiers,len(liste_noms_dossiers))
    return(liste_noms_dossiers)

def creation_dossiers(url): # ok, 13/10/23
    for dossier in creation_noms_dossiers(url):
        try:
            mkdir(dossier)
        except OSError as e:
            pass
        finally :
            pass
    return()

def creation_noms_fichiers_csv(url): #ok, modifié le 13//10/2023
    liste_noms_fichiers_csv=[]
    liste_category=category1(url)  
    for nom_category in liste_category:
        nom_category_csv=nom_category+".csv"
        liste_noms_fichiers_csv.append(nom_category_csv)
    print(liste_noms_fichiers_csv,len(liste_noms_fichiers_csv))
    return(liste_noms_fichiers_csv) 

#creation_fichiers_par_categorie(url) #modifié le 13/10/23
liste_fichiers_csv=creation_noms_fichiers_csv(url)
liste_categories=adresse_category(url)
liste_parametre = list(zip(liste_categories, liste_fichiers_csv))
#print(liste_parametre[0]) exple : ('http://books.toscrape.com/catalogue/category/books/travel_2/index.html', 'travel_2.csv')

for paramet in liste_parametre:
    url1=str(paramet[0])
    fichier1_csv=str(paramet[1])
    print(paramet,"\n", "1.",url1,"\n","2.",fichier1_csv)
    creation_fichiers_csv(url1,fichier1_csv)

# pour placer les fichiers csv dans les dossiers
for nom in category1(url):
    emplacement_actuel="../p2/"+nom+".csv"
    destination="../p2/"+nom+"/"+nom+".csv"
    replace(emplacement_actuel,destination)


