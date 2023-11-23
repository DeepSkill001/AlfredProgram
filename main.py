from words import words
import random

print("Добро пожаловать в наш тренажёр!")
print("Сколько слов готовы перевести?")
answer = input()
answer = int(answer)
print("Ваш выбор:", answer, "слов(а).Удачи!")

count = 0

for i in range(answer):

    word, key = random.choice(list(words.items()))

    print("Введите превод слова -", word)
    ans_word = input()

    if ans_word == key:
        count += 1
        print("Вы правы, ответом на слово", word, "будет", key)
        print("Правильно переведено -", count, "слов(а)")
        print("Поздравляю вы перевели -", count, "слов из", answer)
    else:
         print("К сожалению вы ошиблись в переводе слова", word, "его переводом станет слово", key)
         print("Вы перевели -", count, "слов из", answer)

print("Работа программы успешно завершена.")


