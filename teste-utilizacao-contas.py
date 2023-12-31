from Models.Conta import Conta

conta = Conta(123, "Mateus", 100, 1000000)

# O python permite acessar metodos que seriam privados através do _NomeObjeto__AtributoPrivado
print(f'Acessando metodos privados | saldo:{conta._Conta__saldo}')

conta.deposita(10)
conta.deposita(-10)
conta.extrato()

conta.saca(10000000)
conta.extrato()

conta2 = Conta(321, "João", 10, 1000000)

print(f'Transferindo dinheiro da conta para conta2')
conta.transfere(10,conta2)
conta.extrato()

conta.limite = 10000 # acessando setter do limite da conta 
print(f'acessando limite da conta {conta.limite}')# acessando limite pelo metodo getter




conta.saca(100000000000000000) # Valor passando do limite 
conta.extrato()  
print(f'O codigo do banco da conta é {conta.codigo_banco()} ')
print(f'Codigo de todos os bancos {conta.codigo_de_todos_bancos()}')

