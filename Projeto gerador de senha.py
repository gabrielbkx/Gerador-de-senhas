print("BEM VINDO AO GERADOR DE SENHAS")
quantidade_de_letras = int(input("quantas letras voce quer que a sua senha tenha?\n"))
quantidade_de_simbolos = int(input("Quantos símbolos você deseja que sua senha tenha?\n"))
quantidade_de_numeros = int(input("Quantos números terá na sua senha?\n"))
import random
import string
#criando as listas
lista_de_letras_minusculas = list(string.ascii_lowercase)

lista_de_letras_maiusculas = list(string.ascii_uppercase)
lista_de_simbolos = list(string.punctuation)

senha = []

for c1 in  range(0,quantidade_de_letras):
    #aleatoriedade 1
    letras_aleatorias = random.choice(lista_de_letras_maiusculas + lista_de_letras_minusculas)
    senha.append(letras_aleatorias)
for c2 in range (quantidade_de_simbolos):
    # aleatoriedade 2
    simbolos_aleatorios = random.choice(lista_de_simbolos)
    senha.append(simbolos_aleatorios)
for c3 in range (0,quantidade_de_numeros ):
    # aleatoriedade 3
    numeros_aleatorios = random.randint(0, 9)
    senha.append(str(numeros_aleatorios))

senha_string = "".join(senha)
print(f"Aqui esta a sua senha {senha_string}")