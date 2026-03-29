from random import *
import time
euro = 200
print("Tu commences le jeu avec un capital de 200€")
print("Pour gagner tu dois avoir un capital de 1000€")
while euro<1000:
    mise=int(input("Combien mises tu ? "))
    if mise>euro:
        print("Tu n'as pas assez de fonds")
        continue
    elif mise==0:
        print("Tu ne peux pas miser 0€")
        continue
    roulette = randint(0, 20)
    nombre=int(input("Choisi un nombre entre 0 et 20: "))
    if 0<=nombre<=20:
        print("La roulette se lance !")
    else:
        print("Le nombre que tu as choisi n'est pas entre 1 et 20.")
        continue
    time.sleep(2.0)
    if nombre == roulette:
        print("La roulette s'est arrêter sur le chiffre" , roulette)
        print("Bravo, tu as remporté ta mise de" , mise, "€")
        euro=euro+mise
        print("Tu as maintenant" , euro , "€")
    else:
        print("La roulette s'est arrêter sur le chiffre" , roulette)
        print("Dommage tu as perdu!")
        euro=euro-mise
        print("Tu à désormais" , euro , "€")
    if euro ==0:
        print("Tu as fait faillite")
        break
if euro>=400:
    print("Bravo tu as gagné !")

