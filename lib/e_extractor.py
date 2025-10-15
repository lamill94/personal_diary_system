def e_extractor(string):
    if 'e' in string:
        new_str = ""
        for letter in string:
            if letter == 'e':
                new_str = 'e' + new_str
            else:
                new_str = new_str + letter
        return new_str
    else:
        return string
    
"""
Or could do list comprehensions:

    letter_es = [letter for letter in string if letter == 'e']
    non_letter_es = [letter for letter in string if letter != 'e']
    return "".join(letter_es + non_letter_es)
"""