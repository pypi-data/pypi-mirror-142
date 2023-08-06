from pyfrench import couleur

def afficher(texte: str):
    return print(str(texte) + couleur.FIN)
def demander(question: str):
    return input('{}\n'.format(question) + couleur.FIN)