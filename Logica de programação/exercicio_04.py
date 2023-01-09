'''
Faça um programa para o cálculo de uma folha de pagamento
sabendo que os descontos são do imposto de renda, que depende do salário bruto (conforme tabela abaixo)
3% para o Sindicato
e que o FGTS corresponde a 11% do salário bruto,
mas não é descontado (é a empresa que deposita.)
O salário líquido corresponde ao salário bruto menos os descontos.
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
a. Desconto do IR;
b. Salário Bruto ate R$900,00 (inclusive) – Isento;
c. Salário Bruto de R$ 1500, 00 (inclusive) – desconto de 5%;
d. Salario bruto até R$ 2500,00 (Inclusive) – desconto de 10%;
e. Salário bruto acima de 2500 – Desconto de 20%.
'''

horas = int(input("Quantas horas foram trabalhadas ? "))
valorhora = int(input("Qual valor da hora trabalhada? R$"))
salario = horas * valorhora
inss =  salario * 0.05
if salario < 900:
    ir = 0
if salario <= 1500:
    ir = salario * 0.05
if salario <= 2500:
    ir = salario * 0.1
else:     
    ir = salario * 0.2
sindicato = salario * 0.03
fgts = salario * 0.11
total = ir + inss + sindicato
liquido = salario - total
print(f"valor do salario bruto: R${salario}")
print(f"valor do desconto de imposto de renda: R${ir}")
print(f"valor do desconto de INSS: R${inss}")
print(f"valor do desconto de Sindicato: R${sindicato}")
print(f"Valor de FGTS depositado pela empresa: R${fgts}")
print(f"O Total de descontos do sálario é de R${total}")
print(f"O salario liquido tem um valor de R${liquido}")
