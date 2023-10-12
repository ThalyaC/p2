"""
Projet 2 phase 2
Phase Récuperer les liens d'une catégorie, 
puis extraire les données demandées pour chaque livre dans un fichier csv.

"""

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

def suite_page_intermed(url):               #(ok 04/10/2023)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    recherche_li_next=soup.find("li",class_="next")
    extrait_page_suivante=recherche_li_next.find('a').get('href')
    #print("1, ",extrait_page_suivante)# exple résultat = page-2.html
    return(extrait_page_suivante)

def numero_page_suivante(url):              #ok, 04/10/2023
    extrait_page_suivante=suite_page_intermed(url)
    recherche_nombre0=extrait_page_suivante.split('.')
    recherche_nombre0.pop()                 #suppression html
    recherche_nombre1='.'.join(recherche_nombre0)
    recherche_nombre2=recherche_nombre1.split('-')
    recherche_nombre=recherche_nombre2[1]
    #print(recherche_nombre) #exple : 2
    return(recherche_nombre)

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
    liste_pages=[]
    liste_pages.append(url)
    n=2
    while validation_page_factice(n,url):
        resultat=validation_page_factice(n,url)
        liste_pages.append(resultat)
        n=n+1
    #print(liste_pages)
    return(liste_pages)
    #exple : ['http://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html',
    # 'http://books.toscrape.com/catalogue/category/books/sequential-art_5/page-2.html', 
    # 'http://books.toscrape.com/catalogue/category/books/sequential-art_5/page-3.html', 
    # 'http://books.toscrape.com/catalogue/category/books/sequential-art_5/page-4.html']
    
# Récupérer les liens internet des produits

#   liste des catégories pour les soustraire de la liste des liens
def categories(url):                              #ok, 03/10/2023
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    recherche_col=soup.find("ul",class_="nav nav-list")
    #print(recherche_col)
    liste_categories=[]
    for link in recherche_col.findAll("a"):
        liste_categories.append(link.get('href'))
    liste_categories.remove("index.html")
    #print("liste des catégories",liste_category)
    return(liste_categories)

# Récupération de tous les liens (ok)
def recuperation_liens(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    liste_lien=[]
    for link in soup.findAll('a'):
        liste_lien.append(link.get('href'))
    #print("1.",liste_lien)
    return(liste_lien)
    
# Suppression des doublons (ok)
def suppression_doublon(url):
    liens_uniques = []
    for lien in recuperation_liens(url) :
        if lien not in liens_uniques:
            liens_uniques.append(lien)
    #print("2.",len(liens_uniques), liens_uniques)
    #print("3.",liens_uniques[-1])
    return(liens_uniques)

# Liste des liens des pages de livres (ok)
def liste_livres(url):
    #print(url)
    liens_sans_liens_categories=[]
    for lien in suppression_doublon(url) :
        if lien not in categories(url):
            liens_sans_liens_categories.append(lien)
    
    liens_livres_imcomplets=[]
    for lien in liens_sans_liens_categories:
        chaine_texte=lien.split("/")
        #sous_liste.append("4.",chaine_texte)
        
        sous_liste=['..']
        chaine_texte1=[]
        for lien in chaine_texte:
            if lien not in sous_liste:
                chaine_texte1.append(lien)
        chaine_texte1 = list(filter(None, chaine_texte1)) #pour supprimer les chaines vides
        #print("5.",chaine_texte1)
        chaine_texte1.pop(-1)
        lien_sans_index='/'.join(chaine_texte1)
        liens_livres_imcomplets.append(lien_sans_index)
        liens_livres_imcomplets = list(filter(None, liens_livres_imcomplets))
    #print("6.",len(liens_livres_imcomplets), liens_livres_imcomplets)
        
    liens_livres=[]
    for lien in liens_livres_imcomplets:
        lien_livre="http://books.toscrape.com/catalogue/"+lien+"/index.html"
        liens_livres.append(lien_livre)
        #print("7.",liens_livres)
    return(liens_livres)
    
# Enregistrement des liens dans un fichier texte 
# Enregistrement des données dans un fichier csv, ok, 04/10/2023

#url="http://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html"
#fichier1_txt='projet2_phase2_cat5.txt'
#fichier2_csv='projet2_phase2.csv'

def creation_fichiers(url,fichier1_txt,fichier2_csv):
    for adresse in toutes_les_pages(url):
        url=adresse
        page = requests.get(url) 
        if page.ok:
            BeautifulSoup(page.content, 'html.parser')
            tslivres=liste_livres(url)
            print("ph2 adresse validée :",adresse,len(tslivres)) #ok
            #enregistrement d'un fichier txt contenant tous les liens des livres d'une catégorie
            with open (fichier1_txt,'a') as cat5: #ok
                for livre in tslivres:
                    cat5.write(livre+'\n')

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