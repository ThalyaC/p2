import livres
from urllib.request import urlretrieve

url = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"

liste=livres.valeurs_tableau(url)
lien_image0=liste[9]

lien_image=lien_image0.replace("../../", "")
 #print("lien de l'image: ",lien_image)

titre_image0=liste[2]
    
def supprimer_ponctuation(chaine):
    caracteres_alphanum=""
    for caractere in chaine:
        if caractere.isalnum() or caractere.isspace():
            caracteres_alphanum += caractere
    return(caracteres_alphanum)

titre_image1=supprimer_ponctuation(titre_image0)
titre_image2=titre_image1.replace(" ","_")
titre_image3=titre_image2.split("_")
titre_image4 = list(filter(None, titre_image3))
titre_image5='_'.join(titre_image4)
titre_image=titre_image5
#print("titre de l'image souhaité: ",titre_image)

dossier0=liste[7]
dossier1=dossier0.lower()
dossier2=dossier1.replace(" ","_")
dossier=dossier2 + "/"

def download_image(lien_image, dossier, titre_image):
    full_path = dossier + titre_image+".jpg"
    urlretrieve(lien_image, full_path)

download_image(lien_image, dossier, titre_image)



