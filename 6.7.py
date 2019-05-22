class circle(object):
    def __init__(self,r):
        self.radius = r
    def dientich (self):
        return self.radius**2*3.14
    def chuvi(self):
        return self.radius*2*3.14
acircle = circle(4)
print( acircle.dientich())
print( acircle.chuvi())



