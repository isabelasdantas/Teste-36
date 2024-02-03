casa = float(input('Qual o valor da casa? R$: '))
salario = float(input('Quanto você recebe? R$: '))
anos = int(input('Em quanto anos você quer pagar?'))
mensal = casa / (anos * 12)
porcent = mensal * 30 / 100
print('Para pagar uma casa no valor de R${:.2f} em {} anos, a prestação fica no valor de R${:.2f}.'
.format(casa, anos, mensal))
if (salario <= porcent):
        print('Empréstimo pode ser CONCEDIDO')
else:
        print('Empréstimo foi NEGADO')
