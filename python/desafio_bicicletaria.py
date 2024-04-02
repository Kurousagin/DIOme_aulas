class Bicicleta:    
    def __init__(self, cor, modelo, ano,valor) -> None:
        self.cor = cor
        self.modelo = modelo
        self.ano = ano 
        self.valor = valor 
        # self.marcha = 1
        
    def buzinar(self):
        print("Plim, plim ......")
        
    def parar(self):
        print("Parando...")
        print("Parada")
        
    def correr(self):
        print("Vush")

    # def trocar_marcha(self, nro_marcha):
    #     print("Trocando Marcha!")

    #     def _trocar_marcha():
    #         if nro_marcha > self.marcha:
    #             print("Marcha Trocada ....!")
    #         else:
    #             print("não foi possivel trocar a marcha")
        
    # def __str__(self) -> str:
    #     return f"Bicicleta: {self.cor}, {self.modelo}, {self.ano}, {self.valor}"
        
    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
        
b1 = Bicicleta("Amarelo","caloi",2022,6000)
print(b1)
b1.buzinar()
# b1.trocar_marcha()
b1.correr()
b1.parar()

