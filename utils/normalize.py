import unicodedata

def normalize(input_text):
    return ''.join(                                         # Remove accents and capital letters
        c for c in unicodedata.normalize('NFD', input_text) # Normalize to NFD form to accent characters
        if unicodedata.category(c) != 'Mn'                  # Remove diacritical marks
    ).lower()