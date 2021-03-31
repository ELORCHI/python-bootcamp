import string

def text_analyzer(*argv):
    """    This function counts the number of upper characters, lower characters, punctuation and spaces in a given text."""
    c = len(argv);   
    if (c == 0):
        args = input("What is the text to analyse?");
        c = len(args);
    else:
        args = argv[0];
    if (c == 1):
        arg_len = len(args);
        index = 0;
        upper = 0;
        lower = 0;
        pun = 0;
        spaces = 0;
        while index < arg_len:
            if args[index].isupper():
                upper += 1;
            elif args[index].islower():
                lower += 1;
            elif args[index].isspace():
                spaces += 1;
            elif args[index] in string.punctuation:
                pun += 1;
            index += 1;
        print("The text contains " + str(arg_len) + " characters");
        print(str(upper) + " upper letters");
        print(str(lower) + " lower letters");
        print(str(pun) + " punctuation marks");
        print(str(spaces) + " spaces");
    else:
        print("ERROR");
