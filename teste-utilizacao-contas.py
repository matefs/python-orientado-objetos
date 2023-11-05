from Models.Conta import Conta

conta = Conta(123, "Mateus", 100, 1000000)


conta.deposita(10)
conta.deposita(-10)
conta.extrato()

conta.saca(10000000)
conta.extrato()

