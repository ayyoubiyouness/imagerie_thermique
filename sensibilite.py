# ce code permet de tracer les sensibilités du capteur utilisé dans l'iphone7 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# On importe les données des sensibilités du capteur utilisé dans l'iphone 7. la première colonne correspond à la couleur
# rouge. la deuxième colonne correspond à la couleur verte. la troixième colonne correspond à la couleur bleu. 
# les longueurs d'ondes sont entre 410 nm et 700 nm 
df = pd.read_excel('iPhone8.xlsx')

# on nomme les colonnes puisqu'elles ne sont pas nommée dans la base de données
df.columns = ['red', 'vert', 'bleu']

# on stocke les valeurs des sensibiltés dans des listes pour faire les calculs
sens_red = []
for i in range (0,30):
    element1 = df.loc[i, 'red']
    sens_red.append(element1)

sens_green=[]
for i in range (0,30):
    element2 = df.loc[i, 'vert']
    sens_green.append(element2)

sens_blue=[]
for i in range (0,30):
    element3 = df.loc[i, 'bleu']
    sens_blue.append(element3)


# On définit une liste de longueurs d'ondes entre 410 nm et 700 nm
longueurs_ondes = [wavelength for wavelength in range(410, 710,10)]


# on trace les figures des trois sensibilités dans la meme courbe
plt.figure(2)
plt.plot(longueurs_ondes, sens_red, 'r-', label="red color")
plt.plot(longueurs_ondes, sens_green, 'g-', label="green color")
plt.plot(longueurs_ondes, sens_blue, 'b-', label="blue color")
plt.xlabel('Longueur d\'onde (nm)')
plt.ylabel('Relative value ')
plt.title('Relative spectral sensitivity functions iPhone7')
plt.legend()
# ce code seul ne va pas afficher la courbe. 
# Si vous voulez l'utiliser tout seul, il faut ajouter dans la ligne 41 plt.show()

