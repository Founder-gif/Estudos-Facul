# Definindo a classe Cidade para representar cidades com nome e população
class Cidade:
    def _init_(self, nome, populacao):
        self.nome = nome
        self.populacao = populacao

# Definindo a classe Estado para representar estados com nome, sigla e lista de cidades
class Estado:
    def _init_(self, nome, sigla):
        self.nome = nome
        self.sigla = sigla
        self.cidades = []

    # Método para adicionar uma cidade à lista de cidades do estado
    def adicionar_cidade(self, cidade):
        self.cidades.append(cidade)

    # Método para calcular a população total do estado somando as populações de suas cidades
    def calcular_populacao_total(self):
        populacao_total = sum(cidade.populacao for cidade in self.cidades)
        return populacao_total

# Criando algumas instâncias da classe Cidade com nome e população
cidade1 = Cidade("São Paulo", 12000000)
cidade2 = Cidade("Rio de Janeiro", 6500000)
cidade3 = Cidade("Belo Horizonte", 2500000)
cidade4 = Cidade("Curitiba", 1900000)
cidade5 = Cidade("Salvador", 2900000)

# Criando algumas instâncias da classe Estado com nome e sigla
estado1 = Estado("São Paulo", "SP")
estado1.adicionar_cidade(cidade1)  # Adicionando cidade1 ao estado1
estado1.adicionar_cidade(cidade2)  # Adicionando cidade2 ao estado1

estado2 = Estado("Minas Gerais", "MG")
estado2.adicionar_cidade(cidade3)  # Adicionando cidade3 ao estado2

estado3 = Estado("Paraná", "PR")
estado3.adicionar_cidade(cidade4)  # Adicionando cidade4 ao estado3
estado3.adicionar_cidade(cidade5)  # Adicionando cidade5 ao estado3

# Calculando e exibindo a população de cada estado
print(f"\tPopulação de {estado1.nome} ({estado1.sigla}): {estado1.calcular_populacao_total()} habitantes")

print(f"\tPopulação de {estado2.nome} ({estado2.sigla}): {estado2.calcular_populacao_total()} habitantes")

print(f"\tPopulação de {estado3.nome} ({estado3.sigla}): {estado3.calcular_populacao_total()} habitantes")