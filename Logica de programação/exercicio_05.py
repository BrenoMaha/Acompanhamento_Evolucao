'''
Um determinado grupo empresarial resolveu dar um aumento de salário aos seus colaboradores 
para isso, contrataram você para desenvolver um programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador
calcule o reajuste segundo os critérios abaixo, que deverá exibis o novo salário, baseado no salário atual. 
Salários até R$ 280,00 (incluindo): aumento de 20%,
Salários entre R$ 280,00 e R$700,00: aumento de 15%;
Salários entre R$ 700,00 e R$ 1500,00: aumento de 10%;
Salários de R$ 1500,00 em diante: aumento de 5%;
'''

salario = float (input("Qual valor do salario? R$"))
if salario <= 280:
    print(f"O salário com aumento vai para um valor de:R${salario + salario*0.2}")
if((salario>=281 )and (salario<=700)):
    print(f"O salario com aumento vai para um valor de:R${salario + salario*0.15}")
if((salario>=701)and(salario<=1500)):
    print(f"O salario com aumento vai para um valor de: R${salario + salario*0.1}")
if(salario>=1501):
    print(f"O salario com aumento vai para um valor de: R${salario + salario*0.05}")
