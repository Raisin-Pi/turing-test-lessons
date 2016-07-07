# Leçon 3 - Créer un tchat robot

## Introduction

Cette leçon apprendra aux élèves comment utiliser le tchat robot, comment afficher la discussion à l’écran et comment créer des robots qui parlent.
Vous devrez vous assurer que « espeak » a été téléchargé et installé sur les cartes SD en utilisant  `sudo apt-get install espeak`.

Les élèves devront avoir accès aux écouteurs/casques pour entendre les sons, vous pourriez aussi avoir besoin d’un haut-parleur pour faire une démonstration en commun.

Enfin, vous devrez vous assurer que le son est géré par les écouteurs plutôt que par le HDMI, en tapant `amixer cset numid=3 1` ou en double-cliquant sur l’icône Python Games et en sélectionnant **Force Headphones**.

## Objectifs de l’exercice

- 	Identifier et utiliser des dispositifs d’entrée et de sortie sur un Raspberry Pi
-	Être capable d’ajouter du code pour tchater avec un programme robot sur le Raspberry Pi en lui faisant lire le texte à haute voix.
-	Tester et évaluer les programmes de robot crées jusqu’ici

## Résultats de l’exercice

### Les élèves seront capables de :

-	Identifier un  dispositif d’entrée et de sortie sur un ordinateur Raspberry Pi.
-	Créer du code sur un programme de tchat robot en lui permettant de parler à voix haute.

### La plupart des élèves seront capables de :

-	Tester et fournir un retour d’information sur le programme.

### Certains élèves seront capables de :

-	Trouver des moyens d’améliorer le tchat robot à travers l’évaluation.


## Sommaire de la leçon

-	Activité d’identification
-	Ajout de texte-parole
-	Amélioration des programmes Python

## Démarrage

Placer, si possible, 4 ensembles des éléments suivants sur un bureau et non connectés :

-	Raspberry Pi
-	Haut-parleurs
-	Ecouteurs/Casques
-	Module Caméra Pi (si vous en avez un)
-	Webcam
-	Clavier
-	Souris
-	Moniteur

Affectez les élèves à des groupes et donnez à chaque groupe des feuilles ou du ruban adhésif de couleurs différentes. Puis laissez-leur le temps d’étiqueter tous les composants avec les informations suivantes :

-	Ce que c’est
-	Si c’est un dispositif d’entrée ou de sortie
-	Ce à quoi ça sert

Après que les élèves aient identifié ces composants, demandez aux groupes d’expliquer les réponses données. Identifiez toutes celles qui sont incorrectes ou vraiment intéressantes et discutez-en avec la classe.
Expliquez que tous les ordinateurs ont des ports d’entrée et de sortie, ce qui a son importance spécialement pour le tchat robot, si on veut écouter les questions/réponses via un casque ou un haut-parleur.

![](images/audio_output.png)

## Déroulement de l’exercice

1.	Demandez aux élèves de mettre en route leur équipement Raspberry Pi et se connecter en utilisant le nom d’utilisateur `pi` et le mot de passe `raspberry`
Ils devront ensuite charger le programme robot en utilisant **IDLE3**, comme vu dans les précédentes leçons.

2.	En utilisant les devoirs de la leçon précédente, demandez aux élèves d’ajouter d’autres questions à l’aide du code `input` et `print`.

3.	Expliquez maintenant qu’ils auront besoin d’ajouter du code pour que le Raspberry Pi dise à voix haute les mots du programme.
Pour cela, ils devront entrer le code suivant :

	```python
	# Mon program en Python par ...
	import os, time

	def robot(text):
	    os.system("espeak ' " + text + " ' ")

	robot("Bonjour")
	```
	**Notez que l’indentation (tabulations et espaces) est importante ; l’éditeur de texte dans IDLE3 devrait normalement auto-édenter pour vous mais le programme ne pourra pas fonctionner sans cela.**    

4. Demandez aux élèves de sauvegarder ceci en enregistrant un nouveau fichier en cliquant sur **File** et **Save As** et le nommer **robot1**. Ils peuvent ensuite lancer leur programme et ils devraient normalement entendre une voix disant « Bonjour » !

5. Ensuite, expliquez-leur qu’au lieu de seulement afficher leurs questions à l’écran, ils peuvent maintenant les faire prononcer par le robot et obtenir des réponses.

	Pour cela, ils auront d’abord besoin de remplacer le mot `print` avec le nom de la fonction robot, puis de supprimer la virgule `,`, et de la remplacer par le symbole plus  `+`. Demandez aux élèves d’enregistrer et de faire un test à ce stade. Peuvent-ils expliquer ce qu’il se passe ? Des points bonus peuvent être attribués à ceux qui trouveront le moyen de faire répondre le robot. La réponse est d’ajouter la ligne ci-dessous en utilisant la fonction `robot`, par exemple :

	```python
	robot('What is your name')
name = input('What is your name: ')
robot("Nice to meet you " + name)
	```
![](images/espeak2.png)

## Travail en commun

Demandez aux élèves d’échanger leur place avec leurs camarades. Ils ont quelques minutes pour tester le programme de leur camarade et suggérer au moins une amélioration en écrivant un commentaire avec le symbole `#`. Les élèves devront ensuite retourner à leur propre programme et appliquer les améliorations.

En exercice supplémentaire, les élèves pourraient effacer une ligne du code du programme de leur camarade, échanger leur place et voir s’ils peuvent réparer le code erroné !
