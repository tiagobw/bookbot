def count_words(text):
    return len(text.split())


def count_chars(text):
    result = {}
    for char in text:
        lower_char = char.lower()
        if lower_char not in result:
            result[lower_char] = 0
        result[lower_char] += 1
    return result
