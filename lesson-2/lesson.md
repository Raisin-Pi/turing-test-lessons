# Leçon 2 - Les ordinateurs peuvent-ils penser par eux-mêmes ?

## Introduction

Basé sur la leçon 1 utilisant IDLE3, cette leçon vous introduira à la programmation par Python par la rédaction d’un programme simple en prenant les instructions utilisateur et en les affichant à l’écran


## Objectifs de l’exercice

-	Savoir comment déboguer un code
-	Comprendre les différences entre parler à un être humain et parler à un programme informatique
-	Être en mesure de créer et déboguer un simple programme d’ordinateur sur Python en utilisant `print` et les commandes d’entrée utilisateur


## Résultats de l’exercice

### Les élèves seront capables de :

-	Ecrire un simple programme Python et vérifier qu’il fonctionne.

### La plupart des élèves seront capables de :

-	Comprendre que Python est un langage de programmation informatique.
-	Ecrire un programme Python simple et savoir expliquer sa séquence.

### Certains élèves seront capables de :

-	Comprendre les limites de l'ordinateur, en comparaison avec l'intelligence humaine, quand il suit des instructions.


## Sommaire de la leçon

- Le premier programme Python

## Démarrage

Dirigez les élèves vers un site internet contenant un tchat robot, comme [Elbot](http://www.elbot.com/). Vous pouvez aussi utiliser Siri sur un appareil Apple.

Les élèves peuvent poser des questions au tchat robot. Demandez-leur de noter toute réponse ne correspondant pas à la question posée. Après quelques minutes d'exercice, rassemblez-les autour d'une discussion où ils pourront donner leurs avis et faire des commentaires. Le professeur devra prendre note des quelques questions qui ont pu rendre confus le tchat robot.

Avec les élèves, dégagez les raisons pour lesquelles ils pensent que le tchat robot ne peut pas répondre à toutes leurs questions comme ils le souhaitent.

Demandez aux élèves pourquoi il est si difficile pour des programmes comme celui-ci de comprendre et interagir avec des êtres humains. Pourquoi est-ce si facile de confondre les deux ? Faites ressortir le fait que les ordinateurs exécutent ou lancent des programmes qui suivent une séquence d'instructions, et qu'ils ne peuvent suivre que cette séquence.

Expliquez le concept du [Test de Turing](http://fr.wikipedia.org/wiki/Turing_test) et de l'Intelligence Artificielle puis annoncez-leur que dans cette leçon, ils vont écrire des programmes Python sur le Raspberry Pi pour le transformer en tchat robot.


## Déroulement de l'exercice

1.	Demandez aux élèves de préparer tout leur matériel Raspberry Pi, de l'allumer et de se connecter en utilisant le nom d'utilisateur `pi` et le mot de passe `raspberry`.

	**A noter : cette série de leçons utilise Python 3. Si les élèves lancent IDLE 2 il est possible que leur code ne s'exécute pas.**

2.	Ensuite, les élèves devront charger l'environnement graphique en tapant `startx`. Pour utiliser Python, ils auront besoin d'accéder à l’environnement de programmation **IDLE3**. Pour l'ouvrir, ils peuvent soit double-cliquer sur l'icône IDLE3, soit cliquer sur **Main Menu**, sélectionner **Programming** suivi de **IDLE 3**.

	![](images/idle3.png)

3.	Montrez-leur la fenêtre d'interprétation IDLE. Expliquez que les commandes peuvent êtres saisies directement dans cette fenêtre après l'invite qui ressemble à cela `>>>`. Cette fenêtre est considérée comme l'interprète. Vous pouvez taper une ligne de code après cet invite et appuyer sur Entrée, ce qui aura pour effet de lancer la ligne de code. Vous pouvez le montrer en tapant  `print("Bonjour le Monde!")`. Laissez-les essayer la fenêtre d'interprétation puis expliquez que l'ordinateur ne peut suivre qu'une instruction à la fois dans la **séquence**.

4.	Expliquez que quand vous écrivez beaucoup de lignes de code dans un programme, cela peut vite devenir fatigant d'utiliser l'interprète ; si vous souhaitez enregistrer votre code, il est préférable d'utiliser un éditeur de texte.
Montrez-leur comment créer un nouveau fichier de l'éditeur de texte en cliquant sur **Fichier>Nouvelle fenêtre** dans le menu du haut de la fenêtre **IDLE3**. Montrez comment on enregistre le fichier en cliquant sur **Fichier > Enregistrer Sous** et nommez-le `name1.py`.

5.	Demandez aux élèves de taper le code suivant dans la fenêtre d'éditeur de texte ;
Soulignez la différence entre un commentaire et une ligne de code. Les commentaires sont une partie totalement ignorée du programme mais qui permettent de prendre note de ce qu'il se passe dans le programme.

	```python

	# Mon Programme en Python par ...

	name = input('Quel est votre prénom : '),
	print("Enchanté de faire votre connaissance ", name)
	```

	*Remarque : les espaces avant `"` dans la chaîne de caractères sont importantes.*

	Enregistrez le fichier comme un fichier Pyhton en cliquant sur **File**, puis **Save as** et nommez-le **robot**.

	Lancez ensuite le fichier en cliquant sur **Run**, puis sur **Run Module**.

	![](images/program-1.png)

6. Les élèves peuvent alors ajouter leurs propres instructions en entrée et déclarations `print`, comme demander l’âge de l’utilisateur ou sa couleur préférée. Par exemple, ils peuvent ajouter :

	```python
age = input('Vous avez quel âge : ')
print("Vous n'avez pas l'air d'avoir", age, "ans")
	```

	Demandez aux élèves d’enregistrer le fichier et de lancer le code comme précédemment.

	![](images/program-2.png)

7. Une fois que les élèves ont des programmes avec de multiples questions, introduisez l’idée d’espacer les questions posées dans le temps. Dans une conversation, il y a habituellement une pause entre une réponse et une question suivante. L’objectif est de créer un tchat robot qui puisse être déconcertant pour un être humain ; par conséquent, nous avons besoin d’une pause entre les questions. Pour obtenir cela, on peut utiliser le module `time`. Pour ajouter le module, les élèves auront besoin d’ajouter `import time` sous le commentaire et avant les questions.
Maintenant, entre les questions, ils auront besoin d’utiliser `time.sleep(1)` où la valeur 1 représente 1 seconde.

	![](images/program-3.png)

8. Laissez les élèves continuer à écrire du code en entrée utilisateur et à afficher l’information à l’écran.
Ensuite, demandez aux élèves de sauvegarder leur travail et d’éteindre le Raspberry Pi en cliquant sur le bouton **Eteindre/Shutdown** dans le bureau.

## Travail en commun

Demandez aux élèves de choisir 3 nouveaux mots qu’ils ont appris durant la ou les dernières leçons puis de les définir. Ensuite, demandez-leur d'écrire un paragraphe pour chacun des mots, ou en utilisant les 3 à la fois.


## Devoirs

Les élèves devront réfléchir à 5 questions qu’ils souhaiteraient poser au tchat robot à la prochaine leçon.
