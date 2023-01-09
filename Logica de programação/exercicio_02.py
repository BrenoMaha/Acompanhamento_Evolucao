'''
faça um programa que leia um número de ponto flutuante (Número Real) e mostre na tela o seu dobro e a sua terça parte.
Exemplo:
ENTRADA:Número: 2.5
SAÍDA:Dobro: 5.0
Terça Parte: 0,83
'''

numero = float (input("digite aqui um numero: "))
dobro = numero * 2
terco = numero / 3
print(f"o dobro do numero {numero} tem valor de {dobro} ")
print(f"a terça parte do numero {numero} tem valor de {terco}")