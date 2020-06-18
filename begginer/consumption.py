# Calculate a car's average consumption being
# provided the total distance traveled (in Km)
# and the spent fuel total (in liters).

X = input('Informe a distancia: ')
Y = input('Informe o total de combustivel gasto: ')
total = int(X)/float(Y)
print('%.3f km/l' %total)
