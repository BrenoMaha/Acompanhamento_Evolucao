'''
crie um programa que calcule sua velocidade dado o espaço e o tempo.
A Velocidade pode ser calculada pela fórmula:   Velocidade = Espaço / Tempo
Entrada: Seu programa deve receber dois números inteiros o espaço e o tempo, respectivamente.
Saída: A saída consiste em uma única linha contendo a velocidade alcançada.
Exemplo:
ENTRADA:
Espaço: 100
Tempo: 10
SAÍDA:
Velocidade: 10
'''

espaco = int(input("Qual a distancia percorrida? "))
tempo = int(input("Em quanto tempo a distancia foi percorrida? "))
velocidade = espaco / tempo
print(f"O valor da velocidade é de {velocidade}")
