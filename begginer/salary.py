'''
Write a program that reads an employee's number,
his/her worked hours number in a month and the
amount he received per hour. Print the employee's
number and salary that he/she will receive at end
of the month, with two decimal places.
'''

number = int(input('Informe um numero: '))
hour = int(input('Informe as horas trabalhadas: '))
rate = float(input('Informe quantia recebida pro hora: '))
salary = hour*rate
print('NUMBER =', number)
print('SALARY = U$ %.2f' %salary)
