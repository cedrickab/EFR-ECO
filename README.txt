                                          		 

Efr��co
Ce projet a �t� d�sign� et d�velopp� par Sary Ballou, Jean Crecel, Nathalie Colard, C�dric Kabor�, Arthy Kandiah, Olivia Kouam�

Sommaire:
1. Description globale
2. Pr�requis
3. Installation
3.1. Configuration de la base de donn�es
      3.2. Lancement de l�application

DESCRIPTION GLOBALE

Efr��co est une application destin�e � d�tecter des d�chets � partir d�une image import�e ou prise. De plus, elle ajoute des rep�res sur une carte l� o� se situe les d�chets.



PREREQUIS
t�l�charger nvidia cuda toolkit
t�l�charger anaconda
t�l�charger wamp server 
Avoir la base de donn�e


INSTALLATION

Configuration de la bas�e de donn�es :

Ouvrir l�application WampServer puis, sur la page phpMyAdmin, cr�er une nouvelle base de donn�es et la nommer �eco�. Importer le fichier eco.sql puis ex�cuter.


Lancement de l�application 
1-creer un environnement python 3.7 dans le cmd d'anaconda
$ conda create -n yourenvname python=3.7 anaconda 
 
2- activer l'environnement
$ source activate yourenvname
 
3- sur le nouvel environnemment tapez 
$  garden install mapview
$  pip install -r requirements.txt
$  train.sh
Une fois le fichier d'entr�e s�lectionn�, le classificateur produira les pr�dictions pour chaque ensemble de donn�es. Un score de pr�diction compris entre 0,8 et 1 est consid�r� comme optimal.

4- Tapez 
$ python main.py
