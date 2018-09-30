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
        jour = int(input("Quel jour: "))                                                                                        # On entre le jour
        D.append(jour)                                                                                                          # On l'ajoute dans le tableau D
        mois = int(input("Quel mois (en chiffre): "))                                                                           # idem pour le mois 
        D.append(mois)
        annee = int(input("De quelle année: "))                                                                                 # idem pour l'année
        D.append(annee)
        if not checkDate(D):                                                                                                    # Vérification que la date rentrée est valide
            print("Erreur dans la saisie de la date")
        else:
            break
    return D

# Fonction pour vérifier que la date saisie est correcte
def checkDate(D):
    if anneeBissextile(D[2]):                                                                                                   # On teste pour savoir si l'année est bissextile afin de pouvoir determiner le nombre de jour de février
        joursMois[1] = 29
    else:
        joursMois[1] = 28
    return D[1] >= 1 and D[1] <= 12 and D[0] >= 1 and D[0] <= joursMois[D[1] - 1] and D[2] >= 1600 and D[2] <= 2199     

# Fonction pour calculer le jour recherché selon la méthode donnée
def calculJour(D):

    x = D[2] % 100                                                                                                              # On garde les deux derniers chiffre de l'année
    x = x + (x//4)                                                                                                              # On ajoute le quart de ce chiffre sans les restes
    x = x + D[0]                                                                                                                # On ajoute la journée du mois
    x = x + ajoutMois[D[1]-1]                                                                                                   # Selon le mois on ajoute une des valeurs contenues dans ajoutMois
    if anneeBissextile(D[2]) and (D[1] == 1 or D[1] == 2):                                                                      # Si l'année est bissextile et que le mois est janvier ou février on ôte 1
        x = x - 1
    x = x + ajoutSiecle[D[2]//100-16]                                                                                           # Selon le siècle on ajoute un des éléments de ajoutSiecle
    x = x % 7                                                                                                                   # On divise la somme obtenue par 7 et on garde le reste
    return x                                                                                                                    # Retourne une valeur entre 0 et 6 qui permettra de déterminer le jour cherché

# Fonction pour afficher le résultat
def affichage(D, joursVoulu):
    print("La date que vous avez rentré, correspond au:\n", J[joursVoulu], D[0], M[D[1]-1], D[2])

# Exécution du programme
date = dateSaisie()
joursVoulu = calculJour(date)
affichage(date, joursVoulu)
