from os import *

# Console
def couleur(rouge: int, vert: int, bleu: int, texte: str):
    if rouge >= 256:
        return print(couleur(235, 192, 52, 'ATTENTION: Utilisez une valeur de couleur RGB en dessous de 255.') + couleur(203, 203, 203, ''))
    if vert >= 256:
        return print(couleur(235, 192, 52, 'ATTENTION: Utilisez une valeur de couleur RGB en dessous de 255.') + couleur(203, 203, 203, ''))
    if bleu >= 256:
        return print(couleur(235, 192, 52, 'ATTENTION: Utilisez une valeur de couleur RGB en dessous de 255.') + couleur(203, 203, 203, ''))
    return "\033[38;2;{};{};{}m{}".format(rouge, vert, bleu, texte)
def txt(nombre: str):
    return int(nombre)
def num(nombre: int):
    return str(nombre)
def afficher(texte: str):
    return print(f"{texte}{couleur(203, 203, 203, '')}")
def demander(question: str):
    return input('{}\n'.format(question) + couleur(203, 203, 203, ' '))
def erreur(erreur: str):
    return print(couleur(255, 0, 0, 'ERREUR: {}'.format(erreur)) + couleur(203, 203, 203, ' '))
def attention(texte: str):
    return print(couleur(235, 192, 52, 'ATTENTION: {}'.format(texte)) + couleur(203, 203, 203, ' '))
def succes(texte: str):
    return print(couleur(45, 166, 49, 'SUCCÈS: {}'.format(texte)) + couleur(203, 203, 203, ' '))
def conseil(texte: str):
    return print(couleur(80, 140, 212, 'CONSEIL: {}'.format(texte)) + couleur(203, 203, 203, ' '))
def commencePar(texte: str, mot: str):
    return texte.startswith(mot)
def finitPar(texte: str, mot: str):
    return texte.endswith(mot)
def cls():
    if name == "nt":
        system("cls")
    else:
        system("clear")

# Fichier
def ouvrir(fichier: str):
    return open(file=fichier)

# Vrai/Faux
def Vrai():
    return True
def Faux():
    return False

# Condition
def si(valeur: bool):
    if valeur:
        return valeur
    else:
        return valeur

# Processeurs logique
def égale(valeur1: int, valeur2: int):
    if valeur1 == valeur2:
        return True
    else:
        return False
def différentDe(valeur1: int, valeur2: int):
    if valeur1 != valeur2:
        return True
    else:
        return False
def plusGrand(valeur1: int, valeur2: int):
    if valeur1 > valeur2:
        return True
    else:
        return False
def plusPetit(valeur1: int, valeur2: int):
    if valeur1 < valeur2:
        return True
    else:
        return False 
def égalePlusGrand(valeur1: int, valeur2: int):
    if valeur1 >= valeur2:
        return True
    else:
        return False
def égalePlusPetit(valeur1: int, valeur2: int):
    if valeur1 <= valeur2:
        return True
    else:
        return False
def AND(A: int, B: int):
    return A & B
def NOT(A: int):
    return ~A+2
def XOR(x: int, y: int):
    return bool((x and not y) or (not x and y))
def NAND(A: int, B: int):
    return NOT(AND(A, B))
def OR(A: int, B: int):
    return A | B
def NOR(A: int, B: int):
    return NOT(OR(A, B))
def XNOR(A: int, B: int):
    return NOT(XOR(A, B))