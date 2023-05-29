# ce code permet de représenter la loi de planck pour différents températures. la longeur d'onde est entre 300 nm et 1020 nm
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# on définit les constantes utilisées dans la loi de planck
h = 6.626e-34
c = 3.0e+8
k = 1.38e-23
# cette fonction prend en entrée une liste de longueur d'onde et une température T et retourne les valeurs 
# de l'énergie spectrale pour chaque longueur d'onde
def planck(wav, T):
    a = 2.0*h*c**2
    b = h*c/(wav*k*T)
    intensity = a/ ( (wav**5) * (np.exp(b) - 1.0) )
    return intensity
# on définit la liste des longueurs d'onde, ici entre 300 nm et 1020 nm
wavelengthsPlan = np.arange(300e-9, 1020e-9, 10e-9)
# on calcule les énergies spectrales pour différentes températures
intensity3000 = planck(wavelengthsPlan, 3000.) # T = 3000 K
intensity2800 = planck(wavelengthsPlan, 2800.) # T = 2800 K
intensity2600 = planck(wavelengthsPlan, 2600.) # T = 2600 K
intensity2400 = planck(wavelengthsPlan, 2400.) # T = 2400 K
intensity2200 = planck(wavelengthsPlan, 2200.) # T = 2200 K
intensity2000 = planck(wavelengthsPlan, 2000.) # T = 2000 K
intensity1800 = planck(wavelengthsPlan, 1800.) # T = 1800 K

# Ensuite, on trace les courbes des énergies spectrales dans la meme courbe
plt.plot(wavelengthsPlan, intensity3000, 'r-', label="Température 3000K")
plt.plot(wavelengthsPlan, intensity2800, 'b-', label="Température 2800K")
plt.plot(wavelengthsPlan, intensity2600, 'y-', label="Température 2600K")
plt.plot(wavelengthsPlan, intensity2400, 'c-', label="Température 2400K")
plt.plot(wavelengthsPlan, intensity2200, 'g-', label="Température 2200K")
plt.plot(wavelengthsPlan, intensity2000, 'm-', label="Température 2000K")
plt.plot(wavelengthsPlan, intensity1800, 'k-', label="Température 3000K")
plt.xlabel('Longueur d\'onde (micro m)')
plt.ylabel('Densité spectrale d\'énergie ( J/s·m²·Hz·sr)')
plt.title('loi de planck')
plt.legend()

