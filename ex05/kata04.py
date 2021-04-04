tup = ( 0, 4, 132.42222, 10000, 12345.67)

print("module_00, ex_04 : ", end="")
tmp = 0.0
leni = len(tup)
for i in range(2, leni):
    print(str('%.2e' % tup[i]) + " ", end="")
