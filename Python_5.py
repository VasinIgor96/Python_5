def sort_words_by_length(words):
    return sorted(words, key=len)
words = ["Яблука","Полуниця", "Банани", "Апельсини", "Ківі","Фрукти"]
sorted_words = sort_words_by_length(words)
print(sorted_words)