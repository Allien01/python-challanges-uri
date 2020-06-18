# Make a program that reads three floating point values: A, B and C. Then, calculate and show:
# a) the area of the rectangled triangle that has base A and height C.
# b) the area of the radius's circle C. (pi = 3.14159)
# c) the area of the trapezium which has A and B by base, and C by height.
# d) the area of ​​the square that has side B.
# e) the area of the rectangle that has sides A and B.

pi = 3.14159
a, b, c = input('Insira 3 medidas: ').split(' ')
triangleRtg = (float(a)*float(c))/2
circle = pi*(float(c)**2)
trapezium =(float(a)+float(b))*float(c)/2
square = float(b)**2
rectangle = float(a)*float(b)
print('TRIANGULO: %.3f' %triangleRtg)
print('CIRCULO: %.3f' %circle)
print('TRAPEZIO: %.3f' %trapezium)
print('QUADRADO: %.3f' %square)
print('RETANGULO: %.3f' %rectangle)
