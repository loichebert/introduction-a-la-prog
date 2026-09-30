from modulea import *
from moduleb import *
# Bonjour existe dans les deux modules, la derniere version importée sera utilisé (pankake stacking)
bonjour()

# dans les modules importés, faire un print(__name__) retourne le nom du module
# faire la meme chose dans le script principal (celui exécuté) va retourner "__main__"
print(__name__)

# on peut utiliser ceci pour verifier quel le code soit seulement exécuté dans le principal
if __name__ == "__main__":
    print("main")