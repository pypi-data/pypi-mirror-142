import math
import random


class Vec2:
    COMPARISON_TYPE = "POS"

    def __init__(self, x=0.0, y=0.0, pos=None):
        if pos is None:
            self.x = x
            self.y = y
        else:
            if type(pos) is Vec2:
                self.x = pos.x
                self.y = pos.y
            elif (type(pos) is list or type(pos) is tuple) and len(pos) == 2:
                self.x = pos[0]
                self.y = pos[1]
            else:
                raise Exception("TypeError: pos argument can only be Vec2, (int, int), (float, float), int or float")

    def getX(self):
        return self.x

    def setX(self, x):
        self.x = x

    def getY(self):
        return self.y

    def setY(self, y):
        self.y = y

    def getPos(self):
        return self.x, self.y

    def setPos(self, newPos):
        self.x = newPos.x
        self.y = newPos.y

    def add(self, x=0.0, y=0.0, glob=0.0, pos=None):
        if pos is None:
            self.x = self.x + x + glob
            self.y = self.y + y + glob
        else:
            if type(pos) == Vec2:
                self.x = self.x + pos.x
                self.y = self.y + pos.y
            elif (type(pos) == tuple or type(pos) == list) and len(pos) == 2:
                self.x = self.x + pos[0]
                self.y = self.y + pos[1]
            else:
                raise Exception("TypeError: only Vec2, (int, int), (float, float), int or float can be added to a Vec2")

    def sub(self, x=0.0, y=0.0, glob=0.0, pos=None):
        if pos is None:
            self.x = self.x - x - glob
            self.y = self.y - y - glob
        else:
            if type(pos) == Vec2:
                self.x = self.x - pos.x
                self.y = self.y - pos.y
            elif (type(pos) == tuple or type(pos) == list) and len(pos) == 2:
                self.x = self.x - pos[0]
                self.y = self.y - pos[1]
            else:
                raise Exception("TypeError: only Vec2, (int, int), (float, float), [int, int], [float, float], "
                                "int or float can be subtracted from a Vec2")

    def div(self, x=1.0, y=1.0, glob=1.0, pos=None):
        if pos is None:
            self.x = self.x / x / glob
            self.y = self.y / y / glob
        else:
            if type(pos) == Vec2:
                self.x = self.x / pos.x
                self.y = self.y / pos.y
            elif (type(pos) == tuple or type(pos) == list) and len(pos) == 2:
                self.x = self.x / pos[0]
                self.y = self.y / pos[1]
            else:
                raise Exception("TypeError: only Vec2, (int, int), (float, float), [int, int], [float, float], "
                                "int or float can be divided with a Vec2")

    def mult(self, x=1.0, y=1.0, glob=1.0, pos=None):
        if pos is None:
            self.x = self.x * x * glob
            self.y = self.y * y * glob
        else:
            if type(pos) == Vec2:
                self.x = self.x * pos.x
                self.y = self.y * pos.y
            elif (type(pos) == tuple or type(pos) == list) and len(pos) == 2:
                self.x = self.x * pos[0]
                self.y = self.y * pos[1]
            else:
                raise Exception("TypeError: only Vec2, (int, int), (float, float), [int, int], [float, float], "
                                "int or float can be multiplied with a Vec2")

    def inverse(self, inverseX, inverseY):
        if inverseX:
            self.x *= -1
        if inverseY:
            self.y *= -1

    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def normalize(self):
        self.div(glob=self.length())

    def normal(self):
        return self / self.length()

    def clone(self):
        return Vec2(self.x, self.y)

    @classmethod
    def randomIntVec(cls, minX=-50, maxX=50, minY=-50, maxY=50):
        x = random.randint(minX, maxX)
        y = random.randint(minY, maxY)
        return Vec2(x, y)

    @classmethod
    def randomVec(cls, minX=-50, maxX=50, minY=-50, maxY=50):
        x = random.randrange(minX, maxX)
        y = random.randrange(minY, maxY)
        return Vec2(x, y)

    @classmethod
    def dist(cls, vecA, vecB):
        return math.sqrt((vecA.x - vecB.x) ** 2 + (vecA.y - vecB.y) ** 2)

    @classmethod
    def degreesToVec2(cls, degrees):
        radians = degrees * (math.pi / 180)
        return Vec2(math.cos(radians), math.sin(radians))

    @classmethod
    def radiansToVec2(cls, radians):
        return Vec2(math.cos(radians), math.sin(radians))

    @classmethod
    def vec2ToRadians(cls, vector):
        return math.acos(vector.normal().x)

    @classmethod
    def vec2ToDegrees(cls, vector):
        return Vec2.vec2ToRadians(vector) / (math.pi / 180)

    @classmethod
    def lerp(cls, vecA, vecB, step):
        x = (1 - step) * vecA.x + step * vecB.x
        y = (1 - step) * vecA.y + step * vecB.y
        return Vec2(x, y)

    @classmethod
    def collinear(cls, vecA, vecB, vecC):
        vecAB = vecB - vecA
        vecAC = vecC - vecA
        coefX = vecAB.x / vecAC.x
        coefY = vecAB.y / vecAC.y
        return coefX == coefY

    @classmethod
    def between(cls, vecA, vecB, target):
        result = False
        if Vec2.collinear(vecA, vecB, target):
            if vecA.x <= target.x <= vecB.x and vecA.y <= target.y <= vecB.y:
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
            Vec2.COMPARISON_TYPE = newType

    def __add__(self, other):
        if type(other) == Vec2:
            result = Vec2(self.x + other.x, self.y + other.y)
        elif (type(other) == tuple or type(other) == list) and len(other) == 2:
            result = Vec2(self.x + other[0], self.y + other[1])
        elif type(other) == int or type(other) == float:
            result = Vec2(self.x + other, self.y + other)
        else:
            raise Exception("TypeError: only Vec2, (int, int), (float, float), int or float can be added to a Vec2")
        return result

    def __sub__(self, other):
        if type(other) == Vec2:
            result = Vec2(self.x - other.x, self.y - other.y)
        elif (type(other) == tuple or type(other) == list) and len(other) == 2:
            result = Vec2(self.x - other[0], self.y - other[1])
        elif type(other) == int or type(other) == float:
            result = Vec2(self.x - other, self.y - other)
        else:
            raise Exception("TypeError: only Vec2, (int, int), (float, float), [int, int], [float, float], "
                            "int or float can be subtracted from a Vec2")
        return result

    def __mul__(self, other):
        if type(other) == Vec2:
            result = Vec2(self.x * other.x, self.y * other.y)
        elif (type(other) == tuple or type(other) == list) and len(other) == 2:
            result = Vec2(self.x * other[0], self.y * other[1])
        elif type(other) == int or type(other) == float:
            result = Vec2(self.x * other, self.y * other)
        else:
            raise Exception("TypeError: only Vec2, (int, int), (float, float), [int, int], [float, float], "
                            "int or float can be multiplied with a Vec2")
        return result

    def __truediv__(self, other):
        if type(other) == Vec2:
            result = Vec2(self.x / other.x, self.y / other.y)
        elif (type(other) == tuple or type(other) == list) and len(other) == 2:
            result = Vec2(self.x / other[0], self.y / other[1])
        elif type(other) == int or type(other) == float:
            result = Vec2(self.x / other, self.y / other)
        else:
            raise Exception(
                "TypeError: only Vec2, (int, int), (float, float), [int, int], [float, float], int or float can be "
                "divided with a Vec2")
        return result

    def __len__(self):
        return len(self.getPos())

    def __lt__(self, other) -> bool:
        result = None
        if Vec2.COMPARISON_TYPE == "LENGTH":
            result = self.length() < other.length()
        elif Vec2.COMPARISON_TYPE == "POS":
            result = self.x < other.x and self.y < other.y
        return result

    def __le__(self, other) -> bool:
        result = None
        if Vec2.COMPARISON_TYPE == "LENGTH":
            result = self.length() <= other.length()
        elif Vec2.COMPARISON_TYPE == "POS":
            result = self.x <= other.x and self.y <= other.y
        return result

    def __gt__(self, other) -> bool:
        result = None
        if Vec2.COMPARISON_TYPE == "LENGTH":
            result = self.length() > other.length()
        elif Vec2.COMPARISON_TYPE == "POS":
            result = self.x > other.x and self.y > other.y
        return result

    def __ge__(self, other) -> bool:
        result = None
        if Vec2.COMPARISON_TYPE == "LENGTH":
            result = self.length() > other.length()
        elif Vec2.COMPARISON_TYPE == "POS":
            result = self.x > other.x and self.y > other.y
        return result

    def __eq__(self, other) -> bool:
        result = None
        if Vec2.COMPARISON_TYPE == "LENGTH":
            result = self.length() == other.length()
        elif Vec2.COMPARISON_TYPE == "POS":
            result = self.x == other.x and self.y == other.y
        return result

    def __ne__(self, other) -> bool:
        result = None
        if Vec2.COMPARISON_TYPE == "LENGTH":
            result = self.length() != other.length()
        elif Vec2.COMPARISON_TYPE == "POS":
            result = self.x != other.x or self.y != other.y
        return result

    def __hash__(self) -> hash:
        return hash(self.getPos())

    def __str__(self) -> str:
        return f"x = {self.x}, y = {self.y}"

    def __repr__(self) -> str:
        return f"(x = {self.x}, y = {self.y})"

    def __format__(self, format_spec):
        pattern = "({:" + format_spec + "}, {:" + format_spec + "})"
        return pattern.format(self.x, self.y)
