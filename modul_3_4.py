# функцию single_root_words, которая принимает
# одно обязательное слово в параметр root_word,
# а далее неограниченную последовательность в параметр *other_words
def single_root_words(root_word, *other_words):
    same_words = [] # Создаём внутри функции пустой список
    for words in other_words: # При помощи цикла for перебираем
                             # предполагаемо подходящие слова
        if root_word in words or words in root_word or words.lower() in root_word:
            same_words.append(words)
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
