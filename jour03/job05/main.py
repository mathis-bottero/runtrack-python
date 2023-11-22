def calcule(num1, operator, num2):
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Erreur: Division par zéro"
    elif operator == '%':
        if num2 != 0:
            result = num1 % num2
        else:
            return "Erreur: Modulo par zéro"
    else:
        return "Opérateur non valide"
    
    print(result)

calcule(5, '+', 5)