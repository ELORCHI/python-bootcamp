import sys

c = sys.argv;
if (len(c) >= 2):
    if (c[1].isdigit()):
        if (int(c[1]) == 0):
            print("I'm Zero");
        elif (int(c[1]) % 2 == 0):
            print("I'm Even.");
        else:
            print("I'm Odd.");
    else:
        print("ERROR");
