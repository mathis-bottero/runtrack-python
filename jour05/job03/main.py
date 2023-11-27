def triangle(n) :
    for i in range(n - 1):
        space = "/" + "  " * i + "\\"
        print(f"{space: ^{n*2}}")
    space = "_" * (n-1) * 2
    print(f"/{space}\\")

n = int(input("Entrer un entier strictement positif: "))
triangle(n)