import sys
if len(sys.argv) != 3 or isinstance(sys.argv[0], str) == False  or sys.argv[2].isdigit() == False:
    print("ERROR")
else:
    tab_words = sys.argv[1].split()
    filter_tab = [word for word in tab_words if len(word) > int(sys.argv[2])]
    for i in range(len(filter_tab)):
        for char in filter_tab[i]:
            if char in "!\"#$%&'()*+,-./:;<=>?@[\]^`{|}~":
                filter_tab[i] = filter_tab[i].replace(char, '')
    print(filter_tab)
