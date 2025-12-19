def get_num_words(text: str) -> int:
    return len(text.split())


def characters_frequency(text: str):
    """
    Returns sorted list of dictionaries with character frequencies in the given text.
    {'char': character, 'num': frequency}
    """
    frequency = []
    for char in text:
        if char.isalpha():
            char = char.lower()
            found = False
            for entry in frequency:
                if entry["char"] == char:
                    entry["num"] += 1
                    found = True
                    break
            if not found:
                frequency.append({"char": char, "num": 1})
    frequency.sort(key=sort_on, reverse=True)
    return frequency


def pretty_print_char_freq(freq_list: list) -> str:
    result = ""
    for entry in freq_list:
        result += f"{entry['char']}: {entry['num']}\n"
    return result


def sort_on(items):
    return items["num"]
