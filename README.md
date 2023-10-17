# BOOKS ONLINE - SYSTÈME DE SURVEILLANCE DES PRIX

Application exécutable à la demande pour le suivi automatique des livres chez [« Books to Scrape »](http://books.toscrape.com/), plus précisément le suivi des prix et autres données nécessaires au service Marketing.

Résultat attendu : Pour chaque catégorie, l’analyse des livres est présentée dans un fichier csv. Chaque fichier csv est accompagné des images des livres concernés. L’ensemble est classé dans les dossiers des catégories respectives.

**Ce programme est une version « bêta », c’est-à-dire une version préliminaire mise à disposition à des fins de test et d’évaluation.**
## INSTALLATION
### PRÉREQUIS
+ Python3
+ Pour les dépendances : consulter requirements.txt
+ Terminal
### INSTALLATION ÉTAPE PAR ÉTAPE
+	Sur GitHub :
1.	Aller sur https://github.com/ThalyaC/p2
2.	Cliquer sur le bouton « code » puis copier l’url du dépôt.

+	Ouvrir votre terminal :
1.	Aller vers le dossier où sera stocké le projet (commande « cd ») 
2.	Cloner le dépôt, pour cela :
commande `git clone` + url copiée  
Exemple : `git clone https://github.com/ThalyaC/p2.git`
3.	Accéder au dossier du programme (commande « cd ») 
4.	Mettre en place un environnement virtuel :  
    a. Pour installer votre environnement :
    Taper : `python3 -m venv env`  
    b. Pour l’activer : `source env/bin/activate`   
(pour le désactiver à la fin du processus, taper simplement : `deactivate`)
7.	Installer les dépendances listées dans le fichier requirements.txt  
Exemple : `pip install requests`
## UTILISATION 
### POUR EXÉCUTER LE PROGRAMME
Taper :  `python3 lancement.py`
### RÉSULTAT ATTENDU
Le programme créera un certain nombre de dossiers situés au même niveau de son arborescence. Actuellement il y a 50 catégories sur le site cible, donc 50 dossiers.
Dans chaque dossier, vous trouverez :
-	Un fichier csv contenant les livres de cette même catégorie avec les informations suivantes : « product_page_url, universal_ product_code (upc), title, price_including_tax, price_excluding_tax, number_available, product_description, category, review_rating, image_url »
-	Les images des livres mentionnés ci-dessus.
  
> [!NOTE]
> L’exécution du programme dure un peu moins de 20 minutes.
