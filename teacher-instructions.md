# Instructions de mise en place pour l'enseignant

Pour ce parcours de travail les élèves devraient avoir accès à :

- Un Raspberry Pi
- Un clavier et souris connecté au RPi
- Un écran connecté au RPi
- Carte SD avec la dernière version de NOOBS et avec l'OS Raspbian d'installé (instructions ci-dessous)
- espeak téléchargé et installé sur chaque Carte SD (instructions ci-dessous)

Pour la leçon 3, les élèves auront besoin du matériel supplémentaire suivant :

- Un adaptateur doubleur de sortie audio connecté à la prise jack du RPi, si les élèves sont en train de travailler en binome sur un RPi.
- Un casque/écouteurs branchés sur l'adaptateur ou RPi par élève.


## Téléchargement et installation NOOBS

Instructions pour les meilleures pratiques pour le [téléchargement et installation de NOOBS peut être lu ici](http://www.raspberrypi.org/help/noobs-setup/).


## Téléchargement et installation d'Espeak

1. Après avoir démarré, se connecter avec le login par défaut `pi` et le mot de passe `raspberry`.
2. Via le terminal en ligne de commande taper : `sudo apt-get install espeak`.
3. Appuyer sur `Y` (ou `O` si en français) au clavier quand demandé.


## Forcer le son vers la sortie casque

1. Se rassurer que les casques sont bien branché dans la prise jack du Raspberry Pi.
2. Après démarrage et connexion vous pouvez taper la commande suivante dans le terminal (ligne de commande) : `amixer cset numid=3 1`.
3. Sinon vous pouvez charger le bureau graphique en tapant `startx`, puis cliquer sur l'icone **Python Games**, selectionner **Force headphones** et cliquer sur **OK**.

	![](lesson-3/images/audio_output.png)

## Préparation d'un lot de cartes SD pour une classe

Une fois les étapes ci-dessus terminées, vous pouvez créer une copie de votre carte SD "maître" et puis l'utiliser pour faire un lot de cartes pour toute la classe.

1. Placer la carte SD "maître" dans un ordinateur ou laptop équipé d'un lecteur de carte mémoire.
2. Sous Windows utiliser [Win disk 32 imager](http://sourceforge.net/projects/win32diskimager/) pour faire une copie d'une carte SD. Sous Mac OSX vous pouvez utiliser la commande `dd` ou  [dd-gui](http://www.gingerbeardman.com/dd-gui/).
3. Retirer la carte SD "maître" et la garder précieusement.
4. Prendre une carte SD vierge et l'insérer dans l'ordinateur ou laptop.
5. Formatter la carte SD puis, via le logiciel d'écriture d'image, selectionner l'image et l'écrire sur la carte.
6. Répéter la dernière étape pour les autres cartes.
