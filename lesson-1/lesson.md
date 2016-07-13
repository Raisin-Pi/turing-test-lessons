# Leçon 1 - Comment les ordinateurs pensent-ils ?

## Introduction

Comment les ordinateurs pensent-ils ? Dans cette leçon, les élèves étudieront de quelle manière les ordinateurs et les robots suivent une séquence d'instructions pour accomplir une tâche. Cette leçon incite principalement les élèves à découvrir le Raspberry Pi, se connecter, accéder à Python 3 ou IDLE3, et à taper une petite séquence d'instructions pour créer une forme.

## Objectifs de l'exercice

-	Rendre compte que les ordinateurs suivent une séquence d'instruction pour réaliser quelque chose.
-	Être en mesure d'installer un Raspberry Pi et de donner un ensemble d'instructions en Python pour en faire une forme.


## Résultats de l'exercice

### Les élèves seront capables de :

- Savoir que les ordinateurs exécutent des programmes qui sont des séquences d'instructions pour réaliser quelque chose.  
- Ecrire un programme simple.

### La plupart des élèves seront capables de :

-	Comprendre que Python est un langage de programmation informatique.
-	Écrire un programme Python simple et expliquer une séquence.

### Certains élèves seront capables de :

-	Écrire un programme pour créer une forme plus complexe.

## Résumé de la leçon

-	Introduction aux parties physiques de base d'un Raspberry Pi.
-	Démonstration que le Raspberry Pi peut se comporter comme un ordinateur traditionnel.
-	Le premier programme Python.


## Démarrage

Tout d'abord, désignez 3 ou 4 élèves en leur demandant d'agir comme des robots puis divisez les élèves restants en 3 ou 4 équipes. Chaque équipe dispose de son propre « robot » dans une « course » pour voir qui arrivera à le contrôler à travers la salle de classe. Expliquez aux « robots » qu'ils ne doivent suivre que les instructions qui leur sont données par leur équipe. Puis, commencez la course. Tout au long de la course, veillez à ce que les élèves utilisent des instructions comme « 10 pas en avant » et « tournez à 90 degrés vers la droite ».

A la fin de la course, discutez des problèmes que les équipes ont rencontrés en demandant à leur robot de suivre leurs instructions. Prolongez ce questionnement par le fait que le robot ne peut pas prendre de décisions par lui-même, et donc que les élèves doivent se montrer très précis sur les directives données.

Expliquez qu'un ordinateur fonctionne en exécutant des instructions l'une après l'autre dans un ordre spécifique. Un ordre donné d'instructions est appelé un programme. Chaque programme s'exécute avec un contrôle de flux donné, décrivant quelle instruction s’exécute à tel instant et quelle sera la prochaine.


## Déroulement de l’exercice

1.	Ayez un Raspberry Pi déjà connecté avec le programme de tchat robot lancé. Tenez la carte Raspberry dans votre main et demandez aux élèves ce qu'ils pensent que c'est. Expliquez-leur que c'est un ordinateur et que vous allez en faire quelque chose de spécial dans les leçons à venir. Au lieu de lancer des applications et des jeux déjà existants, nous allons apprendre à écrire notre propre logiciel pour créer un robot qui discute avec nous.

2.	Commencez avec toutes les parties du Raspberry Pi sur une table: clavier, souris, haut-parleur, carte mémoire, alimentation, moniteur, câble et bien sûr le Raspberry Pi ! Demandez aux élèves de nommer et de décrire chaque composant que vous connectez au Raspberry Pi. Enfin, mettez sous tension et regardez-le démarrer. Une démonstration alternative serait de laisser de côté la carte mémoire et de tenter de démarrer le Pi, ce qui échouera. Vous pouvez ensuite décrire la carte mémoire comme quelque chose qui contient des instructions pour dire au Raspberry Pi comment démarrer. Tous les Raspberry Pi doivent être démarrés et en attente sur l'écran de connexion.

3.	Demander aux élèves de mettre en place leur équipement Raspberry Pi, de l'allumer et de se connecter à leur Pi en utilisant le nom d'utilisateur `pi` et le mot de passe `raspberry`.

	**A noter : les élèves ne verront pas le texte quand ils tapent le mot de passe mais vous pouvez les assurer que ça marche. Pourquoi, pensent-ils, que c'est ainsi ? Astuce : qu'est ce qu'il peut arriver si quelqu'un regardait au-dessus de leur épaule ?**

4.	Ensuite, les élèves doivent charger l'environnement graphique en tapant `startx`. Une fois que le bureau est chargé, montrer aux élèves comment ouvrir **Python 3** ou **IDLE3** en cliquant sur le menu principal **Main Menu**, puis la programmation **Programming** et la sélection de **Python 3**.

	**A noter : cette série de leçons utilise Python 3. Si les élèves lancent IDLE il est possible que leur code ne s'exécute pas.**

5.	Expliquez aux élèves que **Python 3** ou **IDLE3** est une application ou un environnement qui vous permet d'écrire un programme simple en utilisant le langage **Python** de programmation. Il vous permet d'écrire, éditer et exécuter du code.

6.	Montrer aux élèves comment dessiner une forme en tapant une séquence d'instructions, ligne par ligne. Voir la [Fiche de Travail](worksheet.md) pour les étapes nécessaires à l’exécution de cette tâche.

7.	Demandez aux élèves de fermer leur Raspberry Pi en cliquant sur l'icône « Arrêter » **Shut Down** qui se trouve sur le bureau.

## Présentation en classe

Ecrivez la liste suivante de mots sur le tableau :

-	Instructions
-	Séquence
-	Raspberry Pi
-	Python
-	IDLE 3

Sélectionnez un élève au hasard dans la classe qui doit choisir un des mots du tableau, se lever et désigner quelqu'un d'autre qui doit donner la signification du mot. L'élève désigne alors quelqu'un d'autre et ainsi de suite…

## Devoir

Les élèves doivent écrire une séquence d'instructions pour une tâche, comme s'habiller pour aller à l'école ou leurs mouvements de danse préférés.
