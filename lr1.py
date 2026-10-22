import sys
import math
try:
    if len(sys.argv) > 1:
        A = float(sys.argv[1])
    else:
        print('Введите коэффициент A:')
        A = float(input())
except ValueError:
    print('Ошибка [ValueError]: коэффициент A должен быть числом')
    sys.exit(1)
try:
    if len(sys.argv) > 2:
        B = float(sys.argv[2])
    else:
        print('Введите коэффициент B:')
        B = float(input())
except ValueError:
    print('Ошибка [ValueError]: коэффициент B должен быть числом')
    sys.exit(1)
try:
    if len(sys.argv) > 3:
        C = float(sys.argv[3])
    else:
        print('Введите коэффициент C:')
        C = float(input())
except ValueError:
    print('Ошибка [ValueError]: коэффициент C должен быть числом')
    sys.exit(1)
if A == 0.0 and B == 0.0 and C == 0.0:
    print('x может быть любым')
else:
    t_list = []
    if A == 0.0:
        if B != 0.0:
            t_list.append(-C / B)
    else:
        D = B * B - 4.0 * A * C
        if D == 0.0:
            t_list.append(-B / (2.0 * A))
        elif D > 0.0:
            sqrt_D = math.sqrt(D)
            t_list.append((-B + sqrt_D) / (2.0 * A))
            t_list.append((-B - sqrt_D) / (2.0 * A))
    t_all = []
    for t in t_list:
        if t < 0.0:
            continue
        elif t == 0.0:
            t_all.append(0.0)
        else:
            sqrt_t = math.sqrt(t)
            t_all.append(sqrt_t)
            t_all.append(-sqrt_t)
    t_unique = sorted(set(t_all))
    n = len(t_unique)
    if n == 0:
        print('Нет корней')
    elif n == 1:
        print('Один корень: {}'.format(t_unique[0]))
    elif n == 2:
        print('Два корня: {} и {}'.format(t_unique[0], t_unique[1]))
    elif n == 3:
        print('Три корня: {}, {} и {}'.format(t_unique[0], t_unique[1], t_unique[2]))
    elif n == 4:
        print('Четыре корня: {}, {}, {} и {}'.format(
            t_unique[0], t_unique[1], t_unique[2], t_unique[3]))