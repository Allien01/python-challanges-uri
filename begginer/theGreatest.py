# Make a program that reads 3 integer values
# and present the greatest one followed by the
# message "eh o maior".

a, b, c = input('Insira 3 numeros: ').split(' ')
numeros = [int(a), int(b), int(c)]
maior = None

for i in numeros:
    if maior == None:
        maior = i
    elif maior < i:
        maior = i
    else:
        continue
print('%i eh o maior' %maior)
