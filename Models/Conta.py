class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print(f"Construindo o objeto {self}")
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

    def saca(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor

    def transfere(self, valor, origem, destino):
        origem.saca(valor)
        destino.deposita(valor)
