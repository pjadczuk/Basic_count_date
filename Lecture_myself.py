"""
Permet d'afficher le nombre de fois où vous étiez à la salle par mois
"""



# Nom du fichier texte à lire
file_name = open('visites.txt')

# Créer un dictionnaire pour stocker les visites par mois
visits_by_month = {}
liste=[]
def extraire_duree_ligne(ligne):
    debut = ligne.find('2023')+1
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
for i in range(len(liste)):
    del liste[i][0]


for elem in liste:
    mois,date=elem
    if mois not in visits_by_month:
        visits_by_month[mois]=1
    else:
        visits_by_month[mois]+=1

sorted_data = dict(sorted(visits_by_month.items()))

month_mapping = {
    '01': 'janvier',
    '02': 'février',
    '03': 'mars',
    '04': 'avril',
    '05': 'mai',
    '06': 'juin',
    '07': 'juillet',
    '08': 'août',
    '09': 'septembre',
    '10': 'octobre',
    '11': 'novembre',
    '12': 'décembre'
}

# Trier le dictionnaire par les clés (ordre croissant)
sorted_data = dict(sorted(visits_by_month.items()))

# Afficher le dictionnaire trié avec les mois correspondants
for key, value in sorted_data.items():
    month = month_mapping.get(key, "Mois inconnu")
    print(f"{month}: {value}")