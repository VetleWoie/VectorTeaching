import code

class Vector():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return "Vector: [{0},{1}]".format(self.x,self.y)
    
    def __str__(self):
        return "Vector: [{0},{1}]".format(self.x,self.y)
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, other):
        return self.x*other.x + self.y+other.x


if __name__ == "__main__":
    x = Vector(2,3)
    y = Vector(3,2)
    code.interact(local=locals())