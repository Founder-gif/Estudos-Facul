#-----------------------------------------------#
#                                               #
#       Autor: JPAP                             #
#       data: 10/08/23                          #
#       assunto: classes e funções              #
#                                               #
#-----------------------------------------------#

#DEFINIÇÕES----------------------------------------

class Bola:#---------------------------------------
    def __init__(self,cincunferencia,material,cor):
        self.circunferencia = cincunferencia
        self.material       = material
        self.cor            = cor
        
    def trocar_cor(self,cor):
        self.cor            = cor
    
    def mostrar_cor(self):
        return self.cor
    
class quadrado:#-----------------------------------
    def __init__(self,lado):  
        self.lado           = lado
        
    def mudar_lado(self,lado):
        self.lado           = lado
        
    def valor_lado(self):    
        return self.lado
    
    def area_quadrado(self):
        return self.lado * 2
    
class retangulo:#----------------------------------
    def __init__(self,ladoA,ladoB):
        self.ladoA          = ladoA
        self.ladoB          = ladoB
        
    def mudar_lados(self,ladoA,ladoB):
        self.ladoA          = ladoA
        self.ladoB          = ladoB
        
    def valor_lados(self):
        return self.ladoA and self.ladoB
    
    def area_retangulo(self):
        return self.ladoA * self.ladoB
    
    def perimetro_retangulo(self):
        return (self.ladoA * 2) * (self.ladoB * 2)
    
#Testes de Classes --------------------------------

ret1 = retangulo(1,2)

ret1.mudar_lados(5,10)

print(f'''O valor dos lados são: {ret1.valor_lados()}''')s

