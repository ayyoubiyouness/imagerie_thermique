import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sensibilite
import plancklaw
import scipy.integrate as spi
df = pd.read_excel('iPhone8.xlsx')
wave = [wavelength/1e9 for wavelength in range(410,710,10)]

red_sens = sensibilite.sens_red
blue_sens = sensibilite.sens_blue
green_sens = sensibilite.sens_green

def trapezoidal_rule(x, y, n):
    h = (x[-1] - x[0]) / n
    sum = 0
    for i in range(1, n):
        sum += y[i]
    return h/2 * (y[0] + y[-1] + 2*sum)

NV = []
NR = []
NB = []
temp = np.arange(2000, 10000,20)
for t in temp :
   
    valeur_planck = []
    for i in wave :
        valeur_planck.append(plancklaw.planck(i,temp))
    produitgreen = []
    produitred = []
    produitbleu = []
    for i in range(len(red_sens)) :
        produitgreen.append(green_sens[i]*valeur_planck[i])
        produitred.append(red_sens[i]*valeur_planck[i])
        produitbleu.append(blue_sens[i]*valeur_planck[i])
    aire_sous_la_courbe_verte = trapezoidal_rule(wave, produitgreen, 30)
    aire_sous_la_courbe_rouge = trapezoidal_rule(wave, produitred, 30)
    aire_sous_la_courbe_bleu = trapezoidal_rule(wave, produitbleu, 30)
    NV.append(aire_sous_la_courbe_verte)
    NR.append(aire_sous_la_courbe_rouge)
    NB.append(aire_sous_la_courbe_bleu)
    break
couleur_v = NV [0]
couleur_r = NR[0]
couleur_b = NB[0]
couleurverte = list(couleur_v)
couleurbleu = list(couleur_b)
couleurrouge = list(couleur_r)

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


    

    
   
                     
                   
    











