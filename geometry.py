import math

class DegreessError(Exception):
    pass


class SideError(Exception):
    pass


class FourSides:

    def __init__(self, side1, side2, side3, side4, deg1, deg2, deg3, deg4):
        sidelist = [side1, side2, side3, side4]
        deglist = [deg1, deg2, deg3, deg4]
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.side4 = side4
        self.deg1 = deg1
        self.deg2 = deg2
        self.deg3 = deg3
        self.deg4 = deg4
        if any(i <= 0 for i in deglist):
            raise DegreessError("Угол не может быть отрицальной или равной нулю")
        if any(i <= 0 for i in sidelist):
            raise SideError("Сторона не может быть отрицальной или равной нулю")
        if deg1 + deg2 + deg3 + deg4 != 360:
            raise DegreessError("Сумма углов должна быть равна 360 градусам")

        if any(side >= sum(sidelist) - side for side in sidelist):
            raise SideError("Одна из сторон слишком велика")

    def area(self):
        return 0.5 * (
            self.side1 * self.side2 * math.sin(math.radians(self.deg2))
            + self.side3 * self.side4 * math.sin(math.radians(self.deg4))
        )

    def __add__(self, oth_obj):
        return self.area() + oth_obj.area()

    def __sub__(self, oth_obj):
        return self.area() - oth_obj.area()

    def __repr__(self):
        pass


class Rectangle(FourSides):
    def __init__(self, side1, side2, side3, side4, deg1, deg2, deg3, deg4):
        super().__init__(side1, side2, side3, side4, deg1, deg2, deg3, deg4)
        if not all(i == 90 for i in [deg1, deg2, deg3, deg4]):
            raise DegreessError("Все углы должны быть 90 градусов")

    def area(self):
        return self.side1 * self.side2

    def __add__(self, oth_obj):
        return super().__add__(oth_obj)

    def __sub__(self, oth_obj):
        return super().__sub__(oth_obj)

    def __repr__(self):
        return super().__repr__()


class Square(Rectangle):
    def __init__(self, side1, side2, side3, side4, deg1, deg2, deg3, deg4):
        super().__init__(side1, side2, side3, side4, deg1, deg2, deg3, deg4)
        if len({side1, side2, side3, side4}) > 1:
            raise SideError("Все стороны должны быть равны")

    def area(self):
        return self.side1**2

    def __add__(self, oth_obj):
        return super().__add__(oth_obj)

    def __sub__(self, oth_obj):
        return super().__sub__(oth_obj)

    def __repr__(self):
        return super().__repr__()


class Rhombus(FourSides):
    def __init__(self, side1, side2, side3, side4, deg1, deg2, deg3, deg4):
        super().__init__(side1, side2, side3, side4, deg1, deg2, deg3, deg4)
        if (deg1 != deg3) or (deg2 != deg4):
            raise DegreessError("Паралельные углы ромба должны быть равны")
        if ((deg1 + deg2) != 180) or ((deg3 + deg4) != 180):
            raise DegreessError("Соседние углы в сумме должны быть 180 градусов")
        if not side1 == side2 == side3 == side4:
            raise SideError("Все стороны ромба должны быть равны")

    def area(self):
        return self.side1**2 * math.sin(math.radians(self.deg1))

    def __add__(self, oth_obj):
        return super().__add__(oth_obj)

    def __sub__(self, oth_obj):
        return super().__sub__(oth_obj)

    def __repr__(self):
        return super().__repr__()
    
