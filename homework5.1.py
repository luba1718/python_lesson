# Напишите программу, удаляющую из текста все слова, содержащие "абв". 
# В тексте используется разделитель пробел.
# in Number of words: 10
# out авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба
# in Number of words: 6
# out ваб вба абв ваб бва абв
# ваб вба ваб бва
# in Number of words: -1
# out The data is incorrect

import random
txt = "abc"
print("что нужно удалить из текста: ", txt)
num_word = (int(input("введите колличество слов в текте: ")))
word_list = []
print("random text: ")
for j in range(num_word):
    random_txt = random.sample(txt, 3)
    word_list.append("".join(random_txt))
print(" ".join(word_list))
print("текст без abc: ")
word_list2 = list(filter(lambda j: txt not in j, word_list))
print(" ".join(word_list2))