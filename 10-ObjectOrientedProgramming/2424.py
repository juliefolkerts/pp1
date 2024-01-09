class C():
    def __init__(self,points):
        self.points = points

    def m(self,n):
        self.n = n
        count = 0
        for point in self.points:
            if point[0] > 0 and point[1] > 0:
                count += 1
            else:
                count = count
        if count >= n:
            result = True
        else:
            result = False
        return result
    

a = C([[2,3],[1,8],[-6,4],[3,-7]])
print(a.m(2))
print(a.m(3))