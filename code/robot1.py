# Mon Programme en Python par ...
import os, time

def robot(text):
    os.system("espeak '" + text + "'")

robot("Bonjour")

time.sleep(1)

robot('Quel est votre prénom')
prenom = input('Quel est votre prénom : ')
robot("Enchanté de faire votre connaissance " + prenom)

time.sleep(1)

robot("Vous avez quel âge")
age = input('Vous avez quel âge : ')
robot("Vous n'avez pas l'air d'avoir " + age "ans")
