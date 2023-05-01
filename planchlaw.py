# ce code permet de donner la loi de planck pour différents températures. la longeur d'onde est entre 300 nm et 1020 nm
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
h = 6.626e-34
c = 3.0e+8
k = 1.38e-23
def planck(wav, T):
    a = 2.0*h*c**2
    b = h*c/(wav*k*T)
    intensity = a/ ( (wav**5) * (np.exp(b) - 1.0) )
    return intensity
wavelengthsPlan = np.arange(300e-9, 1020e-9, 10e-9)
intensity3000 = planck(wavelengthsPlan, 3000.)
intensity2800 = planck(wavelengthsPlan, 2800.)
intensity2600 = planck(wavelengthsPlan, 2600.)
intensity2400 = planck(wavelengthsPlan, 2400.)
intensity2200 = planck(wavelengthsPlan, 2200.)
intensity2000 = planck(wavelengthsPlan, 2000.)
intensity1800 = planck(wavelengthsPlan, 1800.)
plt.figure(1)
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

