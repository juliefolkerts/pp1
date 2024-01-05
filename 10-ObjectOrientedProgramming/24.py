class C():
    def __init__(self,coords):
        self.coords = coords
    
    def m(self,n):
        self.n = n
        count = 0
        for x in self.coords:
            if x[0] > 0 and x[1] > 0:
                count += 1
            else:
                count = count
        if count >= n:
            result = True
        else:
            result = False
        return result
    
cor = C([[2,3],[1,8],[-6,4],[3,-7]])
print(cor.m(3))
