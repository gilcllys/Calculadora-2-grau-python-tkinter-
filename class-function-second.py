
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

funcao = second_function(1,-6,8)
delta = funcao.delta()
raiz1 = funcao.raiz1()
raiz2 = funcao.raiz2()

print(f"delta ={delta}")
print(f"raiz1 ={raiz1}")
print(f"raiz2 ={raiz2}")