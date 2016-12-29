import os
import pandas as pd

def read_book(title_path):
    """
    read a book and return it as a string
    :param title_path: path to book
    :return: string with book content
    """
    with open(title_path, "r", encoding="utf-8") as current_file:
        text = current_file.read()
        text = text.replace("\n", "").replace("\r", "")
    return text


def word_stats(word_counts):
    number_unique = len(word_counts)
    counts = word_counts.values()
    return number_unique, counts


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


def word_count_distribution(text):
    result = {}
    words = count_words(text)
    for count in words.values():
        if count in result:
            result[count] += 1
        else:
            result[count] = 1
    return result



import matplotlib.pyplot as plt
def read_all_books_with_stats(book_dir):
    stats = pd.DataFrame(columns= ("language", "author", "title", "length", "unique"))
    title_number = 1
    for language in os.listdir(book_dir):
        language_dir = os.path.join(book_dir, language)
        for author in os.listdir(language_dir):
            author_dir = os.path.join(language_dir, author)
            for title in os.listdir(author_dir):
                input_file = os.path.join(author_dir, title)
                # print(input_file)
                text = read_book(input_file)
                number_unique, counts = word_stats(count_words(text))
                stats.loc[title_number] = language, author.capitalize(), title.replace(".txt", ""), sum(counts), number_unique
                title_number += 1
    # plt.plot(stats.length, stats.unique, "bo")
    # plt.loglog(stats.length, stats.unique, "bo")
    plt.figure(figsize=(10, 10))
    subset = stats[stats.language == "English"]
    plt.loglog(subset.length, subset.unique, "o", label="English", color="crimson")
    subset = stats[stats.language == "French"]
    plt.loglog(subset.length, subset.unique, "o", label="French", color="forestgreen")
    subset = stats[stats.language == "German"]
    plt.loglog(subset.length, subset.unique, "o", label="German", color="orange")
    subset = stats[stats.language == "Portuguese"]
    plt.loglog(subset.length, subset.unique, "o", label="Portuguese", color="blueviolet")
    plt.legend()
    plt.xlabel("Book length")
    plt.ylabel("Number of unique words")
    plt.savefig("plot.pdf")

    plt.show()
    # print(stats.head(8))



def my_test_pandas():
    table = pd.DataFrame(columns = ("name", "age"))
    table.loc[-1] = "Jan", 34
    table.loc[0] = "John", 24
    table.loc[1] = "James", 22
    table.loc[2] = "Jess", 32
    print(table)
    print(table.columns)


def more_frequent(distribution):
    result = {}
    actual_words = all_words = sum(distribution.values())
    for how_many in sorted(distribution):
        actual_words -= distribution[how_many]
        if actual_words>0:
            result[how_many] = all_words / actual_words
        else:
            result[how_many] = 0.0
    return result

def test_homework():
    text = read_book("Books\English\shakespeare\Romeo and Juliet.txt")
    distribution = word_count_distribution(text)
    frequency = more_frequent(distribution)
    print(frequency)
    number_unique, counts = word_stats(count_words(text))

if __name__ == '__main__':
    # read_all_books_with_stats("./Books")
    test_homework()
    # my_test_pandas()
# word_counts = count_words(text)
# number_unique, counts = word_stats(word_counts)
# print(number_unique)
# print(sum(counts))

# index = text.find("What's in a name?")
# print(index)
# sample_text = text[index : index + 1000]
# print(sample_text)
