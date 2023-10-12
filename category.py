"""
Projet 2 phase 2
Phase Récuperer les liens d'une catégorie, 
puis extraire les données demandées pour chaque livre dans un fichier csv.

"""#ok 12/10/23

# appeler les librairies pour ce programme
import requests
from bs4 import BeautifulSoup
import csv
import livres

"""
Catégorie choisie : sequential-art_5
75 livres
4 pages

"""
#Recherche des pages suivantes de la catégorie :

def racine(url):                               #ok 04/10/2023
    url1=url.split('/')
    #print(url1)
    url1.pop()                                  #suppression du dernier élément
    url_sans_index = '/'.join(url1)             # transformation d'une liste en chaine de caractères
    #print(url_sans_index) 
    # #exple : http://books.toscrape.com/catalogue/category/books/sequential-art_5
    return(url_sans_index)

def suite_page_factice(n,url):                      #ok 04/10/2023
    url_sans_index=racine(url)
    page_suivante="page-"+str(n)+".html"
    nouvelle_page=url_sans_index+"/"+page_suivante
    #print(nouvelle_page) 
    #exple=http://books.toscrape.com/catalogue/category/books/sequential-art_5/page-1.html
    return(nouvelle_page)

def validation_page_factice(n,url):                 #ok, 04/10/2023
    urlx=suite_page_factice(n,url)
    page = requests.get(urlx)
    if page.ok:
        #print(urlx,"ok")
        return(urlx)

def toutes_les_pages(url):                      #ok, 04/10/2023
    liste_pages_next=[]
    liste_pages_next.append(url)
    n=2
    while validation_page_factice(n,url):
        resultat=validation_page_factice(n,url)
        liste_pages_next.append(resultat)
        n=n+1
    #print(liste_pages)
    return(liste_pages_next)
    #exple : ['http://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html',
    # 'http://books.toscrape.com/catalogue/category/books/sequential-art_5/page-2.html', 
    # 'http://books.toscrape.com/catalogue/category/books/sequential-art_5/page-3.html', 
    # 'http://books.toscrape.com/catalogue/category/books/sequential-art_5/page-4.html']
    
# Récupérer les liens internet des produits


def liste_livres_1page(url): #ok 12/10/23
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    # Récupération de tous les liens (ok)
    liste_lien=[]
    for link in soup.findAll('a'):
        liste_lien.append(link.get('href'))
    #print("1.",liste_lien)
    #return(liste_lien)
    # Suppression des doublons (ok)
        liens_uniques = []
        for lien in liste_lien :
            if lien not in liens_uniques:
                liens_uniques.append(lien)
    #print("2.",len(liens_uniques), liens_uniques)
    #print("3.",liens_uniques[-1])
    #return(liens_uniques)
    #   liste des catégories pour les soustraire de la liste des liens
    recherche_col=soup.find("ul",class_="nav nav-list")
    #print(recherche_col)
    liste_categories=[]
    for link in recherche_col.findAll("a"):
        liste_categories.append(link.get('href'))
    liste_categories.remove("index.html")
    #print("liste des catégories",liste_categories)
    #return(liste_categories)
    # Liste des liens des pages de livres (ok)
    liens_sans_liens_categories=[]
    for lien1 in liens_uniques :
        if lien1 not in liste_categories:
            liens_sans_liens_categories.append(lien1)
    
    liens_livres_imcomplets=[]
    for lien2 in liens_sans_liens_categories:
        chaine_texte=lien2.split("/")
        #sous_liste.append("4.",chaine_texte)
        
        sous_liste=['..']
        chaine_texte1=[]
        for lien3 in chaine_texte:
            if lien3 not in sous_liste:
                chaine_texte1.append(lien3)
        chaine_texte1 = list(filter(None, chaine_texte1)) #pour supprimer les chaines vides
        #print("5.",chaine_texte1)
        chaine_texte1.pop(-1)
        lien_sans_index='/'.join(chaine_texte1)
        liens_livres_imcomplets.append(lien_sans_index)
        liens_livres_imcomplets = list(filter(None, liens_livres_imcomplets))
    #print("6.",len(liens_livres_imcomplets), liens_livres_imcomplets)
        
    liens_livres=[]
    for lien4 in liens_livres_imcomplets:
        lien_livre="http://books.toscrape.com/catalogue/"+lien4+"/index.html"
        liens_livres.append(lien_livre)
    #print("7.",len(liens_livres))
    #résultat : liste des livres de la première page.
    return(liens_livres)


def ts_livres(url): #ok 12/10/23
    liste_ts_livres=[]
    for adresse in toutes_les_pages(url):
        print("ph2 adresse validée :",adresse,len(liste_livres_1page(adresse)))
        for livre in liste_livres_1page(adresse):
            liste_ts_livres.append(liste_livres_1page(adresse)) 
    print(len(liste_ts_livres))
    return(liste_ts_livres)

url="http://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html"
ts_livres(url)

    
# Enregistrement des liens dans un fichier texte 
# Enregistrement des données dans un fichier csv, ok, 04/10/2023

#url="http://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html"
#fichier1_txt='projet2_phase2_cat5.txt'
#fichier2_csv='projet2_phase2.csv'
#tous_les_livres_1categorie(url)
""""
def creation_fichiers_csv(url,fichier_csv):
    url_livre1=liste_livres(url)[0]
    livres.en_tete_csv(url_livre1,fichier2_csv)
        
    with open (fichier1_txt,'r') as cat5:
        for ligne in cat5:
            url=ligne.strip()
            response=requests.get(url)
            if response.ok:
                valeurs_client=livres.valeurs_tableau(url)
                with open(fichier2_csv,'a') as fich_cat5:
                    ligne = valeurs_client
                    writer = csv.writer(fich_cat5, delimiter=',')
                    writer.writerow(ligne)

#creation_fichiers(url,fichier1_txt,fichier2_csv)
"""