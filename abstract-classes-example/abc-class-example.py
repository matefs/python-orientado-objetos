from abc import ABC, abstractmethod

class ClasseAbstrata(ABC):
    @abstractmethod
    def metodo_abstrato(self, argumento):
        pass

class ClasseConcreta(ClasseAbstrata):
    def metodo_abstrato(self, argumento):
        return argumento

# Exemplo de uso
instancia_concreta = ClasseConcreta()
print(instancia_concreta.metodo_abstrato("Exemplo"))
