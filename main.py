def main():    
    path_to_book = "books/frankenstein.txt"
    text = get_text(path_to_book)
    number_of_words = get_number_of_words(text)
#    lowercase_text = make_lowercase(text)
    return print(f"The book contains {number_of_words} words.")

def get_text(path):
    with open(path) as f:
        return f.read()
    

def get_number_of_words(text):
    words = text.split()
    return len(words)
 

#def make_lowercase(text):
#    return text.lower()
    

#def get_word_list(lowercase_text):
#    return lowercase_text.split()

#def get_characters(word_list):
#    return word_list.split()

main()

