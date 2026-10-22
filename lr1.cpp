#include <iostream>
#include <vector>
#include <cmath>
class Biquadrat {
private:
    double coef_A;
    double coef_B;
    double coef_C;
    std::vector<double> t_all;
public:
    Biquadrat()
        : coef_A(0.0), coef_B(0.0), coef_C(0.0), t_all() {}

    double get_coef(const char* prompt) {
        double coef = 0.0;
        while (true) {
            std::cout << prompt;
            std::cin >> coef;
            if (std::cin.fail()) {
                std::cin.clear();
                std::cin.ignore(10000, '\n');
                std::cout << "Ошибка: введите действительное число.\n";
            } else {
                return coef;
            }
        }
    }
    void get_coefs() {
        coef_A = get_coef("Введите коэффициент A: ");
        coef_B = get_coef("Введите коэффициент B: ");
        coef_C = get_coef("Введите коэффициент C: ");
    }
    bool vse_nyli() const {
        return coef_A == 0.0 && coef_B == 0.0 && coef_C == 0.0;
    }
    std::vector<double> resh_yr(double a, double b, double c) {
        std::vector<double> t_list;
        double D = b * b - 4.0 * a * c;
        if (D == 0.0) {
            t_list.push_back(-b / (2.0 * a));
        } else if (D > 0.0) {
            double sqrt_D = std::sqrt(D);
            t_list.push_back((-b + sqrt_D) / (2.0 * a));
            t_list.push_back((-b - sqrt_D) / (2.0 * a));
        }
        return t_list;
    }
    void get_t() {
        t_all.clear();
        std::vector<double> t_list = resh_yr(coef_A, coef_B, coef_C);
        for (std::size_t i = 0; i < t_list.size(); ++i) {
            double t = t_list[i];
            if (t < 0.0) {
                continue;
            } else if (t == 0.0) {
                t_all.push_back(0.0);
            } else {
                double sqrt_t = std::sqrt(t);
                t_all.push_back(sqrt_t);
                t_all.push_back(-sqrt_t);
            }
        }
        std::vector<double> t_unique;
        for (std::size_t i = 0; i < t_all.size(); ++i) {
            bool found = false;
            for (std::size_t j = 0; j < t_unique.size(); ++j) {
                if (t_unique[j] == t_all[i]) {
                    found = true;
                    break;
                }
            }
            if (!found) {
                t_unique.push_back(t_all[i]);
            }
        }
        for (std::size_t i = 0; i < t_unique.size(); ++i) {
            for (std::size_t j = 0; j + 1 < t_unique.size() - i; ++j) {
                if (t_unique[j] > t_unique[j + 1]) {
                    double tmp = t_unique[j];
                    t_unique[j] = t_unique[j + 1];
                    t_unique[j + 1] = tmp;
                }
            }
        }
        t_all = t_unique;
    }
    void print_t() {
        if (t_all.empty()) {
            std::cout << "Нет корней\n";
        } else if (t_all.size() == 1) {
            std::cout << "Один корень: " << t_all[0] << '\n';
        } else if (t_all.size() == 2) {
            std::cout << "Два корня: " << t_all[0]
                      << " и " << t_all[1] << '\n';
        } else if (t_all.size() == 3) {
            std::cout << "Три корня: " << t_all[0] << ", "
                      << t_all[1] << " и " << t_all[2] << '\n';
        } else if (t_all.size() == 4) {
            std::cout << "Четыре корня: " << t_all[0] << ", "
                      << t_all[1] << ", " << t_all[2]
                      << " и " << t_all[3] << '\n';
        }
    }
};
int main() {
    Biquadrat solver;
    solver.get_coefs();
    if (solver.vse_nyli()) {
        std::cout << "x может быть любым\n";
    } else {
        solver.get_t();
        solver.print_t();
    }
    return 0;
}