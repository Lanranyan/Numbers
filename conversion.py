'''
Convert from F to C, and C to F
'''

degree = input(" Enter c for Celsius, or f for Fahrenheit :")
temperature = int(input(" Enter the temperature value :"))

if degree == 'f': # "==" is identical
    C = (temperature - 32)*5/9
    print("The temperature in celsius is ",round(C))
elif degree == 'c':
    F = temperature*9/5 + 32
    print("The temperature in Fahrenheit is : ",round(F))
else :
    print("There's no such degree like : ", degree)

exit()