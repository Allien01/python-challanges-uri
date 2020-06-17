# Make a program that calculates and shows
# the volume of a sphere being provided the
# value of its radius (R) . The formula to
# calculate the volume is: (4/3) * pi * R3.
# Consider (assign) for pi the value 3.14159.

pi = 3.14159
r = float(input('Insira o raio: '))  # The input contains a value of floating point (double precision
volume = ((4/3)*pi*(r**3))
print('VOLUME = %.3f' %volume)  # The value must be presented with 3 digits after the decimal point.
