def invert(dictionary: dict):
    inverted_dict = {}
    for key, value in dictionary.items():
        inverted_dict[value] = key
    dictionary.clear()
    dictionary.update(inverted_dict)
