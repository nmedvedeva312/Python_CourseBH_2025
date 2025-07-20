'''
Запросить фразу состоящую минимум из трех слов. 
Сформировать фразу из этих слов в которой каждая буква слова, 
продублирована то количество раз, которое соответствует номеру позиции 
данной буквы в слове этой буквы. 
Например: Привет как дела => Прриииввввееееетттттт кааккк деелллаааа

'''

while True:
    phrase = input("Введите фразу из минимум трёх слов: ").strip()
    words = phrase.split() # split() создаёт список слов.
    if len(words) < 3:
        print("Ошибка: нужно минимум три слова.")
    else:
        break

result_words = []

for word in words:
    new_word = ""
    for i, ch in enumerate(word, start=1):
        new_word += ch * i  # буква дублируется i раз, i — позиция буквы
    result_words.append(new_word)

result_phrase = " ".join(result_words)
print(result_phrase)

s = "How are you".split()

# s1 = ''.join(''.join(char * i for i, char in enumerate(word, 1)) for user in users)