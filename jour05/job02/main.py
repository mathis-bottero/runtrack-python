def draw_rectangle(width, height) :
    la = "-" * (width - 2)
    space = " " * (width - 2)
    print(f"|{la}|")
    for k in range((height - 2)):
        print(f"|{space}|")
    print(f"|{la}|")

draw_rectangle(10, 3)