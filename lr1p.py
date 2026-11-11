def vvod(name):
    while True:
        try:
            return float(input("Введите " + name + ": "))
        except ValueError:
            print("Ошибка [ValueError]: введите число")
def kor(t):
    if t < 0: print("Нет корней")
    elif t == 0: print("x = 0")
    else:
        print("x =", t ** 0.5)
        print("x =", -(t ** 0.5))
def main():
    a = vvod("A")
    b = vvod("B")
    c = vvod("C")
    if a == 0 and b == 0 and c == 0:
        print("x может быть любым")
    elif a == 0:
        if b != 0: kor(-c / b)
    else:
        D = b * b - 4 * a * c
        print("D =", D)
        if D < 0: print("Нет корней")
        elif D == 0: kor(-b / (2 * a))
        else:
            kor((-b + D ** 0.5) / (2 * a))
            kor((-b - D ** 0.5) / (2 * a))
if __name__ == "__main__":
    main()