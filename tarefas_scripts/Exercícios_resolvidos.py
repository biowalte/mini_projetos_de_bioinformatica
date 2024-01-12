'''
1- Faça um programa que receba a idade do usuário e
diga se ele é maior ou menor de idade.
2- Faça um programa que receba duas notas digitadas pelo usuário.
Se a nota for maior ou igual a seis, escreva aprovado, senão escreva reprovado.
3- Escreva um programa que resolva uma equação de segundo grau.
4- Escreva um programa que ordene uma lista numérica com três elementos.
5- Escreva um programa que receba dois números e um sinal,
e faça a operação matemática definida pelo sinal.
'''

#1.

idade = input('Digite sua idade: ')
idade = int(idade)
if idade >= 0 and idade < 18: 
    print("Voce é menor de idade!") 

elif idade >= 18 and idade < 70: 
    print("você é maior de idade!") 
#1
else: 
    print ("Idade invalida!")


#2.
nota1 = float(input('Digite um número: '))
nota2 = float(input('Digite outro número: '))
media23 = (nota1 + nota2) / 3

print('A média dos números é ', media23)
print('A média dos números é ', media23)


#3. 
# a.2 + b.x + c
#   (-b +- sqtr(b2-4ac))/2
from math import sqrt
a = int(input('digite o valor de a:'))
b = int(input('digite o valor de b:'))
c = int(input('digite o valor de c:'))

delta = ((b ** 2) - 4) * a * c
raiz_delta = sqrt(delta)

x1 = (-b + raiz_delta)/2*a
x2 = (-b - raiz_delta)/2*a

print('x1 = %d' %x1)
print('x2 = %d' %x2)


#4. 
usando algoritimo sorted
lista = (2, 3, 1)
lista = sorted(lista)
print(lista)

#OU usando algoritimo select sort

lista = (2, 3, 1)

for i in range(len(lista)):
    
    menor = i 
    
    for j in range(i+1, len(lista)):

        if lista[j] < lista[menor]:
            menor = j

    if lista[i] != lista[menor]:
            aux = lista[i]
            lista[i] = lista[menor]
            lista[menor] = aux

print(lista)


#5.
 
num1 = int(input("digite um numéro"))
operador = input("digite um operador")
num2 = int(input("digite outro número"))

#soma:
if operador == "+":
    resultado = num1 + num2
    print(resultado)
#subtração:
elif operador == "-":
    resultado = num1 - num2 
    print(resultado)
#divisão:
elif operador == "/":
    resultado = num1 / num2
    print(resultado)
#multiplicação:
elif operador == "*":
    resultado = num1 * num2
    print(resultado)
#exponenciação:
elif operador == "**":
    resultado = num1 ** num2
    print(resultado)
else:
    print('Esta é uma simples calculadora, por favor digite apenas 2 números\
          e um operador: *, **, +, -, /,')