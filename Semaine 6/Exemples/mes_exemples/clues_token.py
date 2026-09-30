import math
# il est possible de donner des indices à python (et pycharm) sur les

# Pour les fonctions,
# Dans cet exemple, j'indique que le premier nb devrait être une str et que le deusieme devrait etre un float
# la fleche (->) indique le type de retour attendu
def afficher_nombre(nom: str, nombre: float) -> float:
    print(f"Bonjour {nom}! Votre nombre est {nombre}")
    return nombre ** 2


# ceci indique a pycharm qu'il s'attend a ce que la fonction soit appellée avec une str  et un float et devrait
# retourner un float
print(afficher_nombre("Bob Ross", 42.1))

# si je ne spécifie pas les bons types, pycharm va me donner un avertissement, cependant ce sont que des indinces
# donc pas d'erreur
print(afficher_nombre(42, 3))

# On peut faire ceci pour toute déclaration de variables
mon_int: int = 2
mon_float: float = 42.0
phrase: str = "une str"
# etc...

# les builtins de pythons incluent tous les indices de type
math.sqrt(5.0)