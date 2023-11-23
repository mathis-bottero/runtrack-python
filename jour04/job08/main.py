def calculate(list):
    sum = 0
    for number in list:
        if number % 2 == 0:
            sum += number
    return sum

L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]
resultat = calculate(L)
print(resultat)