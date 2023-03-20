import os
import pandas as pd

path = r'C:\Users\guilh\Desktop\Nova pasta'

# files = ['_ceinture_carre',
#          '_ceinture_cercle',
#          '_ceinture_huit',
#          '_ceinture_rectangle',
#          '_ceinture_rectangle_diag',
#          '_ceinture_triangle',
#          '_cheville_cercle2',
#          '_cheville_cercle3',
#          '_cheville_coeur',
#          '_cheville_hasard',
#          '_cheville_huit',
#          '_cheville_ligne_marche_arriere',
#          '_cheville_losange',
#          '_cheville_rectangle',
#          '_cheville_rectangle_diag',
#          '_cheville_triangle',
#          '_dos_carre',
#          '_dos_cercle',
#          '_dos_coeur',
#          '_dos_rectangle_diag',
#          '_dos_triangle',
#          '_poche_carre',
#          '_poche_cercle_antihoraire',
#          '_poche_cercle_horaire',
#          '_poche_coeur',
#          '_poche_rectangle_diag',
#          '_poche_triangle']

for file in os.scandir(path + '\\xlsx'):
    read_file = pd.read_excel(path + '\\xlsx\\' + file.name)
    read_file.to_csv(path + '\\csv\\' + file.name[:-5] + '.csv', index = None, header=True)
