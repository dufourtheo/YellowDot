print("Nous allons maintenant calculer le nombre de points jaunes.")

valeurs = [64, 32, 16, 8, 4, 2, 1]
messages = ["64", "32", "16", "8", "4", "2", "1"]
total = 0

for i in range(len(valeurs)):
    reponse = input("Voulez-vous ajouter {} points jaunes ? (oui/non) ".format(messages[i]))
    if reponse.lower() == "oui":
        total += valeurs[i]
        print("{} a été ajouté à votre total.".format(messages[i]))
    else:
        print("Aucun changement n'a été apporté pour {}.".format(messages[i]))

print("Le total de points jaunes est de : {}".format(total))

with open("resultat.txt", "w") as f:
    f.write(str(total))
    print("Le résultat a été sauvegardé dans le fichier resultat.txt.")
