# Make a program that reads a seller's name,
# his/her fixed salary and the sale's total
# made by himself/herself in the month
# (in money). Considering that this seller
# receives 15% over all products sold, write
# the final salary (total) of this seller at
# the end of the month , with two decimal places.

name = input('Informe seu nome: ')
salary = float(input('Informe seu salario: '))
salesTotal = float(input('Informe o total das vendas: '))
total = salary + (salesTotal*0.15)
print('TOTAL = R$ %.2f' %total)
