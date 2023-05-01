import numpy as np
from PIL import Image

img = Image.open("carduelis-tristis.jpg")


r, g, b = img.split()
r.show(title="Canal Rouge")
g.show(title="Canal Vert")
b.show(title="Canal Bleu")

r_array = np.array(r.resize((4, 4)))
g_array = np.array(g.resize((4, 4)))
b_array = np.array(b.resize((4, 4)))

print("Tableau du canal Rouge : ")
print(r_array)
print("Tableau du canal Vert : ")
print(g_array)
print("Tableau du canal Bleu : ")
print(b_array)
