def funch(div1,div2):
    division = div1/div2
    print(division)

num1 = 5
num2 = 0 
try:
    funch(num1,num2)
except ZeroDivisionError:
    print("No se puede dividir por 0")
