
class Conta: 
    def __init__(self, numero, titular, saldo, limite):
        print(f"Construindo o objeto {self}")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo 
        self.__limit = limite
  
    def extrato(self):
        print(f'Saldo {self.__saldo} do titular {self.__titular}')
   
    def deposita(self,valor):
        self.__valor += valor

    def saca(self,valor):
        self.__valor -= valor
    
conta = Conta(123,"Mateus",100,1000000);
print(conta)
conta.extrato()