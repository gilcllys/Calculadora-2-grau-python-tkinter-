class second_function:
    def __init__(self,A,B,C):
        self.a = float(A)
        self.b = float(B)
        self.c = float(C)

    def delta(self):
        Delta = (self.b)**2 - 4*(self.a*self.c)
        return Delta
    
    def raiz1(self):
        raiz1 = (-self.b - second_function.delta(self)**(1/2))/(2*self.a)
        return raiz1

    def raiz2(self):
        raiz2 = (-self.b + second_function.delta(self)**(1/2))/(2*self.a)
        return raiz2