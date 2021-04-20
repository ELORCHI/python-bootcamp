import sys

arg_len = len(sys.argv)
if arg_len <= 1:
    sys.exit()
morse_char = [[".-"], ["-..."], ["-.-."], ["-.."], ["."], ["..-."], ["--."],
        ["...."], [".."], [".---"], ["-.-"], [".-.."], ["--"], ["-."], ["---"],
        [".--."], ["--.-"], [".-."], ["..."], ["-"], ["..-"], ["...-"], [".--"],
        ["-..-"], ["-.--"], ["--.."]]
morse_number = [["-----"], [".----"], ["..---"], ["...--"], ["....-"],
        ["....."], ["-...."], ["--..."], ["---.."], ["----."]]
code = []
for index in range(1, arg_len):
    string = sys.argv[index]
    string = string.lower()
    for c in string:
        if c.isalpha():
            code += morse_char[ord(c) - 97]
        elif c.isdigit():
            code += morse_number[ord(c) - 48]
        else:
            print("ERROR")
            sys.exit()
print(*code)
