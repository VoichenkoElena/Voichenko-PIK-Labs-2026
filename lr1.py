while True:
    try:
        a = float(input("Введите A: "))
        break
    except ValueError:
        print("Ошибка [ValueError]: введите число")
while True:
    try:
        b = float(input("Введите B: "))
        break
    except ValueError:
        print("Ошибка [ValueError]: введите число")
while True:
    try:
        c = float(input("Введите C: "))
        break
    except ValueError:
        print("Ошибка [ValueError]: введите число")
if a == 0 and b == 0 and c == 0:
    print("x может быть любым")
else:
    if a == 0:
        if b != 0:
            t = -c / b
            if t < 0:
                print("Нет корней")
            elif t == 0:
                print("x = 0")
            else:
                print("x =", t ** 0.5)
                print("x =", -(t ** 0.5))
    else:
        D = b * b - 4 * a * c
        print("D =", D)
        if D < 0:
            print("Нет корней")
        elif D == 0:
            t = -b / (2 * a)
            if t < 0:
                print("Нет корней")
            elif t == 0:
                print("x = 0")
            else:
                print("x =", t ** 0.5)
                print("x =", -(t ** 0.5))
        else:
            t1 = (-b + D ** 0.5) / (2 * a)
            t2 = (-b - D ** 0.5) / (2 * a)
            
            if t1 > 0:
                print("x =", t1 ** 0.5)
                print("x =", -(t1 ** 0.5))
            elif t1 == 0:
                print("x = 0")
            if t2 > 0:
                print("x =", t2 ** 0.5)
                print("x =", -(t2 ** 0.5))
            elif t2 == 0:
                print("x = 0")