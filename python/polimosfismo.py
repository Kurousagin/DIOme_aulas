
# class Passaro: 
#     def voar(self): 
#         print("Voando ....")
    
# class Pardal(Passaro):
#     def voar(self):
#         super().voar()

# class Avestruz(Passaro):
#     def voar(self):
#         print("Avestruz não voa!")

# def plano_de_voo(obj):
#     obj.voar()

# plano_de_voo(Pardal())
# plano_de_voo(Avestruz())        



############################################################################################################

class Aeronaves:
    def voar(self):
        print("Decolando....")

class Aviao(Aeronaves):
    def voar(self):
        super().voar()

class hidroaviao(Aeronaves):
    def planar(self):
        print("Planando sobre as águas")
    
    def voar(self):
         super().voar()
    
    

    

naves = Aeronaves()
naves.voar()
hridronave = hidroaviao()
hridronave.planar()
hridronave.voar()

