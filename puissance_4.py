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

# Affichage graphique

racine = tk.Tk()
canvas = tk.Canvas(racine, width=DIAMETRE_JETON*NOMBRE_COLONNE, height=DIAMETRE_JETON*NOMBRE_LIGNE, bg="blue")

canvas.grid()

configuration_initiale()
affichage_jeuton()

racine.mainloop()