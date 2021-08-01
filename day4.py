#function to convert celsius into fahrenheit
def fahrenheit(celsius):
    #fahrenheit conversion
    Fahrenheit=celsius*(9/5)+32
    return Fahrenheit

#getting input value for celsius
celsius=int(input("Enter the temperature in celsius:"))
#calling function
Fahrenheit_from_celsius=fahrenheit(celsius)
print("The Fahrenheit value for celsius {} is:{}".format(celsius,Fahrenheit_from_celsius))
