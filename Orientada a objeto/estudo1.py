import random as rd
from os import system as sys

class player:
    
    def __init__(self, nome,vida = 10):
        self.nome = nome
        self.vida = vida
        
    def ataque(self):
        dano = rd.randrange(0,10)        
        return dano
    
    def dano(self, dano):
        vida =- dano
        return vida
    
sys("cls")

print(f''' 
      
    ========================
        Teste de player
    ========================
      
      ''')
        
player1 = player(nome=input("\tDigite seu nome: "))

sys("cls")

print(f'''
    =====================================
        Nome do jogador: {player1.nome}
        Vida inicial: {player1.vida}
    =====================================
      ''')

sys("cls")

