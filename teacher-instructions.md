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

1. Après avoir démarré, se connecter avec le login par défaut `pi` et password `raspberry`.
2. Via le terminal en ligne de commande taper : `sudo apt-get install espeak`.
3. Appuyer sur `Y` (ou `O` si en français) au clavier quand demandé.


## Forcer le son vers la sortie casque

1. Se rassurer que les casques sont bien branché dans la prise jack du Raspberry Pi.
2. After booting and logging in you can type the following line on the command line: `amixer cset numid=3 1`.
3. Alternatively you can load the desktop by typing `startx`, double-clicking on the **Python Games** icon, selecting **Force headphones** and clicking **OK**.

	![](lesson-3/images/audio_output.png)

## Making a class set of SD cards

Once you have completed the steps above, you can make a copy of your master SD card and then use that to make a class set.

1. Place your master SD card in a computer or laptop with an SD card reader.
2. On Windows use [Win disk 32 imager](http://sourceforge.net/projects/win32diskimager/) to make a copy of an SD card. On Mac OSX you can use the `dd` command or a [dd-gui](http://www.gingerbeardman.com/dd-gui/).
3. Remove the master SD card and keep it safe.
4. Take a fresh SD card and insert it into your computer or laptop.
5. Format the SD card then, using your imaging software, select the image and write it to the card.
6. Repeat the last step for the rest of your cards.
