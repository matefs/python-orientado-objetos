'''
Source: https://www.youtube.com/watch?v=PDqy1HoA3QM&ab_channel=NeuralNine
'''
from typing import Union 

def some_calculation_integer(x: int , y: int ) -> int:
    return (x+y)**2

def some_calculation(x: Union[int,float] , y: Union[int,float] ) -> Union[int,float]:
    return ( x + y) **2 

print(some_calculation_integer(4,5))
print(some_calculation(4.1,5))

# Tipando Retorno de função como tipo none 
def exemplo() -> None:
    variavel: int = 10

print(exemplo());

def exemplo2() -> None:
    variavel: int = 10
    return variavel

print(exemplo2());


