import sys

i = len(sys.argv) - 1;
t = 0;
txt = ""
while i > 0:
    t = len(sys.argv[i]) - 1;
    while t >= 0:
        if (sys.argv[i][t]).isupper():
            txt += (sys.argv[i][t]).lower();
        else:
            txt += (sys.argv[i][t]).upper();
        t += -1;
    i += -1;
    if i > 0:
        txt += ' ';
print(txt);
