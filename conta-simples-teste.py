# Exemplo procedural 
def cria_conta(numero, titular, saldo ,limite ):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta

def depositar(conta,valor):
    conta["saldo"] += valor

def sacar(conta,valor):
    conta["saldo"] -= valor

def extrato(conta):
    print(f'A conta possui um saldo de {conta["saldo"]}')


MinhaContaPessoal = cria_conta(123,"mateus", 50, 1000)

extrato(MinhaContaPessoal)


