
class Conta: 
    def __init__(self, numero, titular, saldo, limite):
        print(f"Construindo o objeto {self}")
        self.numero = numero
        self.titular = titular
        self.saldo = saldo 
        self.limit = limite
    def extrato(self):
        print(f'Saldo {self.saldo} do titular {self.titular}')

conta = Conta(123,"Mateus",100,1000000);
print(conta)
print(conta.numero)
conta.extrato()