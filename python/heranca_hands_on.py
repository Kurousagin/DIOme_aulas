# #Herança Simples #########################################################################################################
# # class veiculo:
# #     def __init__(self, cor, placa, numero_rodas):
# #         self.cor = cor
# #         self.placa = placa 
# #         self.numero_rodas = numero_rodas 
       

# #     def ligar_motor(self):
# #         print("Ligando o motor ....")

# # class Motocicleta(veiculo):
# #     pass

# # class Carro(veiculo):
# #     pass

# # class Caminhao(veiculo):
# #     def __init__(self,cor, placa, numero_rodas,carregado):
# #         self.carregado = carregado

# #     def esta_carregado(self):
# #         print(f"{'Sim' if self.carregado else 'Não'} estou carregado")



# # # moto = Motocicleta("preta", "abc-123", 2, "Volkswagen")
# # # moto.ligar_motor()

# # # carro = Carro("Preto", "cuf0f0", 4 , "nissan")
# # # carro.ligar_motor()


# # caminhao = Caminhao("Azul", "ABC-125", 8, False)
# # caminhao.ligar_motor()
# # caminhao.esta_carregado()



# #Herança Multipla #####################################################################################

# class Animal:
#     def __init__(self, nro_patas) :
#         self.nro_patas = nro_patas

#     def __str__(self):
#         return f"{self.__class__.__name__}:{', '.join([f'{chave}={valor}'for chave, valor in self.__dict__.items()])}"

# class Mamifero(Animal):
#     def __init__(self, cor_pelo,**kw) :
#         self.cor_pelo = cor_pelo
#         super().__init__(**kw)

# class Ave(Animal):
#     def __init__(self, cor_bico,**kw) :
#         self.cor_bico = cor_bico
#         super().__init__(**kw)


# class Gato(Mamifero):
#     pass

# class FalarMixin:
#     pass



# class Ornitorrinco(Mamifero, Ave):
#    def __init__(self, cor_bico,cor_pelo, nro_patas) :
#         print(Ornitorrinco.__mro__)

#         self.cor_bico = cor_bico
#         super().__init__(cor_bico = cor_bico, cor_pelo=cor_pelo, nro_patas=nro_patas)



# # gato = Gato(nro_patas= 4, cor_pelo=" Laranja")
# # print(gato)



# ornitorrinco = Ornitorrinco(nro_patas = 2, cor_pelo = " cinza", cor_bico = " Laranja")
# print(ornitorrinco)
class Foo:
    def hello(self):
        print(self.__class__.__name__.lower())


class Bar(Foo):
    def hello(self):
        return super().hello()


bar = Bar()
bar.hello()