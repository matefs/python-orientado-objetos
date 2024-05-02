
class Cliente:

    def __init__(self,nome):
        self.__nome = nome

    @property
    def nome(self):
        print("chamando o @property nome()")
        return self.__nome

    @nome.setter
    def nome(self,nome):
        print('chamando setter nome () ')
        self.__nome = nome

cliente = Cliente('Mateus')
print(cliente.nome)
#cliente.nome


