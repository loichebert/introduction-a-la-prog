for nb in range(600, 700, 2):

     nb_str= str(nb)
     premier_nb = int(nb_str[0])
     deuxieme_nb = int(nb_str[1])
     troisieme_nb = int(nb_str[2])
# on vérifie qu'un des nb est 3
     if  premier_nb == 3 or deuxieme_nb == 3 or troisieme_nb == 3:
         # on vérifie si la somme des 3 chiffres est 11
         if premier_nb + deuxieme_nb + troisieme_nb == 11:
             # on a trouvé la réponse, on sort de la boucle
             print(f"le nombre recherché est {nb}")
             break
