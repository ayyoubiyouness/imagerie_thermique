import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_excel('iPhone8.xlsx')
df.columns = ['red', 'vert', 'bleu']
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
print(len(sens_blue))
longueurs_ondes = [wavelength for wavelength in range(410, 710,10)]
print(len(longueurs_ondes))

plt.figure(2)
plt.plot(longueurs_ondes, sens_red, 'r-', label="red color")
plt.plot(longueurs_ondes, sens_green, 'g-', label="green color")
plt.plot(longueurs_ondes, sens_blue, 'b-', label="blue color")
plt.xlabel('Longueur d\'onde (nm)')
plt.ylabel('Relative value ')
plt.title('Relative spectral sensitivity functions iPhone7')
plt.legend()


