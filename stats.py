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


def get_num(sorted_chars):
    return sorted_chars["num"]


def generate_sort_chars(chars_count):
    result = []
    for key, value in chars_count.items():
        item = {}
        item["char"] = key
        item["num"] = value
        result.append(item)
    result.sort(reverse=True, key=get_num)
    return result


def print_sorted_chars(sorted_chars):
    for item in sorted_chars:
        char = item["char"]
        num = item["num"]
        if char.isalpha():
            print(f"{char}: {num}")
