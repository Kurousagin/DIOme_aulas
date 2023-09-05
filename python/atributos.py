# class Estudante:
#     escola = "DIO"
#     def __init__( self, nome, matricula):
#         self.nome = nome
#         self.matricula = matricula

#     def __str__(self):
#         return f"{self.nome} - {self.matricula} - {self.escola} "
    
# def mostrar_valores(*objs):
#     for obj in objs:
#         print(obj)
    

# aluno1 = Estudante("Guilherme", 1)
# aluno2 = Estudante("Ana Julia", 2)

# mostrar_valores(aluno1, aluno2)

# Estudante.escola = "DevMedia"
# aluno3 = Estudante("Darfran", 3)

# mostrar_valores(aluno1, aluno2, aluno3)




###### Metodos de classe #######

# class Pessoa:
#     def __init__(self, nome=None , idade=None):
#         self.nome = nome
#         self.idade= idade


#     @classmethod
#     def criar_data_nascimento(cls, ano, mes , dia, nome):
        
#         idade = 2022 - ano
#         return Pessoa(nome, idade)


# p2 = Pessoa.criar_data_nascimento(2003,8,27,"Pedro")
# print(p2.nome, p2.idade)



###### Metodos estáticos #######


# class Pessoa:
#     def __init__(self, nome=None , idade=None):
#         self.nome = nome
#         self.idade= idade

#     @staticmethod
#     def e_maior_idade(idade):
#         return idade >= 18


# print(Pessoa.e_maior_idade(8))
# print(Pessoa.e_maior_idade(19))


################# Classes Abstratas ###################

from abc import ABC, abstractmethod

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando a tv...")
        print("Ligada")

    def desligar(self):
        print("Desligando a tv....")
        print("Desligada")

class CoontroleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando ar...")
        print("Ligado")

    def desligar(self):
        print("Desligando ar....")
        print("Desligado")


controle = ControleTV()
controle.ligar()
controle.desligar()
controlear = CoontroleArCondicionado()
controlear.ligar()
controlear.desligar()












