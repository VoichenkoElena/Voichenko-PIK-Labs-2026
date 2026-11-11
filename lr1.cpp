#include <iostream>
#include <cmath>
#include <limits>
class U {
public:
    double a, b, c;
    double vvod_chisla(const char* prompt) {
        double x;
        while (true) {
            std::cout << prompt;
            std::cin >> x;
            if (std::cin.fail()) {
                std::cin.clear();
                std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); // Очищаем буфер
                std::cout << "Ошибка1: введите число" << std::endl;
            } else {
                return x;
            }
        }
    }
    void vvod() {
        a = vvod_chisla("Введите A: ");
        b = vvod_chisla("Введите B: ");
        c = vvod_chisla("Введите C: ");
    }
    void kor(double t) {
        if (t < 0) return;
        if (t == 0) {
            std::cout << "x = 0" << std::endl;
        } else {
            std::cout << "x = " << std::sqrt(t) << std::endl;
            std::cout << "x = " << -std::sqrt(t) << std::endl;
        }
    }
    void reshenie() {
        if (a == 0 && b == 0 && c == 0) {
            std::cout << "x может быть любым" << std::endl;
            return;
        }
        if (a == 0) {
            if (b != 0) kor(-c / b);
            return;
        }
        double D = b * b - 4 * a * c;
        std::cout << "D = " << D << std::endl;

        if (D < 0) {
            std::cout << "Нет корней" << std::endl;
        } else if (D == 0) {
            kor(-b / (2 * a));
        } else {
            kor((-b + std::sqrt(D)) / (2 * a));
            kor((-b - std::sqrt(D)) / (2 * a));
        }
    }
};
int main() {
    setlocale(LC_ALL, "ru_RU.UTF-8");
    U obj;
    obj.vvod();
    obj.reshenie();
    return 0;
}