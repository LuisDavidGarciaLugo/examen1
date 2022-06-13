from math import sqrt

#El simbolo "-" reemplaza a "&" para la representacion de la operacion de valor absoluto
class cuaternion(object):

    def __init__(self, a,b,c,d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __repr__(self):
        return "{} + {}i + {}j + {}k".format(self.a,self.b,self.c,self.d)

    def __str__(self):
        return "{} + {}i + {}j + {}k".format(self.a,self.b,self.c,self.d)

    def __add__(self, x):
        typeName = type(x).__name__
        if typeName == 'int' :  return cuaternion(self.a+x,self.b,self.c,self.d)
        elif typeName == 'cuaternion' : return cuaternion(self.a+x.a,self.b+x.b,self.c+x.c,self.d+x.d)
        else: raise TypeError("unsupported operand type(s) for +: 'cuaternion' and '" + typeName + "'")
        
    def __mul__(self, x):
        typeName = type(x).__name__
        if typeName == 'int': return cuaternion(self.a*x,self.b,self.c,self.d)
        elif typeName == 'cuaternion' : return cuaternion(
            self.a*x.a - self.b*x.b - self.c*x.c - self.d*self.d,
            self.a*x.b + self.b*x.a + self.c*x.d - self.d*self.c,
            self.a*x.c - self.b*x.d + self.c*x.a + self.d*self.b,
            self.a*x.d + self.b*x.c - self.c*x.b + self.d*self.a
        )
        else: raise TypeError("unsupported operand type(s) for +: 'cuaternion' and '" + typeName + "'")

    def __invert__(self):
        return cuaternion(self.a,-self.b,-self.c,-self.d)

    def __neg__(self):
        return sqrt(self.a**2 + self.b**2 + self.c**2 + self.d**2)