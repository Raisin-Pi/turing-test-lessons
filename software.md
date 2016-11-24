# Installation Applications

## Téléchargement et installation espeak

1. Après démarrage, se connecter avec le login par défaut `pi` et mot de passe `raspberry`.
2. A l'invite de la ligne de commande/terminal tapez : `sudo apt-get install espeak`.
3. Taper `Y` (ou `O` en français) sur le clavier au moment venu.

## Forcer le son vers le casque

1. Assurez-vous que le casque est bien branché au niveau de la sortie son jack du Raspberry Pi.
2. Après démarrage et connexion, vous pouvez entrer la ligne de commande suivante : `amixer cset numid=3 1`.
3. Sinon vous pouvez charger le bureau en tapant `startx`, cliquez sur l'icône **Python Games**, sélectionnez par la suite **Force headphones** et cliquez sur **OK**.

	![](/lesson-3/images/audio_output.png)
