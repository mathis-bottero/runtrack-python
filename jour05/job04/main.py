def tapis(n):
    border = "+" + "-" * n + "+"
    print(f"{border}")
    for i in range(n):
        interieur = "#" * (n-i-1) + " " + "#" * i
        print(f"|{interieur}|")
    print(f"{border}")


tapis(10)