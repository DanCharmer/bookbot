def count_text(text):
    number_of_words = len(text.split())
    return number_of_words

def count_characters(text):
    text = text.lower()
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_character_counts(char_count):
    char_list = [{"char": char, "count": count} for char, count in char_count.items() if char.isalpha()]
    char_list.sort(key=lambda x: x["count"], reverse=True)
    
    return char_list