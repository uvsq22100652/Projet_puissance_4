#########################################################
# Groupe LDDBI 6
# Clémence GERMETTE
# Sofia TERKI
# Erwan MAIRE
# Adam JACCOU
#########################################################

# Librairies
import tkinter as tk

# Constantes
NOMBRE_LIGNE = 6
NOMBRE_COLONNE = 7
DIAMETRE_JETON = 100

# Variables globals
configuration = []
jeuton = []
joueur = 1

# Fonctions

def configuration_initiale():
    """
    Création d'une grille vide
    """
    global configuration
    if configuration != []:
        configuration = []
    for i in range(NOMBRE_LIGNE):
            configuration.append([0 for j in range(NOMBRE_COLONNE)])
    return configuration


def affichage_jeuton():
    """
    Fonction qui associe à chaque valeur de la configuration le jeuton de couleur corespondante
    """
    canvas.delete('all')
    del jeuton[:]
    for i in range(NOMBRE_LIGNE):
        for j in range(NOMBRE_COLONNE):
            if configuration[i][j] == 0:
                color = "white"
            elif configuration[i][j] == 1:
                color = "red"
            elif configuration[i][j] == 2:
                color = "yellow"
            jeuton.append(canvas.create_oval(j*(DIAMETRE_JETON)+10, i*(DIAMETRE_JETON)+10,
             (j+1)*(DIAMETRE_JETON)-10, (i+1)*(DIAMETRE_JETON)-10,fill = color, outline = color))

            
def mouvement_jeton(event):
    """Fonction qui permet de faire tomber le jeton dans la
    grille jusqu'à toucher le fond ou un autre jeton"""
    global joueur, configuration
    x = event.x
    ligne = -1
    if x<100:
        colonne = 0
    if 100<x<200:
        colonne = 1
    if 200<x<300:
        colonne = 2
    if 300<x<400:
        colonne = 3
    if 400<x<500:
        colonne = 4
    if 500<x<600:
        colonne = 5
    if 600<x<700:
        colonne = 6
    while configuration[ligne][colonne] != 0:
        ligne -= 1
    if joueur == 1:
        configuration[ligne][colonne] = 1
        joueur = 2
    elif joueur == 2:
        configuration[ligne][colonne] = 2
        joueur = 1
    affichage_jeuton()
    
    
# Affichage graphique

racine = tk.Tk()
canvas = tk.Canvas(racine, width=DIAMETRE_JETON*NOMBRE_COLONNE, height=DIAMETRE_JETON*NOMBRE_LIGNE, bg="blue")

canvas.grid()

canvas.bind('<Button>', mouvement_jeton )
configuration_initiale()
affichage_jeuton()

racine.mainloop()
