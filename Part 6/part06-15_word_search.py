import re

def find_words(search_term: str) -> list:
    # Load the file containing words (assuming it's named "words.txt")
    with open("words.txt", "r") as file:
        words = file.read().split()

    # If there are no wildcard characters
    if '.' not in search_term and '*' not in search_term:
        return [word for word in words if word == search_term]

    # If there is an asterisk at the end of the search term
    if search_term.endswith('*'):
        prefix = search_term[:-1]
        return [word for word in words if word.startswith(prefix)]

    # If there is an asterisk at the beginning of the search term
    if search_term.startswith('*'):
        suffix = search_term[1:]
        return [word for word in words if word.endswith(suffix)]

    # If there is a dot in the search term
    if '.' in search_term:
        regex_pattern = "^" + search_term.replace(".", ".") + "$"
        return [word for word in words if re.match(regex_pattern, word)]

    # If there is an asterisk in the middle of the search term
    parts = search_term.split("*")
    prefix = parts[0]
    suffix = parts[1]
    regex_pattern = "^" + prefix + ".*" + suffix + "$"
    return [word for word in words if re.match(regex_pattern, word)]
