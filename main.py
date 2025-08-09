def get_book_text(books):
    with open(books) as f:
        file_contents = f.read()
    return file_contents

#def main():
    #print(get_book_text("bookbot/books/frankenstein.txt"))

#main()

#book_contents = "Thats so fucking stupid thats been my entire fucking problem why was that not made clear you stipid piece of shit"
book_path = "books/frankenstein.txt"

book_contents = get_book_text(book_path)

from stats import count_words
how_many_times = count_words(book_contents)
print(f"{how_many_times} words found in the document")


from stats import count_each_character
how_many_characters = count_each_character(book_contents)
print(how_many_characters)