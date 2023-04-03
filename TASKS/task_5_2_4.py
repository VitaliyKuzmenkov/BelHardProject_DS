"""Требуется реализовать программу, которая выводит слово,
имеющее максимальную длину (или список слов, если таковых несколько).
"""
with open('info.txt', 'r', encoding='utf-8') as text_file:
    file = [i.strip('\n') for i in text_file]
    print(file)
    max_len = 0
    lst = list()
    for word_file in file:
        for sing in word_file:
            if len(word_file) >= max_len:
                max_len = len(word_file)
                max_word = word_file
        if len(max_word) == len(word_file):
            lst.append(max_word)
    print(lst)

