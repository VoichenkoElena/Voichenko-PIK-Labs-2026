import sys
import math
def get_coef(index, prompt):
    while True:
        try:
            coef_str = sys.argv[index]
        except IndexError:
            print(prompt)
            coef_str = input()
        try:
            return float(coef_str)
        except ValueError:
            print('Ошибка [ValueError]: введите действительное число.')
            if index < len(sys.argv):
                del sys.argv[index]
def resh_yr(a, b, c):
    t_list = []
    if a == 0.0:
        if b != 0.0:
            t_list.append(-c / b)
        return t_list
    D = b * b - 4.0 * a * c
    if D == 0.0:
        t_list.append(-b / (2.0 * a))
    elif D > 0.0:
        sqrt_D = math.sqrt(D)
        t_list.append((-b + sqrt_D) / (2.0 * a))
        t_list.append((-b - sqrt_D) / (2.0 * a))
    return t_list
def get_t(A, B, C):
    t_all = []
    t_list = resh_yr(A, B, C)
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
    return t_unique
def print_t(t_list):
    n = len(t_list)
    if n == 0:
        print('Нет корней')
    elif n == 1:
        print('Один корень: {}'.format(t_list[0]))
    elif n == 2:
        print('Два корня: {} и {}'.format(t_list[0], t_list[1]))
    elif n == 3:
        print('Три корня: {}, {} и {}'.format(t_list[0], t_list[1], t_list[2]))
    elif n == 4:
        print('Четыре корня: {}, {}, {} и {}'.format(
            t_list[0], t_list[1], t_list[2], t_list[3]))
def main():
    try:
        A = get_coef(1, 'Введите коэффициент A:')
        B = get_coef(2, 'Введите коэффициент B:')
        C = get_coef(3, 'Введите коэффициент C:')
    except Exception as e:
        print('Ошибка [{}]: {}'.format(type(e).__name__, e))
        return
    if A == 0.0 and B == 0.0 and C == 0.0:
        print('x может быть любым')
        return
    try:
        t_list = get_t(A, B, C)
    except ValueError as e:
        print('Ошибка [ValueError]: {}'.format(e))
        return
    except OverflowError as e:
        print('Ошибка [OverflowError]: {}'.format(e))
        return
    except Exception as e:
        print('Ошибка [{}]: {}'.format(type(e).__name__, e))
        return
    print_t(t_list)
if __name__ == "__main__":
    main()