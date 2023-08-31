class Bicicleta:    
    def _init_(self, cor, modelo, ano,valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano 
        self.valor = valor 
        
    def buzinar(self):
        print("Plim, plim ......")
        
    def parar(self):
        print("Parando...")
        print("Parada")
        
    def correr(self):
        print("Vush")
        
        
b1 = Bicicleta()
b1.cor = "verde"
b1.buzinar()
b1.correr()
b1.parar()
print(b1.cor)