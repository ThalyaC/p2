import livres
from urllib.request import urlretrieve

url = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"

liste=livres.valeurs_tableau(url)
lien_image0=liste[9]

lien_image=lien_image0.replace("../../", "")
#print("lien de l'image: ",lien_image)

titre_image0=liste[0]
titre_image1=titre_image0.split('/')
titre_image=titre_image1[4].replace("-","_")
#print("titre_essai :",titre_image)

dossier0=liste[7]
dossier1=dossier0.lower()
dossier2=dossier1.replace(" ","_")
dossier=dossier2 + "/"

def download_image(lien_image, dossier, titre_image):
    full_path = dossier + titre_image+".jpg"
    urlretrieve(lien_image, full_path)

#download_image(lien_image, dossier, titre_image)



