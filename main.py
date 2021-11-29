try:
    indice_valeur_max = int(0)
    valeur_max = 0
    n = int(input("Saisir le nombre de valeur du tableau"))
    tab = {}

    for i in range(n):
        print("Veillez saisir la valeur", i, "du tableau")
        tab[i] = int(input())
        if i == 0:
            valeur_max = tab[i]
        if valeur_max < tab[i]:
            valeur_max = tab[i]
            indice_valeur_max = i

    print("La valeur max est:", valeur_max," son indice est", indice_valeur_max)
except ValueError:
    print("Mauvaise Saisie")