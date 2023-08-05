import math
import random


class Vec4:
    COMPARISON_TYPE = "POS"

    def __init__(self, x=0.0, y=0.0, w=0.0, h=0.0, pos=None):
        if pos is None:
            self.x = x
            self.y = y
            self.w = w
            self.h = h
        else:
            if type(pos) is Vec4:
                self.x = pos.x
                self.y = pos.y
                self.w = pos.w
                self.h = pos.h
            elif (type(pos) is list or type(pos) is tuple) and len(pos) == 4:
                self.x = pos[0]
                self.y = pos[1]
                self.w = pos[2]
                self.h = pos[3]
            else:
                raise Exception("TypeError: pos argumennt can only be Vec4, (int, int, int, int), (float, float, "
                                "float, float), [int, int, int, int], [float, float, float, float], int or float")

    def getX(self):
        return self.x

    def setX(self, x):
        self.x = x

    def getY(self):
        return self.y

    def setY(self, y):
        self.y = y

    def getW(self):
        return self.w

    def setW(self, w):
        self.w = w

    def getH(self):
        return self.h

    def setH(self, h):
        self.h = h

    def getPos(self):
        return self.x, self.y, self.w, self.h

    def setPos(self, newPos):
        self.x = newPos.x
        self.y = newPos.y
        self.w = newPos.w
        self.h = newPos.h

    def add(self, x=0.0, y=0.0, w=0.0, h=0.0, glob=0.0, pos=None):
        if pos is None:
            self.x = self.x + x + glob
            self.y = self.y + y + glob
            self.w = self.w + w + glob
            self.h = self.h + h + glob
        else:
            if type(pos) == Vec4:
                self.x = self.x + pos.x
                self.y = self.y + pos.y
                self.w = self.w + pos.w
                self.h = self.h + pos.h
            elif (type(pos) == tuple or type(pos) == list) and len(pos) == 4:
                self.x = self.x + pos[0]
                self.y = self.y + pos[1]
                self.w = self.w + pos[2]
                self.h = self.h + pos[3]
            else:
                raise Exception("TypeError: only Vec4, (int, int, int, int), (float, float, float, float), [int, int, "
                                "int, int], [float, float, float, float], int or float can be added to a Vec4")

    def sub(self, x=0.0, y=0.0, w=0.0, h=0.0, glob=0.0, pos=None):
        if pos is None:
            self.x = self.x - x - glob
            self.y = self.y - y - glob
            self.w = self.w - w - glob
            self.h = self.h - h - glob
        else:
            if type(pos) == Vec4:
                self.x = self.x - pos.x
                self.y = self.y - pos.y
                self.w = self.w - pos.w
                self.h = self.h - pos.h
            elif (type(pos) == tuple or type(pos) == list) and len(pos) == 4:
                self.x = self.x - pos[0]
                self.y = self.y - pos[1]
                self.w = self.w - pos[2]
                self.h = self.h - pos[3]
            else:
                raise Exception("TypeError: only Vec4, (int, int, int, int), (float, float, float, float), [int, int, "
                                "int, int], [float, float, float, float], int or float can be subtracted from a Vec4")

    def div(self, x=1.0, y=1.0, w=1.0, h=1.0, glob=1.0, pos=None):
        if pos is None:
            self.x = self.x / x / glob
            self.y = self.y / y / glob
            self.w = self.w / w / glob
            self.h = self.h / h / glob
        else:
            if type(pos) == Vec4:
                self.x = self.x / pos.x
                self.y = self.y / pos.y
                self.w = self.w / pos.w
                self.h = self.h / pos.h
            elif (type(pos) == tuple or type(pos) == list) and len(pos) == 4:
                self.x = self.x / pos[0]
                self.y = self.y / pos[1]
                self.w = self.w / pos[2]
                self.h = self.h / pos[3]
            else:
                raise Exception("TypeError: only Vec4, (int, int, int, int), (float, float, float, float), [int, int, "
                                "int, int], [float, float, float, float], int or float can be divided with a Vec4")

    def mult(self, x=1.0, y=1.0, w=1.0, h=1.0, glob=1.0, pos=None):
        if pos is None:
            self.x = self.x * x * glob
            self.y = self.y * y * glob
            self.w = self.w * w * glob
            self.h = self.h * h * glob
        else:
            if type(pos) == Vec4:
                self.x = self.x * pos.x
                self.y = self.y * pos.y
                self.w = self.w * pos.w
                self.h = self.h * pos.h
            elif (type(pos) == tuple or type(pos) == list) and len(pos) == 4:
                self.x = self.x * pos[0]
                self.y = self.y * pos[1]
                self.w = self.w * pos[2]
                self.h = self.h * pos[3]
            else:
                raise Exception("TypeError: only Vec4, (int, int, int, int), (float, float, float, float), [int, int, "
                                "int, int], [float, float, float, float], int or float can be multiplied with a Vec4")

    def inverse(self, inverseX, inverseY, inverseW, inverseH):
        if inverseX:
            self.x *= -1
        if inverseY:
            self.y *= -1
        if inverseW:
            self.w *= -1
        if inverseH:
            self.h *= -1

    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.w ** 2 + self.h ** 2)

    def normalize(self):
        self.div(glob=self.length())

    def normal(self):
        return self / self.length()

    def clone(self):
        return Vec4(self.x, self.y, self.w, self.h)

    @classmethod
    def randomIntVec(cls, minX=-50, maxX=50, minY=-50, maxY=50, minW=-50, maxW=50, minH=-50, maxH=50):
        x = random.randint(minX, maxX)
        y = random.randint(minY, maxY)
        w = random.randint(minW, maxW)
        h = random.randint(minH, maxH)
        return Vec4(x, y, w, h)

    @classmethod
    def randomVec(cls, minX=-50, maxX=50, minY=-50, maxY=50, minW=-50, maxW=50, minH=-50, maxH=50):
        x = random.randrange(minX, maxX)
        y = random.randrange(minY, maxY)
        w = random.randint(minW, maxW)
        h = random.randint(minH, maxH)
        return Vec4(x, y, w, h)

    @classmethod
    def dist(cls, vectorA, vectorB):
        return math.sqrt((vectorA.x - vectorB.x) ** 2 + (vectorA.y - vectorB.y) ** 2 +
                         (vectorA.w - vectorB.w) ** 2 + (vectorA.h - vectorB.h) ** 2)

    @classmethod
    def lerp(cls, vecA, vecB, step):
        x = (1 - step) * vecA.x + step * vecB.x
        y = (1 - step) * vecA.y + step * vecB.y
        w = (1 - step) * vecA.w + step * vecB.w
        h = (1 - step) * vecA.h + step * vecB.h
        return Vec4(x, y, w, h)

    @classmethod
    def collinear(cls, vecA, vecB, vecC):
        vecAB = vecB - vecA
        vecAC = vecC - vecA
        coefX = vecAB.x / vecAC.x
        coefY = vecAB.y / vecAC.y
        coefW = vecAB.w / vecAC.w
        coefH = vecAB.h / vecAC.h

        return coefX == coefY and coefY == coefW and coefW == coefH

    @classmethod
    def between(cls, vecA, vecB, target):
        result = False
        if Vec4.collinear(vecA, vecB, target):
            if vecA.x <= target.x <= vecB.x and vecA.y <= target.y <= vecB.y and vecA.w <= target.w <= vecB.w \
                    and vecA.h <= target.h <= vecB.h:
                result = True
        return result

    @classmethod
    def setComparisonType(cls, newType):
        """
        :param newType:
        Compare by :

        - LENGTH

        - POS
        """
        if newType == "LENGTH" or newType == "POS":
            Vec4.COMPARISON_TYPE = newType

    def __add__(self, other):
        if type(other) == Vec4:
            result = Vec4(self.x + other.x, self.y + other.y, self.w + other.w, self.h + other.h)
        elif (type(other) == tuple or type(other) == list) and len(other) == 4:
            result = Vec4(self.x + other[0], self.y + other[1], self.w + other[2], self.h + other[3])
        elif type(other) == int or type(other) == float:
            result = Vec4(self.x + other, self.y + other, self.w + other, self.h + other)
        else:
            raise Exception("TypeError: only Vec4, (int, int, int, int), (float, float, float, float), [int, int, "
                            "int, int], [float, float, float, float], int or float can be added to a Vec4")
        return result

    def __sub__(self, other):
        if type(other) == Vec4:
            result = Vec4(self.x - other.x, self.y - other.y, self.w - other.w, self.h - other.h)
        elif (type(other) == tuple or type(other) == list) and len(other) == 4:
            result = Vec4(self.x - other[0], self.y - other[1], self.w - other[2], self.h - other[3])
        elif type(other) == int or type(other) == float:
            result = Vec4(self.x - other, self.y - other, self.w - other, self.h - other)
        else:
            raise Exception("TypeError: only Vec4, (int, int, int, int), (float, float, float, float), [int, int, "
                            "int, int], [float, float, float, float], int or float can be subtracted from a Vec4")
        return result

    def __mul__(self, other):
        if type(other) == Vec4:
            result = Vec4(self.x * other.x, self.y * other.y, self.w * other.w, self.h * other.h)
        elif (type(other) == tuple or type(other) == list) and len(other) == 4:
            result = Vec4(self.x * other[0], self.y * other[1], self.w * other[2], self.h * other[3])
        elif type(other) == int or type(other) == float:
            result = Vec4(self.x * other, self.y * other, self.w * other, self.h * other)
        else:
            raise Exception("TypeError: only Vec4, (int, int, int, int), (float, float, float, float), [int, int, "
                            "int, int], [float, float, float, float], int or float can be multiplied with a Vec4")
        return result

    def __truediv__(self, other):
        if type(other) == Vec4:
            result = Vec4(self.x / other.x, self.y / other.y, self.w / other.w, self.h / other.h)
        elif (type(other) == tuple or type(other) == list) and len(other) == 4:
            result = Vec4(self.x / other[0], self.y / other[1], self.w / other[2], self.h / other[3])
        elif type(other) == int or type(other) == float:
            result = Vec4(self.x / other, self.y / other, self.w / other, self.h / other)
        else:
            raise Exception("TypeError: only Vec4, (int, int, int, int), (float, float, float, float), [int, int, "
                            "int, int], [float, float, float, float], int or float can be divided with a Vec4")
        return result

    def __len__(self):
        return len(self.getPos())

    def __lt__(self, other) -> bool:
        result = None
        if Vec4.COMPARISON_TYPE == "LENGTH":
            result = self.length() < other.length()
        elif Vec4.COMPARISON_TYPE == "POS":
            result = self.x < other.x and self.y < other.y and self.w < other.w and self.h < other.h
        return result

    def __le__(self, other) -> bool:
        result = None
        if Vec4.COMPARISON_TYPE == "LENGTH":
            result = self.length() <= other.length()
        elif Vec4.COMPARISON_TYPE == "POS":
            result = self.x <= other.x and self.y <= other.y and self.w <= other.w and self.h <= other.h
        return result

    def __gt__(self, other) -> bool:
        result = None
        if Vec4.COMPARISON_TYPE == "LENGTH":
            result = self.length() > other.length()
        elif Vec4.COMPARISON_TYPE == "POS":
            result = self.x > other.x and self.y > other.y and self.w > other.w and self.h > other.h
        return result

    def __ge__(self, other) -> bool:
        result = None
        if Vec4.COMPARISON_TYPE == "LENGTH":
            result = self.length() >= other.length()
        elif Vec4.COMPARISON_TYPE == "POS":
            result = self.x >= other.x and self.y >= other.y and self.w >= other.w and self.h >= other.h
        return result

    def __eq__(self, other):
        result = None
        if Vec4.COMPARISON_TYPE == "LENGTH":
            result = self.length() == other.length()
        elif Vec4.COMPARISON_TYPE == "POS":
            result = self.x == other.x and self.y == other.y and self.w == other.w and self.h == other.h
        return result

    def __ne__(self, other) -> bool:
        result = None
        if Vec4.COMPARISON_TYPE == "LENGTH":
            result = self.length() != other.length()
        elif Vec4.COMPARISON_TYPE == "POS":
            result = self.x != other.x or self.y != other.y or self.w != other.w or self.h != other.h
        return result

    def __hash__(self) -> hash:
        return hash(self.getPos())

    def __str__(self):
        return f"x = {self.x}, y = {self.y}, w = {self.w}, h = {self.h}"

    def __repr__(self) -> str:
        return f"(x = {self.x}, y = {self.y}, w = {self.w}, h = {self.w})"

    def __format__(self, format_spec):
        pattern = "({:" + format_spec + "}, {:" + format_spec + "}, {:" + format_spec + "}, {:" + format_spec + "})"
        return pattern.format(self.x, self.y, self.w, self.h)
