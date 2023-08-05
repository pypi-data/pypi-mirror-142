import math
import random


class Vec3:
    COMPARISON_TYPE = "POS"

    def __init__(self, x=0.0, y=0.0, z=0.0, pos=None):
        if pos is None:
            self.x = x
            self.y = y
            self.z = z
        else:
            if type(pos) is Vec3:
                self.x = pos.x
                self.y = pos.y
                self.z = pos.z
            elif (type(pos) is list or type(pos) is tuple) and len(pos) == 3:
                self.x = pos[0]
                self.y = pos[1]
                self.z = pos[2]
            else:
                raise Exception("TypeError: pos argument can only be Vec3, (int, int, int), (float, float, float), "
                                "[int, int, int], [float, float, float], int or float")

    def getX(self):
        return self.x

    def setX(self, x):
        self.x = x

    def getY(self):
        return self.y

    def setY(self, y):
        self.y = y

    def getZ(self):
        return self.z

    def setZ(self, z):
        self.z = z

    def getPos(self):
        return self.x, self.y, self.z

    def setPos(self, newPos):
        self.x = newPos.x
        self.y = newPos.y
        self.z = newPos.z

    def add(self, x=0.0, y=0.0, z=0.0, glob=0.0, pos=None):
        if pos is None:
            self.x = self.x + x + glob
            self.y = self.y + y + glob
            self.z = self.z + z + glob
        else:
            if type(pos) == Vec3:
                self.x = self.x + pos.x
                self.y = self.y + pos.y
                self.z = self.z + pos.z
            elif (type(pos) == tuple or type(pos) == list) and len(pos) == 3:
                self.x = self.x + pos[0]
                self.y = self.y + pos[1]
                self.z = self.z + pos[2]
            else:
                raise Exception("TypeError: only Vec3, (int, int, int), (float, float, float), [int, int, int], "
                                "[float, float, float], int or float can be added to a Vec3")

    def sub(self, x=0.0, y=0.0, z=0.0, glob=0.0, pos=None):
        if pos is None:
            self.x = self.x - x - glob
            self.y = self.y - y - glob
            self.z = self.z - z - glob
        else:
            if type(pos) == Vec3:
                self.x = self.x - pos.x
                self.y = self.y - pos.y
                self.z = self.z - pos.z
            elif (type(pos) == tuple or type(pos) == list) and len(pos) == 3:
                self.x = self.x - pos[0]
                self.y = self.y - pos[1]
                self.z = self.z - pos[2]
            else:
                raise Exception("TypeError: only Vec3, (int, int, int), (float, float, float), [int, int, int], "
                                "[float, float, float], int or float can be subtracted from a Vec3")

    def div(self, x=1.0, y=1.0, z=1.0, glob=1.0, pos=None):
        if pos is None:
            self.x = self.x / x / glob
            self.y = self.y / y / glob
            self.z = self.z / z / glob
        else:
            if type(pos) == Vec3:
                self.x = self.x / pos.x
                self.y = self.y / pos.y
                self.z = self.z / pos.z
            elif (type(pos) == tuple or type(pos) == list) and len(pos) == 3:
                self.x = self.x / pos[0]
                self.y = self.y / pos[1]
                self.z = self.z / pos[2]
            else:
                raise Exception("TypeError: only Vec3, (int, int, int), (float, float, float), [int, int, int], "
                                "[float, float, float], int or float can be divided with a Vec3")

    def mult(self, x=1.0, y=1.0, z=1.0, glob=1.0, pos=None):
        if pos is None:
            self.x = self.x * x * glob
            self.y = self.y * y * glob
            self.z = self.z * z * glob
        else:
            if type(pos) == Vec3:
                self.x = self.x * pos.x
                self.y = self.y * pos.y
                self.z = self.z * pos.z
            elif (type(pos) == tuple or type(pos) == list) and len(pos) == 3:
                self.x = self.x * pos[0]
                self.y = self.y * pos[1]
                self.z = self.z * pos[2]
            else:
                raise Exception("TypeError: only Vec3, (int, int, int), (float, float, float), [int, int, int], "
                                "[float, float, float], int or float can be multiplied with a Vec3")

    def inverse(self, inverseX, inverseY, inverseZ):
        if inverseX:
            self.x *= -1
        if inverseY:
            self.y *= -1
        if inverseZ:
            self.z *= -1

    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def normalize(self):
        self.div(glob=self.length())

    def normal(self):
        return self / self.length()

    def clone(self):
        return Vec3(self.x, self.y, self.z)

    @classmethod
    def randomIntVec(cls, minX=-50, maxX=50, minY=-50, maxY=50, minZ=-50, maxZ=50):
        x = random.randint(minX, maxX)
        y = random.randint(minY, maxY)
        z = random.randint(minZ, maxZ)
        return Vec3(x, y, z)

    @classmethod
    def randomVec(cls, minX=-50, maxX=50, minY=-50, maxY=50, minZ=-50, maxZ=50):
        x = random.randrange(minX, maxX)
        y = random.randrange(minY, maxY)
        z = random.randint(minZ, maxZ)
        return Vec3(x, y, z)

    @classmethod
    def dist(cls, vectorA, vectorB):
        return math.sqrt((vectorA.x - vectorB.x) ** 2 + (vectorA.y - vectorB.y) ** 2 + (vectorA.z - vectorB.z) ** 2)

    @classmethod
    def lerp(cls, vecA, vecB, step):
        x = (1 - step) * vecA.x + step * vecB.x
        y = (1 - step) * vecA.y + step * vecB.y
        z = (1 - step) * vecA.z + step * vecB.z
        return Vec3(x, y, z)

    @classmethod
    def collinear(cls, vecA, vecB, vecC):
        vecAB = vecB - vecA
        vecAC = vecC - vecA
        coefX = vecAB.x / vecAC.x
        coefY = vecAB.y / vecAC.y
        coefZ = vecAB.z / vecAC.z
        return coefX == coefY and coefY == coefZ

    @classmethod
    def between(cls, vecA, vecB, target):
        result = False
        if Vec3.collinear(vecA, vecB, target):
            if vecA.x <= target.x <= vecB.x and vecA.y <= target.y <= vecB.y and vecA.z <= target.z <= vecB.z:
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
            Vec3.COMPARISON_TYPE = newType

    def __add__(self, other):
        if type(other) == Vec3:
            result = Vec3(self.x + other.x, self.y + other.y, self.z + other.z)
        elif (type(other) == tuple or type(other) == list) and len(other) == 3:
            result = Vec3(self.x + other[0], self.y + other[1], self.z + other[2])
        elif type(other) == int or type(other) == float:
            result = Vec3(self.x + other, self.y + other, self.z + other)
        else:
            raise Exception("TypeError: only Vec3, (int, int, int), (float, float, float), [int, int, int], [float, "
                            "float, float], int or float can be added to a Vec3")
        return result

    def __sub__(self, other):
        if type(other) == Vec3:
            result = Vec3(self.x - other.x, self.y - other.y, self.z - other.z)
        elif (type(other) == tuple or type(other) == list) and len(other) == 3:
            result = Vec3(self.x - other[0], self.y - other[1], self.z - other[2])
        elif type(other) == int or type(other) == float:
            result = Vec3(self.x - other, self.y - other, self.z - other)
        else:
            raise Exception("TypeError: only Vec3, (int, int, int), (float, float, float), [int, int, int], [float, "
                            "float, float], int or float can be subtracted from a Vec3")
        return result

    def __mul__(self, other):
        if type(other) == Vec3:
            result = Vec3(self.x * other.x, self.y * other.y, self.z * other.z)
        elif (type(other) == tuple or type(other) == list) and len(other) == 3:
            result = Vec3(self.x * other[0], self.y * other[1], self.z * other[2])
        elif type(other) == int or type(other) == float:
            result = Vec3(self.x * other, self.y * other, self.z * other)
        else:
            raise Exception("TypeError: only Vec3, (int, int, int), (float, float, float), [int, int, int], [float, "
                            "float, float], int or float can be multiplied with a Vec3")
        return result

    def __truediv__(self, other):
        if type(other) == Vec3:
            result = Vec3(self.x / other.x, self.y / other.y, self.z / other.z)
        elif (type(other) == tuple or type(other) == list) and len(other) == 3:
            result = Vec3(self.x / other[0], self.y / other[1], self.z / other[2])
        elif type(other) == int or type(other) == float:
            result = Vec3(self.x / other, self.y / other, self.z / other)
        else:
            raise Exception("TypeError: only Vec3, (int, int, int), (float, float, float), [int, int, int], [float, "
                            "float, float], int or float can be divided with a Vec3")
        return result

    def __len__(self):
        return len(self.getPos())

    def __lt__(self, other) -> bool:
        result = None
        if Vec3.COMPARISON_TYPE == "LENGTH":
            result = self.length() < other.length()
        elif Vec3.COMPARISON_TYPE == "POS":
            result = self.x < other.x and self.y < other.y and self.z < other.z
        return result

    def __le__(self, other) -> bool:
        result = None
        if Vec3.COMPARISON_TYPE == "LENGTH":
            result = self.length() <= other.length()
        elif Vec3.COMPARISON_TYPE == "POS":
            result = self.x <= other.x and self.y <= other.y and self.z <= other.z
        return result

    def __gt__(self, other) -> bool:
        result = None
        if Vec3.COMPARISON_TYPE == "LENGTH":
            result = self.length() > other.length()
        elif Vec3.COMPARISON_TYPE == "POS":
            result = self.x > other.x and self.y > other.y and self.z > other.z
        return result

    def __ge__(self, other) -> bool:
        result = None
        if Vec3.COMPARISON_TYPE == "LENGTH":
            result = self.length() >= other.length()
        elif Vec3.COMPARISON_TYPE == "POS":
            result = self.x >= other.x and self.y >= other.y and self.z >= other.z
        return result

    def __eq__(self, other):
        result = None
        if Vec3.COMPARISON_TYPE == "LENGTH":
            result = self.length() == other.length()
        elif Vec3.COMPARISON_TYPE == "POS":
            result = self.x == other.x and self.y == other.y and self.z == other.z
        return result

    def __ne__(self, other) -> bool:
        result = None
        if Vec3.COMPARISON_TYPE == "LENGTH":
            result = self.length() != other.length()
        elif Vec3.COMPARISON_TYPE == "POS":
            result = self.x != other.x or self.y != other.y or self.z != other.z
        return result

    def __hash__(self) -> hash:
        return hash(self.getPos())

    def __str__(self) -> str:
        return f"x = {self.x}, y = {self.y}, z = {self.z}"

    def __repr__(self) -> str:
        return f"(x = {self.x}, y = {self.y}, z = {self.z})"

    def __format__(self, format_spec):
        pattern = "({:" + format_spec + "}, {:" + format_spec + "}, {:" + format_spec + "})"
        return pattern.format(self.x, self.y, self.z)
