class Rectangle:
    def __init__(self, a_side, b_side):
        if isinstance(a_side, (int, float)) == False:
            a_side = 1
            print("Input format the first side is wrong. Changed to 1")
        if isinstance(b_side, (int, float)) == False:
            b_side = 1
            print("Input format the second side is wrong. Changed to 1")
        self.a_side = a_side
        self.b_side = b_side

    def __str__(self):
        return f'({self.a_side}, {self.b_side})'

    def get_space(self):
        return self.a_side * self.b_side

    def get_perimeter(self):
        return 2 * (self.a_side + self.b_side)

obi = Rectangle(10,50)

print(obi)
print(obi.get_perimeter())
print(obi.get_space())