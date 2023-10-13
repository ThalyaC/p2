#projet 2 phase 1
#Phase 1: Récuperer les éléments suivants dans la page et les stocker dans des variables.

# appeler les librairies pour ce programme
import requests
from bs4 import BeautifulSoup
import csv


# indiquer la page internet consultée et accéder à son code html source
#url = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
#url = ph0.url

def analyse_page_livre(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')    
# Voir le code html source
#bs4 parse la page et nous permet d'accéder à des éléments du code et à les modifier si nécessaire.
#phase 1.A récupérer les éléments extraits d'un tableau

#1.a.1 récupération des données du seul tableau contenu dans la page html

#les clés
    cle_tableau=soup.find_all("th")
    cle_texte = []
    for cle in cle_tableau:
        cle_texte.append(cle.string)

    #print("1.",cle_texte)

#Les valeurs
    valeur_tableau=soup.find_all("td")
    valeur_texte = []
    for valeur in valeur_tableau:
        valeur_texte.append(valeur.string)

    #print("2.",valeur_texte)

#1.a.2 modification des noms de clés selon la demande du projet
    cle_texte[0]="universal_product_code (upc)"
    cle_texte[2]="price_excluding_tax"
    cle_texte[3]="price_including_tax"
    cle_texte[5]="number_available"
    #print("3.",cle_texte)

#1.a.3 extraction du nombre de stock disponible dans la chaîne de caractère
    chaine_texte=valeur_texte[5].replace("(","")
    chaine_texte=chaine_texte.replace(")","")
    chaine_texte=chaine_texte.replace(" ",",")
    chaine_texte=chaine_texte.split(",")
    #print("4.",chaine_texte)
    #print("5.",len(chaine_texte))

# sachant que le nombre souhaité se trouve en 3ème position:
    valeur_texte[5]=chaine_texte[2]
    #print("6.",valeur_texte)

#Inversion de position entre les prix (exl. et incl.)
    elt1=cle_texte[2]
    elt2=cle_texte[3]
    inversion_cle=[]
    inversion_cle.append(elt2)
    inversion_cle.append(elt1)
    #print("7. inversion des clés 2 et 3",inversion_cle)

    elta=valeur_texte[2]
    eltb=valeur_texte[3]
    inversion_valeur=[]
    inversion_valeur.append(eltb)
    inversion_valeur.append(elta)
    #print("8. inversion des valeurs 2 et 3",inversion_valeur)

    elt1=inversion_cle[0]
    elt2=inversion_cle[1]
    cle_texte[2]=elt1
    cle_texte[3]=elt2
    #print("9. nouvelles clés du tableau :",cle_texte)

    elta=inversion_valeur[0]
    elt2=inversion_valeur[1]
    valeur_texte[2]=elta
    valeur_texte[3]=eltb
    #print("10. nouvelles_valeurs_tableau:",valeur_texte)

# 1.a.4 suppression des éléments non utilisés dans le tableau
    element_a_supprimer = [1, 4, 6]
 
    for element in sorted(element_a_supprimer, reverse = True):
        del cle_texte[element]
        del valeur_texte[element]
 
    #print ("11. vérification des listes:", cle_texte, valeur_texte)

#Phase 1.B insertion des éléments hors tableau

# 1.b.1 création d'une fonction pour insérer les clés, valeurs dans les listes respectives (pos = position)
    def insertion(pos, cle, valeur):
        cle_texte.insert(pos, cle)
        valeur_texte.insert(pos, valeur)

#1.b.2 récupération et insertion des éléments demandés dans les listes

# product_page_url - l'adresse url de la page
    product_page_url=url
    insertion(0, "product_page_url", product_page_url)
    #print(f"12. Adresse de la page : {product_page_url}")

#le titre de la page (<title>)
    title1=soup.title.string
    title1=title1.strip('\n')
    title1=title1.split('|')

    title2 = []
    for titre in title1:
        title2.append(titre)
    #print(title2)

    title=title2[0]
    insertion(2,"title",title)
    #print(f"13. titre de la page : {title}")

#product_description (seul p sans class)
    if soup.find("p", class_=None):
        product_description=soup.find("p", class_=None)
        product_description=product_description.text
    else :
        product_description="vide"
    insertion(6, "product_description", product_description)
    #print(f"14. description du produit : {product_description}")

#1.a.4 category
    category0=soup.find_all('a')

    category=[]
    for categ in category0:
        category.append(categ.string)

    insertion(7, "category", category[3]) 
    #print("15. catégorie :",category[3])

#évaluation
    etoile=["star-rating One", "star-rating Two", "star-rating Three", "star-rating Four", "star-rating Five"]
    review_rating0=soup.find("p",class_=etoile)
    review_rating1=review_rating0.attrs
    review_rating2=review_rating1['class']
    del review_rating2[0]
    review_rating=review_rating2[0]

    insertion(8, "review_rating", review_rating)
    #print(f"16. évaluation : {review_rating}")

#image du livre
    titre_image=soup.h1.string
    image_url0=soup.find("img", alt=titre_image)
    image_url1=image_url0.attrs
    image_url2=image_url1['src']
    image_url="http://books.toscrape.com/"+image_url2
    insertion(10, "image_url", image_url)
    #print("17.adresse de l'image :",image_url)

# Phase C création d'un dictionnaire pour le CVS
    tableau= dict(zip(cle_texte, valeur_texte))
    #print("18.dictionnaire pour le CSV",tableau)
    return (tableau)

def en_tete_tableau(url):
    tableau=analyse_page_livre(url)
    en_tete1=tableau.keys()
    en_tete=[]
    for en_t in en_tete1:
        en_tete.append(en_t)
    #print("1. en-tête du document",en_tete)
    return(en_tete)

def valeurs_tableau(url):
    tableau=analyse_page_livre(url)
    valeurs_client1=tableau.values()
    valeurs_client=[]
    for val in valeurs_client1:
        valeurs_client.append(val)

    #print("2. valeurs du document",valeurs_client)
    return(valeurs_client)

def en_tete_csv(url,fichier):
    en_tete=en_tete_tableau(url)
    with open(fichier, 'w') as fichier_csv:
        writer = csv.writer(fichier_csv, delimiter=',')
        writer.writerow(en_tete)
    return()

def inserer_valeurs_csv(url,fichier):
    valeurs_client=valeurs_tableau(url)
    with open(fichier, 'a') as fichier_csv:
        ligne = valeurs_client
        writer = csv.writer(fichier_csv, delimiter=',')
        writer.writerow(ligne)
    return()

# # Créer un objet writer (écriture additionnelle sinon "w" qui écrase les données précédente) avec ce fichier

#Lancement de l'écriture de la phase 1 dans un fichier csv
def livre1(url,fichier):
    analyse_page_livre(url)
    en_tete_csv(url,fichier)
    inserer_valeurs_csv(url,fichier)
#en_tete_csv() # à ne réaliser qu'une fois

def livre_suivant(url,fichier):
    analyse_page_livre(url)
    inserer_valeurs_csv(url,fichier)


"""
fichier='livre.csv'
url = "http://books.toscrape.com/catalogue/soumission_998/index.html"
livre1(url,fichier)

url="http://books.toscrape.com/catalogue/sharp-objects_997/index.html"
livre_suivant(url,fichier)
"""

