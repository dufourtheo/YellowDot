#pip install Pillow
from PIL import Image
import sys
import webbrowser
import subprocess

if len(sys.argv) < 2:
    print("Erreur : Veuillez fournir le nom d'un fichier image en utilisant la commande :")
    print("python main.py nom_de_fichier.png")
    exit()

filename = sys.argv[1]


image = Image.open(filename)

#-------------------------------#

blue_channel = image.split()[2]
transformed_blue = blue_channel.point(lambda x: (256-x)**2)
transformed_blue.show()
#------------------------------#
# Sauvegarder l'image transformée
transformed_blue.save("transformed_" + filename)
print("L'image transformée a été enregistrée sous le nom : transformed_" + filename)






webbrowser.open("https://w2.eff.org/Privacy/printers/docucolor/")

subprocess.run(["python", "yellowdotcalcul.py", filename])


