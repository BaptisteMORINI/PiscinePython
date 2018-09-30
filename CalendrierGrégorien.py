# 25/09/18 - Noyade Sèche - Premier Pas dans l'eau
# Morini Baptiste

# Déclaration des différents tableaux utilisés dans le programme

D = []                                                                                                                          # Tableau qui va contenir la date
J = ["Dimanche", "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi"]                                                   # Tableau contenant les jours de la semaine
M = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]   # Tableau contenant les mois
ajoutMois = [0, 3, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5]                                                                                # Tableau contenant les valeurs à ajouter en fonction du mois pour le calcul de la date
ajoutSiecle = [6, 4, 2, 0, 6, 4]                                                                                                # Tableau contenant les valeurs à ajouter en fonction du siècle pour le calcul de la date
joursMois = [31, 0, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]                                                                     # Tableau contenant le nombre de jours par mois

# Fonction pour savoir si l'année rentrée est bissextile ou non
def anneeBissextile(annee):
    anneeBissextile = False
    if (annee % 400 == 0) or (annee % 4 == 0 and annee % 100 != 0):
        anneeBissextile = True
    return anneeBissextile

# Fonction pour saisir la date et la mettre dans le tableau D
def dateSaisie():
    while True:
        jour = int(input("Quel jour: "))
        D.append(jour)
        mois = int(input("Quel mois (en chiffre): "))
        D.append(mois)
        annee = int(input("De quelle année: "))
        D.append(annee)
        if not checkDate(D):
            print("Erreur dans la saisie de la date")
        else:
            break
    return D

# Fonction pour vérifier que la date saisie est correcte
def checkDate(D):
    if anneeBissextile(D[2]):
        joursMois[1] = 29
    else:
        joursMois[1] = 28
    return D[1] >= 1 and D[1] <= 12 and D[0] >= 1 and D[0] <= joursMois[D[1] - 1] and D[2] >= 1600 and D[2] <= 2199

# Fonction pour calculer le jour recherché selon la méthode donnée
def calculJour(D):

    x = D[2] % 100
    x = x + (x//4)
    x = x + D[0]
    x = x + ajoutMois[D[1]-1]
    if anneeBissextile(D[2]) and (D[1] == 1 or D[1] == 2):
        x = x - 1
    x = x + ajoutSiecle[D[2]//100-16]
    x = x % 7

    return x

# Fonction pour afficher le résultat
def affichage(D, joursVoulu):
    print("La date que vous avez rentré, correspond au:\n", J[joursVoulu], D[0], M[D[1]-1], D[2])

# Exécution du programme
date = dateSaisie()
joursVoulu = calculJour(date)
affichage(date, joursVoulu)