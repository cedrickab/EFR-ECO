                                          		 

Efr’éco
Ce projet a été désigné et développé par Sary Ballou, Jean Crecel, Nathalie Colard, Cédric Kaboré, Arthy Kandiah, Olivia Kouamé

Sommaire:
1. Description globale
2. Prérequis
3. Installation
3.1. Configuration de la base de données
      3.2. Lancement de l’application

DESCRIPTION GLOBALE

Efr’éco est une application destinée à détecter des déchets à partir d’une image importée ou prise. De plus, elle ajoute des repères sur une carte là où se situe les déchets.



PREREQUIS
télécharger nvidia cuda toolkit
télécharger anaconda
télécharger wamp server 
Avoir la base de donnée


INSTALLATION

Configuration de la basée de données :

Ouvrir l’application WampServer puis, sur la page phpMyAdmin, créer une nouvelle base de données et la nommer ‘eco’. Importer le fichier eco.sql puis exécuter.


Lancement de l’application 
1-creer un environnement python 3.7 dans le cmd d'anaconda
$ conda create -n yourenvname python=3.7 anaconda 
 
2- activer l'environnement
$ source activate yourenvname
 
3- sur le nouvel environnemment tapez 
$  garden install mapview
$  pip install -r requirements.txt
$  train.sh
Une fois le fichier d'entrée sélectionné, le classificateur produira les prédictions pour chaque ensemble de données. Un score de prédiction compris entre 0,8 et 1 est considéré comme optimal.

4- Tapez 
$ python main.py
