# In this problem, the task is to read a code of
# a product 1, the number of units of product 1,
# the price for one unit of product 1, the code
# of a product 2, the number of units of product 2
# and the price for one unit of product 2. After
# this, calculate and show the amount to be paid.

code, num, price = input('Insira codigo, unidades, preco: ').split(" ")
code2, num2, price2 = input('Insira codigo, unidades, preco: ').split(" ")
amount1 = int(num)*float(price)
amount2 = int(num2)*float(price2)
total = amount1 + amount2
print('VALOR A PAGAR: R$ %.2f' %total)  # Boa pratica de comentario inline é dar 2 spaces after print and 1 after 'tralha'
