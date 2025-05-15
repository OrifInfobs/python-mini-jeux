import unicodedata

def normalize(input_text):
    return ''.join(
        c for c in unicodedata.normalize('NFD', input_text)
        if unicodedata.category(c) != 'Mn'
    ).lower()