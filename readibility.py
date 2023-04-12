def main():
    text = input("Text: ")
    letters = count_letters(text)
    words = count_words(text)
    sentences = count_sentences(text)
    index = coleman_liau_index(letters, words, sentences)
    if index < 1:
        print("Before Grade 1")
    elif index >= 16:
        print("Grade 16+")
    else:
        print(f"Grade {index}")


def count_letters(text):
    return len([letter for letter in text if letter.isalpha()])


def count_words(text):
    return len(text.split())


def count_sentences(text):
    sentences = 0
    for i in text:
        if i == "." or i == "!" or i == "?":
            sentences += 1
    return sentences


def coleman_liau_index(letters, words, sentences):
    L = letters / words * 100
    S = sentences / words * 100
    index = 0.0588 * L - 0.296 * S - 15.8
    return round(index)


while True:
    if __name__ == "__main__":
        main()
