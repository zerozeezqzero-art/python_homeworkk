from geometry import FourSides, Rectangle, Square, Rhombus, DegreessError, SideError
def menu():
    old_obj = None
    obj = None
    while True:
        b = int(
            input(
                "что вы хотите сделать\n создать обьект - 1\n сложить площади обьектов - 2\n вычесть площади обьектов - 3\n сравнить обьекты - 4\n"
            )
        )

        if b == 1:
            n = int(
                input(
                    "выберите какой обьект хотите создать\n 1 - четырехугольник\n 2 - прямоугольник\n 3 - квадрат\n 4 - ромб\n"
                )
            )

            if n == 1:
                data = input("Введите 4 стороны и 4 угла через пробел: ").split()
                values = [float(x) for x in data]
                obj = FourSides(
                    values[0],
                    values[1],
                    values[2],
                    values[3],
                    values[4],
                    values[5],
                    values[6],
                    values[7],
                )

            elif n == 2:
                data = input("Введите 4 стороны и 4 угла через пробел: ").split()
                values = [float(x) for x in data]
                obj = Rectangle(
                    values[0],
                    values[1],
                    values[2],
                    values[3],
                    values[4],
                    values[5],
                    values[6],
                    values[7],
                )

            elif n == 3:
                data = input("Введите 4 стороны и 4 угла через пробел: ").split()
                values = [float(x) for x in data]
                obj = Square(
                    values[0],
                    values[1],
                    values[2],
                    values[3],
                    values[4],
                    values[5],
                    values[6],
                    values[7],
                )

            elif n == 4:
                data = input("Введите 4 стороны и 4 угла через пробел: ").split()
                values = [float(x) for x in data]
                obj = Rhombus(
                    values[0],
                    values[1],
                    values[2],
                    values[3],
                    values[4],
                    values[5],
                    values[6],
                    values[7],
                )

            print(f"Обьект создан\nплощадь - {obj.area()} ")

            if old_obj == None:
                old_obj = obj
        if b == 2:
            if old_obj == None:
                print("Создайте второй обьект")
            else:
                print(old_obj + obj)
                break

        if b == 3:
            if old_obj == None:
                print("Создайте второй обьект") 
            
            print(abs(old_obj - obj))
            break
        if b == 4:
            if old_obj == None:
                print("Создайте второй обьект")
            
            print(f" {obj.__class__.__name__} {max(obj.area(),old_obj.area())} > {old_obj.__class__.__name__} {min(obj.area(),old_obj.area())}")
            break