from main import cliente 
from random import randint, uniform

tol=0.1

for i in range (1,10):
    n=randint(500000,30000000)
    cliente1=cliente(n)
    if uniform(0,1) < tol:
        cliente1.modificarcategoria('Preferencial')
    else: 
        cliente1.modificarcategoria('General')
    cliente1.testcliente(n)
