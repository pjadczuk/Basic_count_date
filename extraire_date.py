"""
Permet  d'extraire les  dates en forme de liste de liste [[année,mois,jour]]
"""

# Nom du fichier texte à lire
file_name = open('visites.txt')

liste=[]
def extraire_duree_ligne(ligne):
    debut = ligne.find('\t')+1
    fin = ligne.find(' - ')
    return ligne[debut:fin]

mes_lignes= file_name.readlines()
for lignes in mes_lignes:
    ma_ligne=lignes.strip()
    liste.append(extraire_duree_ligne(ma_ligne))
liste=set(liste)
liste=list(liste)
for i in range(len(liste)):
    liste[i]=liste[i].split('-')
