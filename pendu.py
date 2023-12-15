# *****************************************************************************
# ** Programme du Pendu                                                      **
# **-------------------------------------------------------------------------**
# ** 24/11/2023 | Yoann Darche | Création.                                   **
# *****************************************************************************

import pendu_dessin
import pendu_dico

# =============================================================================
# ==                 V A R I A B L E S   G L O B A L E S                     ==
# =============================================================================

LETTRES_PROPOSEES = [ ]
MOT_A_DEVINER = "BANANE"
MOT_JOUEUR = ""

MAX_ERREUR = 10
NB_ERREUR = 0

# =============================================================================
# ==                        F O N C T I O N S                                ==
# =============================================================================

def AfficheAide():

    print("\n\n")
    print(""" 
+--------------+
| Jeu du Pendu | 
+--------------+

A chaque tour saisissez une lettre pour deviner le mot.
Si votre lettre est dans le mot, elle saffichera dans le mot à deviner.
Si elle n'est pas dans le mot alors vous perdu chance, et lorsque vous avez
utilisé toutes vos chances vous serrez pendu !

Voici la liste de mots clefs spéciaux:

AIDE : Affiche l'aide que vous voyez.
QUIT : Pour quitter le programme.

LIST : Liste toutes les lettres déjà proposées

    """)

        
def ListeLettresProposees():
    """
    Fonction qui liste les lettres proposées
    """
    global LETTRES_PROPOSEES

    print("\n")
    print("Liste des lettres proposées :")
    print("")

    if len(LETTRES_PROPOSEES) == 0:
        print("   Vous n'avez proposé aucune lettre !\n\n")
        return

    LETTRES_PROPOSEES.sort()

    cpt = 0
    for l in LETTRES_PROPOSEES:
        print("  %c  "%(l,), end='\t')
        
        if cpt % 4 == 3:
            print('\n')

        cpt += 1

    print('\n')

    #print(LETTRES_PROPOSEES)
    


def EstDejaProposee(lettre):
    """
    Cette fonction vérifie si la lettre a déjà été proposée.
    Si la lettre a été proposée, alors la fonction retourne False
    Sinon la lettre sera ajoutée aux lettres déjà proposées et la fonction retoure True
    """

    global LETTRES_PROPOSEES

    l = lettre.upper()[0]

    if l in LETTRES_PROPOSEES:
        return True

    LETTRES_PROPOSEES.append(l)

    return False

def EstDansLeMot(lettre):
    """
    Cette fonction s'occupe de vérifier si une lettre
    appartient au mot à deviner 
    """
    global MOT_A_DEVINER, MOT_JOUEUR

    if lettre in MOT_A_DEVINER:
        i = 0
        while True:
            i = MOT_A_DEVINER.find(lettre, i)
            if i<0:
                break
            MOT_JOUEUR = MOT_JOUEUR[ 0:i ]+lettre[ 0 ]+MOT_JOUEUR[ i+1: ]
            i += 1
        return  True
    else:
        return False

def EstCeQueJaiGagne():
    """
    Cette fonction vérifie si le mot a été deviné
    """ 
    global MOT_JOUEUR

    if "." in MOT_JOUEUR:
        return False

    return True



def InitMotJoueur():

    global MOT_JOUEUR, MOT_A_DEVINER, NB_ERREUR

    MOT_A_DEVINER = pendu_dico.DonneMoiUnMot()
    MOT_JOUEUR = "." * len(MOT_A_DEVINER)
    NB_ERREUR = 0

def AfficheLeMotADeviner():

    global MOT_JOUEUR

    print("+-%s-+"%("---"*len(MOT_JOUEUR),) )

    print("| ",end='')

    for l in MOT_JOUEUR:
        print(" %c "%(l,), end='')

    print(" |")
    
    print("+-%s-+"%("---"*len(MOT_JOUEUR),) )

    print("\n")




def PendLe():
    """DonneMoiUnMot
    Ajouter 1 au nombre d'erreur
    Affiche la potence du pendu en fonction du nombre d'erreur
    Retourne True, si le nombre d'erreur max est atteint.
    """

    global NB_ERREUR, MAX_ERREUR

    NB_ERREUR += 1
    
    print(pendu_dessin.SEQUENCE_PENDU[NB_ERREUR])

    if NB_ERREUR >= MAX_ERREUR:
        print("T'es pendu ahahah !")
        return True

    return False


# =============================================================================
# ==            P R O G R A M M E   P R I N C I P A L E                      ==
# =============================================================================

print("\n\n********************")
print("* P E N D U  V 0.1 *")
print("********************\n")

print(" > Pour l'aide saisir AIDE\n")

InitMotJoueur()

print(pendu_dessin.SEQUENCE_PENDU[0])

run = True

while run:

    AfficheLeMotADeviner()

    print("\nSaisissez votre lettre :", end='')

    lettre = input('? ')
    lettre = lettre.upper()

    # test du vide
    if len(lettre) == 0:
        print(" [!] Veuillez saisir une lettre ou un mot clef !")
        continue

    # Traitement des mots clefs spéciaux
    if lettre == "QUIT" or lettre == "QQ":
        run = False
        continue

    if lettre == "AIDE":
        AfficheAide()
        continue

    if lettre == "LIST":
        ListeLettresProposees()
        continue

    # Traitement de la lettre
    if len(lettre) > 1:
        print(" [-] Mot clef inexistant, pour deviner le mot saisir une seule lettre")
        continue

    # Teste si la à déjà été utilisée
    if EstDejaProposee(lettre) :
        print(" [!] Lettre déjà proposée !")
        continue

    if not EstDansLeMot(lettre):
        print("Pas de bol, tente autre chose !")
        if PendLe():
            run = False
        continue

    if EstCeQueJaiGagne():
        AfficheLeMotADeviner()
        print("Bravo tu as gagné sans être pendu !")
        run = False
        continue

    




print("Fin du programme, salut !")

