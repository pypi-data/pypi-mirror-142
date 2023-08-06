VIOLET = '\033[95m'
CYAN = '\033[96m'
CYAN_FONCÉ = '\033[36m'
BLEU = '\033[94m'
VERT = '\033[92m'
JAUNE = '\033[93m'
ROUGE = '\033[91m'
BLANC = '\033[37m'
NOIR = '\033[30m'
MAGENTA = '\033[35m'
GRAS = '\033[1m'
DIM = '\033[2m'
NORMAL = '\033[22m'
SOULIGNE = '\033[4m'
FIN = '\033[0m'
def depuis_rgb(rouge: int, vert: int, bleu: int, texte: str):
    if rouge >= 256:
        return print('\033[38;2;235;162;52mATTENTION: Utilisez une valeur de couleur RGB en dessous de 255.' + '\033[22m')
    if vert >= 256:
        return print('\033[38;2;235;162;52mATTENTION: Utilisez une valeur de couleur RGB en dessous de 255.' + '\033[22m')
    if bleu >= 256:
        return print('\033[38;2;235;162;52mATTENTION: Utilisez une valeur de couleur RGB en dessous de 255.' + '\033[22m')
    return "\033[38;2;{};{};{}m{}".format(rouge, vert, bleu, texte)