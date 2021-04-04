languages = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
    }

for item in languages.items():
    print(str(item[0]) + "was created by " + str(item[1]))
