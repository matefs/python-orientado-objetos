class Conta:
    def __init__(self, numero, titular, saldo, limite):
        # print(f"Construindo o objeto {self}")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo 
        self.__limite = limite
  
    def extrato(self):
        print(f'Saldo {self.__saldo} do titular {self.__titular}')
   
    def deposita(self, valor):
        if valor>=1:
            self.__saldo += valor
        else:
            return "Valor inválido"

    def __pode_sacar(self,valor_a_sacar):
        valor_disponivel_a_sacar = (self.__saldo + self.__limite)
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print(f'O valor {valor } passou do limite')

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    def get_saldo(self):
        return self.saldo

    def get_titular(self):
        return self.__titular

    @property 
    def limite(self):
        return self.__limite 
    
    @limite.setter
    def limite(self,limite):
        self.__limite = limite
    

    