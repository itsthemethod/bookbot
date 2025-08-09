from stats import (
    count_words, 
    count_each_character, 
    chars_dict_to_sorted_list,
)

def main():
        #print(get_book_text("bookbot/books/frankenstein.txt"))
    #book_contents = "Thats so fucking stupid thats been my entire fucking problem why was that not made clear you stipid piece of shit"
    book_path = "bookbot/books/frankenstein.txt"
    book_contents = get_book_text(book_path)
    
   
    how_many_times = count_words(book_contents)
   
    how_many_characters = count_each_character(book_contents)
   
    chars_dictionary = chars_dict_to_sorted_list(how_many_characters)


    print_report(book_path, how_many_times, chars_dictionary)
    
    #print(f"{how_many_times} words found in the document")
    #print(how_many_characters)


def get_book_text(books):
    with open(books) as f:
        file_contents = f.read()
    return file_contents


def print_report(book_path, how_many_characters, chars_dictionary):
     print("============ BOOKBOT ============")
     print(f"Analyzing book found at {book_path}...")
     print("----------- Word Count ----------")
     print(f"Found {how_many_characters} total words")
     print("--------- Character Count -------")
     for item in chars_dictionary:
         if not item["char"].isalpha():
             continue
         print(f"{item["char"]}: {item["num"]}")
     print("============= END ===============")


main()