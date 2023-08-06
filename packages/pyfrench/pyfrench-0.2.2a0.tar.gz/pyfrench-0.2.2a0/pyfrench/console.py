def commencePar(texte: str, mot: str):
    return texte.startswith(mot)
def finitPar(texte: str, mot: str):
    return texte.endswith(mot)

# Fichier
def ouvrir(fichier: str):
    return open(file=fichier)

Vrai = True
Faux = False

# Condition
def si(valeur: bool):
    return valeur
def replacePar(texte: str, caractère1: str, caractère2: str):
    return texte.replace(caractère1, caractère2)

# Lien
def google(recherche: str):
    return f'https://www.google.com/search?q={recherche.replace(" ", "+")}'
def youtube(recherche: str):
    return f'https://www.youtube.com/watch?v={recherche}'