heads = []
news = []
author = ""
hour = ""
for i in range(3):
    print("Podaj nagłówek nr " + str(i + 1) + ": ")
    heads.append(input())
for i in range(3):
    print("Podaj newsa nr " + str(i + 1) + ": ")
    news.append(input())
print("Podaj autora: ")
author = input()
print("Podaj godzinę: ")
hour = input()