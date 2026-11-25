from lab_python_oop import Cube, Cone, Tetrahedron
import rich

def main():
    fig1 = Cube(2)
    fig2 = Cube(5)
    fig3 = Cone(3, 4)
    fig4 = Cone(1, 2)
    fig5 = Tetrahedron(3)
    fig6 = Tetrahedron(6)
    fig7 = Cube(10)
    fig8 = Cone(2, 5)

    print(fig1)
    print(fig2)
    print(fig3)
    print(fig4)
    print(fig5)
    print(fig6)
    print(fig7)
    print(fig8)

    print("\n--- Демонстрация работы методов ---")
    print(f"Тип фигуры 1: {fig1.get_type()}")
    print(f"Объем фигуры 1: {fig1.volume():.2f}")
    print(f"Площадь фигуры 1: {fig1.area():.2f}")

    rich.print("[bold green]Демонстрация работы внешнего пакета rich[/bold green]")

    print("\nВыберите фигуру для демонстрации:")
    print("1 - Куб")
    print("2 - Конус")
    print("3 - Тетраэдр")
    choice = input("Ваш выбор (1/2/3): ")

    try:
        if choice == '1':
            s = float(input("Введите сторону куба: "))
            fig = Cube(s)
            print(fig)
            print("Тип фигуры:", fig.get_type())
        elif choice == '2':
            r = float(input("Введите радиус конуса: "))
            h = float(input("Введите высоту конуса: "))
            fig = Cone(r, h)
            print(fig)
            print("Тип фигуры:", fig.get_type())
        elif choice == '3':
            e = float(input("Введите ребро тетраэдра: "))
            fig = Tetrahedron(e)
            print(fig)
            print("Тип фигуры:", fig.get_type())
        else:
            print("Неверный выбор.")
    except ValueError as e:
        print(f"Ошибка [{type(e).__name__}]: {e}")

if __name__ == "__main__":
    main()