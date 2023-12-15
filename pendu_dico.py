"""
Gère le dictionaire du jeu Pendu
"""

import random

DICO = [
    "BANANE",
    "POMME",
    "RHUM",
    "OISEAU",
    "CORBEAU",
    "CORBEAUX",
    "TRAIN",
    "VOITURE",
    "MOISISSURES",
    "AVION",
    "CAMION",
    "HYDROGENE",
    "POLYCARBONATE",
    "ROUGE",
    "VERT",
    "VERTUEUSES",
    "ALIGATOR"
]

def DonneMoiUnMot():
    """
    Tire au sort un mot et le retourne
    """
    global DICO

    return random.choice(DICO)
