text = "This is my test text. We're keeping this text short to keep things manageable."


def count_words(text):
    text = text.lower()
    skips = [",", ".", ";", ":", "'", '"']
    for skip in skips:
        text = text.replace(skip, "")
    word_counts = {}
    for word in text.split(" "):
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

from collections import Counter

def count_words_fast(text):
    text = text.lower()
    skips = [",", ".", ";", ":", "'", '"']
    for skip in skips:
        text = text.replace(skip, "")
    word_counts = Counter(text.split(" "))
    return word_counts

print(count_words(text))
print(count_words_fast(text))
print(len(count_words("This comprehension check is to check for comprehension.")))
print(count_words(text) is count_words_fast(text))
