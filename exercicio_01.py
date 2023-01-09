'''
Exercicio nivel facil, onde se pede para que se crie uma sequencia de numeros do 1 até o numero digitado pelo usuario
exemplo:
1
2 2
3 3 3 
4 4 4 4
....
. . . . n
'''

def piramide(x):
    '''
    imprime a quantidade de um numero até que chegue no numero digitado pelo usuario 

    parametros:
    x = numero digitado e ultimo numero a ser exibido na sequencia
    '''
    for i in range (1, x + 1):
        cont = 1
        while True:
            print(i, end = '  ')
            if cont == i:
                break
            cont += 1
        print()

x = int(input('Digite o numero: '))
piramide(x)