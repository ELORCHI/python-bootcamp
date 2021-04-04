import sys

def elementary_operations(a, b):
    summ = a + b
    Difference = a - b
    Product = a * b
    if b == 0:
        Quotient = "err"
        Remainder = "err"
    else:
       Quotient = a / b
       Remainder = a % b
    return (summ, Difference, Product, Quotient, Remainder)

error = False
nb_args = len(sys.argv) - 1
arg1 = 0
arg2 = 0
tup = ()
if nb_args > 2:
    print("InputError: too many arguments")
    error = True
elif nb_args < 2:
    print("InputError: few arguments")
    error = True
elif (isinstance(sys.argv[1], int)) or (isinstance(sys.argv[2], int)):
    print("InputError: only numbers")
    error = True
if error:
    print("Usage: python operations.py <number1> <number2> \nExample:\n\tpython operation.py 10 3")
else:
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    tup = elementary_operations(int(arg1), int(arg2))
    print("SUM:         " + str(tup[0]))
    print("Difference:  " + str(tup[1]))
    print("Product:     " + str(tup[2]))
    print("Quotient:    " , end="")
    if tup[3] != "err":
        print(str(tup[3]))
    else:
        print("ERROR (div by zero)")
    print("Remainder:   " , end="")
    if tup[3] != "err":
        print(str(tup[4]))
    else:
        print("ERROR (modulo by zero)")
