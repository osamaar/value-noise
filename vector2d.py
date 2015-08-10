from math import sqrt

class Vect2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '(%.2f, %.2f)' %(self.x, self.y)

    def __len__(self):
        return 2

    def __nonzero__(self):
        if (self.x or self.y):
            return True
        return False
        
    def __iter__(self):
        yield self.x
        yield self.y
    
    def __mul__(self, t):
        return Vect2d(self.x*t, self.y*t)

    def __rmul__(self, t):
        return self * t
    
    def __add__(self, t):
        #print self, t
        return Vect2d(self.x+t[0], self.y+t[1])

    def __sub__(self, t):
        return self + (t[0]*-1, t[1]*-1)

    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError('index should be 0 for x or 1 for y')

    def dot(self, other):
        return self.x*other.x + self.y*other.y

    def mag(self):
        return float(sqrt(self.x**2 + self.y**2))

    def unit(self):
        if not self.mag(): return Vect2d(0, 0)
        return Vect2d(self.x/self.mag(), self.y/self.mag())
