def create_dictionary_by_first_char(input_string):
    words = input_string.split()
    result_dict = {}
    for word in words:
        first_char = word[0]

    if first_char in result_dict:
        result_dict[first_char].append(word)
    else:
        result_dict[first_char] = [word]

    return result_dict

# Example usage
input_string = input("Enter a sentence: ")
result = create_dictionary_by_first_char(input_string)
print("Dictionary with words grouped by first character:", result)