import livres
from urllib.request import urlretrieve

url = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
liste=livres.valeurs_tableau(url)
lien_image0=liste[9]
#http://books.toscrape.com/../../media/cache/fe/72/fe72f0532301ec28892ae79a629a293c.jpg
lien_image=lien_image0.replace("../../", "")
print("lien de l'image: ",lien_image)

titre_image0=liste[2]
titre_image1=titre_image0.replace(" ","_")
titre_image2=titre_image1.split("_")
titre_image3 = list(filter(None, titre_image2))
titre_image4='_'.join(titre_image3)
titre_image=titre_image4
print("titre de l'image souhaité: ",titre_image)


def nom_image_brut(lien_image):
    lien1=lien_image.split('/')
    nom_image_base=lien1[-1]
    return (nom_image_base)

nom_image_base=nom_image_brut(lien_image)
print("nom de l'image sur le site: ",nom_image_base)

dossier0=liste[7]
dossier1=dossier0.lower()
dossier2=dossier1.replace(" ","_")
dossier=dossier2 + "/"

def download_image(lien_image, dossier, titre_image):
    full_path = dossier + titre_image+".jpg"
    urlretrieve(lien_image, full_path)


download_image(lien_image, dossier, titre_image)


