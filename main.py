def main():    
    path_to_book = "books/frankenstein.txt"
    text = get_text(path_to_book)
    number_of_words = get_number_of_words(text)
    characters = count_characters(text)
    alpha_characters = make_alpha(characters)
    list_of_dict = make_list_of_dict(alpha_characters)
    expanded_list_dictionary = make_values_to_keys(alpha_characters)
    expanded_list_dictionary.sort(reverse=True, key=sort_on)

    print(f"--- Begin report of {path_to_book} ---")
    print(f"The word count is {number_of_words}.")
    for line in expanded_list_dictionary:
        print(f"The '{line['letter']}' character was found {line['num']} times.")
    print("--- End report ---")
    #print(list_of_dict)
    #print(alpha_characters)
    #return print(f"The book contains {number_of_words} words.")

#def test_main():
#    test_text = "Hilfe zu viele Funktionen"
#    test_number_of_words = get_number_of_words(test_text)
#    low_test = make_lowercase(test_text)
#    return print(test_number_of_words, low_test)




def get_text(path):
    with open(path) as f:
        return f.read()
    

def get_number_of_words(text):
    words = text.split()
    return len(words)
 

def count_characters(text):
    lowercase_text = text.lower()
    character_dict = {}
    for character in lowercase_text:
        if character in character_dict.keys():
            character_dict[character] += 1
        else:
            character_dict[character] = 1
    return character_dict

def make_alpha(dict):
    for character in list(dict.keys()):
        if character.isalpha() == False:
            del dict[character]
    return dict    

def make_list_of_dict(dict):
    list = []
    for key in dict:
        list.append({key:dict[key]})
    return list

def make_values_to_keys(dict):
    list = []
    for key in dict:
        list.append({"letter":key , "num": dict[key]})
    return list
    
def sort_on(dict):
    return dict["num"]



main()
#test_main()

