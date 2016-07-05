# Leçon 1 - Comment les ordinateurs pensent-ils ?

## Brancher votre Raspberry Pi

Le Raspberry Pi est un ordinateur nu. Pour produire du son avec la carte, nous avons besoin de connecter un certains nombre d'éléments :

-	**Une carte micro-SD**. Cette carte contient les programmes qui peuvent être chargés sur le Raspberry Pi afin qu'il éxécute les choses. Vous devez glisser la carte dans la fente avec les broches métalliques orientés vers le Raspberry Pi. L'étiquette doit être visible quand elle est insérée.
-	**Un clavier**. Branchez le clavier dans l'un des ports USB. USB signifie Universal Serial Bus.C’est une sorte de connecteur pour toutes sortes d'appareils. Le clavier sera le principal outil que nous allons utiliser pour communiquer nos programmes au Raspberry Pi.
-	**Une souris**. Branchez la souris sur l'un des autres ports USB.
-	**Un séparateur/adaptateur doubleur audio**. Ceci est un câble qui va diviser le signal audio en 2. Branchez-le dans la prise audio sur le Raspberry Pi.
-	**Casque/Ecouteurs**. Ils vous permettront d'entendre le son que vous allez produire. Branchez les dans le séparateur audio.
-	**Un écran**. Cela vous permettra de voir le programme que vous êtes en train de créer. Branchez le connecteur HDMI dans le port HDMI du Raspberry Pi. Branchez l'autre extrémité du câble HDMI dans votre moniteur.
-	**Une alimentation**. Branchez l'alimentation dans une prise, puis le petit connecteur USB dans le Raspberry Pi. Lorsque vous allumez l'interrupteur de la prise, vous devriez voir le flash Raspberry Pi et le texte devrait apparaître sur le moniteur.


## Connectez-vous


1.	Une fois que le Raspberry Pi a démarré, vous serez accueilli avec un simple invite de texte pour la connexion.
2.	Tapez `pi` et appuyez sur **Entrée**.
3.	Ensuite, vous serez invité à donner votre mot de passe. Tapez `raspberry` et appuyez sur **Entrée** à nouveau.

	Ne vous inquietez pas que vous ne voyez pas le mot de passe à l'écran en tapant. Il s'agit d'une fonctionnalité de sécurité pour éviter que les gens regardent par-dessus de votre épaule pour récupérer votre mot de passe. Vous devrez vous trouver désormais devant un drôle de'invité de commandes.

## Commencer avec l'interface graphique

Le drôle d'invité de commandes textuelles que vous voyez est l'un des moyens les plus puissants pour communiquer avec un ordinateur. Cependant, il n'est pas très facile d'accès et est rempli de commandes étranges, un peu comme une formule magique. Nous pouvons donc passer à un environnement graphique plus familier, avec des fenêtres et des barres de menus, avec lesquelles on se sentira plus à l'aise. Pour démarrer l'interface, tapez `startx` dans l'invite de texte et appuyez sur **Entrée**.

## Démarrer avec l'environnement de programmation Python 3

Une fois que l'environnement graphique s'est lancée, vous pouvez cliquer sur le **menu principal** en haut de l'écran et choisissez **Python 3** dans le menu de programmation **Programming menu**. Cela va ouvrir l'environnement de programmation Python connu sous le nom **IDLE3**.

![](images/idle3.png)

## Ecrire un simple programme

Vous allez écrire un programme pour créer une forme.

1.	A côté des 3 flèches `>>>` ou de l’invite de commandes, tapez :

	```python
	import turtle
	```
Puis appuyez sur **Entrée**.

2.	A  côté des flèches suivantes `>>>` ou de l’invite de commandes, tapez :

	```python
	robot = turtle.Turtle()
	```
Cette ligne de commande ouvrira la fenêtre graphique « Tortue » avec une flèche au milieu. Ceci est votre tortue, votre robot, et vous pouvez lui donner des instructions pour se déplacer.

3.	Faisons-lui ressembler davantage à une tortue robot en tapant :

	```python
	robot.shape("turtle")
	```

4.	Pour demander à votre tortue robot de se déplacer, tapez :

	```python
	robot.forward(100)
	robot.right(90)
	```
A présent, que vous faut-il de plus pour créer une forme carrée ?
