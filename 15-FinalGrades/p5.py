class C():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def m1(self):
        if self.x > 0:
            if self.y > 0:
                result = 1
            else:
                result = 4
        if self.x < 0:
            if self.y < 0:
                result = 3
            else:
                result = 2
        if self.x == 0 or self.y == 0:
            result = 0
        return result
    def m2(self,a,b):
        self.a = a
        self.b = b
        answer = False
        if self.a > 0:
            if self.b > 0:
                result2 = 1
            else:
                result2 = 4
        if self.a < 0:
            if self.b < 0:
                result2 = 3
            else:
                result2 = 2
        if self.a == 0 or self.b == 0:
            result2 = 0
        if self.m1() == result2:
            answer = True
        return answer
    def m3(self,a,b):
        self.a = a
        self.b = b
        a= False
        x_distance = abs(self.x-self.a)
        y_distance = abs(self.y-self.b)
        distance = (x_distance**2+y_distance**2)**0.5
        if distance > 5:
            a = True
        return a


if __name__ == '__main__':
    p= C(2,3)
    print(p.m1())
    print(p.m2(-3,1))
    print(p.m3(4,7))
    p1 = C(0,5)
    print(p1.m1())
    print(p1.m2(-7,0))