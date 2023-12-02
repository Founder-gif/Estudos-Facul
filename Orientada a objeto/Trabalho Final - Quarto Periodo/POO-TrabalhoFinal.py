
    # Autor: João Paulo de Almeida Pereira 
    # data: 28/11/023
    # assunto: Trabalho final de POO 4º periodo
    
# -------------- imports ------------- #   
from organizador import *
from datetime import date

# -------------- Declarações --------- #

class Jogador:
    def __init__(self, nome, posicao, data_nascimento, nacionalidade, altura, peso):
        self.nome = nome
        self.posicao = posicao
        self.data_nascimento = data_nascimento
        self.nacionalidade = nacionalidade
        self.altura = altura
        self.peso = peso
    
    def imprimir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Posição: {self.posicao}")
        print(f"Data de nascimento: {self.data_nascimento}")
        print(f"Nacionalidade: {self.nacionalidade}")
        print(f"Altura: {self.altura}")
        print(f"Peso: {self.peso}\n")
    
    def calcular_idade(self):
        hoje = date.today()
        data_nascimento = self.data_nascimento.split("/")
        idade = hoje.year - int(data_nascimento[2]) - ((hoje.month, hoje.day) < (int(data_nascimento[1]), int(data_nascimento[0])))
        return idade
    
    def tempo_para_aposentar(self):
        if self.posicao == "defesa":
            tempo = 40 - self.calcular_idade()
        elif self.posicao == "meio-campo":
            tempo = 38 - self.calcular_idade()
        elif self.posicao == "ataque":
            tempo = 35 - self.calcular_idade()
        else:
            tempo = None
        if tempo > 0:
            return f"Faltam {tempo} anos para o jogador se aposentar."
        elif tempo == 0:
            return "O jogador está no último ano de sua carreira."
        else:
            return "O jogador já se aposentou."

def criar_jogador():
    cls()
    cabeçalho('Aposentadoria de Jogador')
    nome = input('\n  Digite o nome do jogador: ')
    cls()
    cabeçalho('Aposentadoria de Jogador')
    lista('Defesa,Meio-Campo,Ataque')
    posicao = input("Escreva a posição do jogador(ex. Defesa):\n ")
    posicao = posicao.lower()
    cls()
    cabeçalho('Aposentadoria de Jogador')
    data_nascimento = input("\n  Digite a data de nascimento\n  do jogador (DD/MM/AAAA): ")
    cls()
    cabeçalho('Aposentadoria de Jogador')
    nacionalidade = input("\n  Digite a nacionalidade\n  do jogador(ex. brasileiro): ")
    cls()
    cabeçalho('Aposentadoria de Jogador')
    altura = float(input("\n  Digite a altura do jogador\n  em metros(ex. 1.75): "))
    cls()
    cabeçalho('Aposentadoria de Jogador')
    peso = float(input("\n  Digite o peso do jogador\n  em kg(ex. 68): "))
    cls()
    cabeçalho('Aposentadoria de Jogador')
    jogador = Jogador(nome, posicao, data_nascimento, nacionalidade, altura, peso)
    jogador.imprimir_dados()
    
    linha()
    idade = jogador.calcular_idade()
    print(f'O jogador possui: {idade} anos')
    print(jogador.tempo_para_aposentar())
    linha()
    pause()

class Ingresso:
    def __init__(self, valor):
        self.valor = valor

    def imprimirValor(self):
        print(f'Valor do Ingresso Comum: R${self.valor:.2f}')


class IngressoVIP(Ingresso):
    def __init__(self, valor, valor_adicional):
        super().__init__(valor)
        self.valor_adicional = valor_adicional

    def valorIngressoVIP(self):
        return self.valor + self.valor_adicional

    def imprimirValorVIP(self):
        print(f'Valor do Ingresso VIP: R${self.valorIngressoVIP():.2f}')
        
def criar_ingresso():
        cls()
        cabeçalho('Ingressos')
        # Definindo valores dos ingressos
        valor_ingresso_comum = int(input("Valor do ingresso: "))
        valor_adicional_vip = 20.0 #Taxa extra do ingresso VIP

        cls()
        cabeçalho('Ingressos')
        # Criando instância de Ingresso
        ingresso_comum = Ingresso(valor_ingresso_comum)
        ingresso_comum.imprimirValor()

        # Criando instância de IngressoVIP
        ingresso_vip = IngressoVIP(valor_ingresso_comum, valor_adicional_vip)
        ingresso_vip.imprimirValorVIP()
        pause()


# -------------- Main ---------------- #

while True:
    cls()
    cabeçalho('Trabalho de POO')

    lista('Jogador,Ingresso,Fechar')

    op = int(input('Escolha: '))

    if op == 3:
        break
    
    elif op == 1:
        criar_jogador()
        
    elif op == 2:
        criar_ingresso()