import random
import string
from tkinter import messagebox

while True :

    y_n = str(input("voulez vous un mot de passe ? [y/n] : "))

    if y_n == "y" :
        try :
            a = int(input("Entrer le nombre de minuscule que vous souhaitez : "))
            b = int(input("Entrer le nombre de majuscule que vous souhaitez : "))
            c = int(input("Entrer le nombre de caractère spéciaux que vous souhaitez : "))
            d = int(input("Entre le nombre de chiffre que vous souhaitez : "))

        except ValueError:
           print("Vous avez entré une valeur impossible ! Relancez le programme ! ")
           break


        lettres_min = random.choices(string.ascii_lowercase, k=a)
        lettres_maj = random.choices(string.ascii_uppercase, k=b)
        chiffres = random.choices(string.digits, k=c)
        speciaux = random.choices(string.punctuation, k=d)
        liste_finale = lettres_min + lettres_maj + chiffres + speciaux
        random.shuffle(liste_finale)
        mot_de_passe = ''.join(liste_finale)
        print("votre mot de passe est :", mot_de_passe)

    else :
        print("Au revoir !")
        break

