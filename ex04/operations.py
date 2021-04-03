import sys

def elementary_operations(a, b)
    summ = a + b
    Difference = a - b
    Product = a * b
    if b == 0:
        Quotient = false
        Remainder = false
    else
       Quotient = a / b
       Remainder = a % b
    return (summ, Difference, Product, Quotient, Remainder)

error = false
nb_args = len(sys.arg) - 1
arg1 = sys.argv[1]
arg2 = sys.argv[2]
tup
if nb_args > 2:
    print("InputError: too many arguments")
    error = true
elif nb_args < 2:
    print("InputError: few arguments")
    error = true
elif type(arg1) != int or type(arg2) != int:
    print("InputError: only numbers")
    error = true
if error:
    print("Usage: python operations.py <number1> <number2> \n Example:\n
        python operation.py 10 3")
else:
    tup = elementary_operations(arg1, arg2)
    print(f"Sum:\t\t%d\nDifference: \t".format(tup[0]), formar(tup[1]))
    print(f"Product\t
