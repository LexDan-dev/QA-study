def filter_long_words(words):
    result = []
    for word in words:
        if len(word) > 5:
            result.append(word)
    return result


words = ["кот", "Машина", "акробат", "Москва", "туча", "дом", "самолет"]
print(filter_long_words(words))
