Exercício 1 — Números únicos e estatísticas

Peça 10 números inteiros ao usuário.

Depois:

armazene todos em uma lista

crie um set com os números únicos

imprima:

a lista original

o set

quantos números repetidos foram digitados

a média dos números

Dica: set(), len(), sum()


lista=[] # cria uma lista vazia

while len(lista) < 10:
    x=int(input("Diga um número: "))
    lista.append(x)
    1

print('Lista que você digitou:: ',lista)    
s=set(lista)
print('total de números repetidos: ' , len(lista)-len(s))

print(s)
contagem={}

for i in lista:
    if i in contagem:
        contagem[i] += 1
    else:
        contagem[i] = 1
        
print('contagem' ,contagem)    

media=sum(lista)/len(lista)
print(media)
        
Exercício 2 — Classificação de palavras

Peça uma frase ao usuário.

Depois:

transforme em lista de palavras

crie duas listas:

palavras com até 4 letras

palavras com mais de 4 letras

imprima as duas listas

mostre quantas palavras há em cada uma

 Dica: split(), len(), append()

frase=input("Escreva uma frase: ")
lista=frase.split()
print(lista)


list2=[x for x in lista if len(x) <= 4]
print(list2 )
print(f"Há {len(list2)} palavras com até 4 letras\n")

list3=[x for x in lista if len(x) > 4]
print(list3 )
print(f"Há {len(list3)} palavras com mais de 4 letras")

 Exercício 3 — Cadastro com verificação

Crie um programa que:

peça nome, idade e cidade

armazene em um dicionário

Depois:

se a idade for menor que 18, imprima "Acesso negado"

se for maior ou igual a 18:

percorra o dicionário

imprima no formato chave -> valor

name=input("Qual o seu nome: ")
age=int(input("Qual a sua idade: "))
city=input("Qual a sua cidade: ")

dic={"nome":name, 
     "idade":age,
     "cidade":city
     
}

if age < 18:
    print("Acesso negado")
else:
    for x, y in dic.items():
        print(x, " -> ", y)

 Dica: if, dict.items()

 Exercício 4 — Contador avançado (dict + set)

Peça uma frase ao usuário.

Depois:

conte quantas vezes cada palavra aparece

imprima apenas as palavras que aparecem mais de uma vez

crie um set dessas palavras repetidas

imprima o set e a quantidade de palavras repetidas

 Dica: padrão de contagem com dicionário

 Exercício 5 — Desafio final (mentalidade de programador)

Crie uma lista inicial:

dados = [10, 20, 20, 30, 40, 40, 50]


O programa deve:

remover duplicados usando set

converter de volta para lista

ordenar a lista

criar um dicionário no formato:

{
  "valores": [...],
  "total": soma dos valores,
  "quantidade": quantidade de valores,
  "maior": maior valor,
  "menor": menor valor
}


Depois:

percorra o dicionário e imprima tudo com for

 Objetivo: pensar em dados, estrutura e lógica, não só código.


dados = [10, 20, 20, 30, 40, 40, 50]
s=set(dados)
dados=list(s)
dados.sort()


dic={
  "valores": dados,
  "total": sum(dados),
  "quantidade": len(dados),
  "maior": dados[-1],
  "menor": dados[0]
}

for x,y in dic.items():
    print(x ,"->", y)







'''Exercício 1'''

pessoas = {
    "p1": {"nome": "Ana", "idade": 22},
    "p2": {"nome": "Carlos", "idade": 17},
    "p3": {"nome": "Maria", "idade": 30}
    }

for x, table in pessoas.items():
    if table["idade"] > 18:
        print(table["nome"])
''' Imprima apenas os nomes das pessoas maiores de idade.'''

''' Exercício 2'''

dicionario={
    "produto1" : {
        "nome" : "x",
        "preço" : 10,
        "estoque" : 1},   
    "produto2": {
        "nome" : "y",
        "preço" : 15,
        "estoque" : 3},
    "produto3" :{
        "nome" : "z",
        "preço" : 50,
        "estoque" : 0}

    }

for x, dicio in dicionario.items():
    if dicio["estoque"] > 0:
        print(dicio["nome"]) #retornará apenas o nome do produto

'''Crie um dicionário aninhado com 3 produtos, cada um contendo:

nome

preço

estoque

Depois:

imprima apenas produtos com estoque > 0

 Exercício 3 (desafio 🏆)

Peça dados de alunos até o usuário digitar "sair"
Armazene tudo em um dicionário aninhado
Depois:

imprima todos os alunos

calcule a média das idades