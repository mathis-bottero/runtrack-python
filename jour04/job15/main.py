def tri(arr):
    n = 0
    while True:
        i = 0
        try:
            while True:
                if arr[i] > arr[i + 1]:
                    temp = arr[i]
                    arr[i] = arr[i + 1]
                    arr[i + 1] = temp
                i += 1
        except IndexError:
            pass

        n += 1
        fin_de_liste = True
        for _ in arr:
            fin_de_liste = False
            break

        if fin_de_liste or n == 1:
            break

L = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

arrondi = 1
liste_arrondie = [int(x + 0.5) for x in L]

tri(liste_arrondie)

print(liste_arrondie)