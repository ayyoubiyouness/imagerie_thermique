import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# On importe les deux fichiers python pour utiliser les valeurs et les calculs déja fait
import sensibilite
import plancklaw

# On importe la base de données qui contient les sensibilités pour les différents 
df = pd.read_excel('iPhone8.xlsx')
wave = [wavelength/1e9 for wavelength in range(410,710,10)]


red_sens = sensibilite.sens_red
blue_sens = sensibilite.sens_blue
green_sens = sensibilite.sens_green

# on calcule l'intégrale avec la méthode de trapèze. 
# Au début, nous avons utilisé des méthodes d'intégration avec numpy.
#  Cependant, des erreurs se produisent. La solution était de programmer notre propre fonction d'intégration
def trapezoidal_rule(x, y, n) :
    h = (x[-1] - x[0]) / n
    sum = 0
    for i in range(1, n):
        sum += y[i]
    return h/2 * (y[0] + y[-1] + 2*sum)



# Par la suite, on va calculer les intensités des différents couleurs : rouge, vert et bleu. 
# On stocke ces veleurs dans des listes. 
NV = []
NR = []
NB = []

# On calcule pour chaque température l'énergie spectrale et le nombre de photon collecté par chaque capteur.
temp = np.arange(50, 10000,20)
for t in temp :
    # Pour une température T. on stocké les valeurs dans une liste. 
    valeur_planck = []
    for i in wave :
        valeur_planck.append(plancklaw.planck(i,temp))
    # Pour la température T. on calcule le produit de l'énergie spectrale et la sensibilité     
    produitgreen = []
    produitred = []
    produitbleu = []
    for i in range(len(red_sens)) :
        produitgreen.append(green_sens[i]*valeur_planck[i])
        produitred.append(red_sens[i]*valeur_planck[i])
        produitbleu.append(blue_sens[i]*valeur_planck[i])
    # Pour la température T. 
    # On calcule l'intégrale de chaque courbe pour récupérer le nombre de photons colléctés par chaque capteur    
    aire_sous_la_courbe_verte = trapezoidal_rule(wave, produitgreen, 30)
    aire_sous_la_courbe_rouge = trapezoidal_rule(wave, produitred, 30)
    aire_sous_la_courbe_bleu = trapezoidal_rule(wave, produitbleu, 30)
    NV.append(aire_sous_la_courbe_verte)
    NR.append(aire_sous_la_courbe_rouge)
    NB.append(aire_sous_la_courbe_bleu)
    break

# On stocke les valeurs des intensités dans des listes. 
couleur_v = NV [0]
couleur_r = NR[0]
couleur_b = NB[0]
couleurverte = list(couleur_v)
couleurbleu = list(couleur_b)
couleurrouge = list(couleur_r)

# Ensuite, on calcule les ratios
v_sur_r = []
for i in range(len(couleur_v)) :
    v_sur_r.append(couleurverte[i]/couleurrouge[i])

r_sur_v = []
for i in range(len(couleur_v)) :
    r_sur_v.append(couleurrouge[i]/couleurverte[i])


b_sur_v = []
for i in range(len(couleur_v)) :
    b_sur_v.append(couleurbleu[i]/couleurverte[i])


b_sur_r = []
for i in range(len(couleur_v)) :
    b_sur_r.append(couleurbleu[i]/couleurrouge[i])   
    

# En fin, on trace les courbes des ratios en fonction des températures
plt.figure(7)
plt.plot(temp, v_sur_r)
plt.xlabel('La température en Kelvin')
plt.ylabel('Ratio vert sur rouge')
plt.title('Représentation du ratio des intensités des sous pixels vert et rouge en fonction de la température')

plt.figure(8)
plt.plot(temp, r_sur_v)
plt.xlabel('La température en Kelvin')
plt.ylabel('Ratio rouge sur vert')
plt.title('Représentation du ratio des intensités des sous pixels rouge et vert en fonction de la température')

plt.figure(9)
plt.plot(temp, b_sur_v)
plt.xlabel('La température en Kelvin')
plt.ylabel('Ratio Bleu sur vert')
plt.title('Représentation du ratio des intensités des sous pixels bleu et vert en fonction de la température')


plt.figure(10)
plt.plot(temp, b_sur_r)
plt.xlabel('La température en Kelvin')
plt.ylabel('Ratio Bleu sur rouge')
plt.title('Représentation du ratio des intensités des sous pixels bleu et rouge en fonction de la température')

plt.show()


    

    
   
                     
                   
    











