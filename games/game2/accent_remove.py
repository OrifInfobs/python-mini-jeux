import unicodedata

# List of French words with accents
french_words_with_accents = [
    'abats', 'abcès', 'abîme', 'aboli', 'abord', 'about', 'accès', 'accru', 'acéré', 'achat',
    'acier', 'actif', 'adieu', 'admis', 'adobe', 'adore', 'adret', 'aéré', 'affin', 'affût',
    'âgé', 'agile', 'agir', 'agneau', 'agrafe', 'aide', 'aigle', 'aiguë', 'aimer', 'ainsi',
    'ajout', 'alarme', 'albâtre', 'album', 'alcool', 'alerte', 'algue', 'alias', 'alibi', 'aligné',
    'allée', 'allia', 'allô', 'alors', 'altéré', 'alu', 'amande', 'amène', 'amour', 'ample',
    'ânesse', 'ange', 'angle', 'anime', 'année', 'anode', 'anse', 'antre', 'août', 'appel',
    'appui', 'âpre', 'aptes', 'aquarel', 'arabe', 'arbre', 'arène', 'argile', 'armée', 'armure',
    'arpent', 'arraché', 'arrêt', 'arsène', 'artère', 'asile', 'aspect', 'assaut', 'astre', 'atelier',
    'atlas', 'atoll', 'atome', 'atout', 'attrait', 'auberge', 'aucun', 'audace', 'aune', 'aurai',
    'aurore', 'aussi', 'autel', 'auteur', 'auto', 'autre', 'aval', 'avare', 'avenir', 'avers'
]

# Function to remove accents
def remove_accents(word):
    return ''.join(c for c in unicodedata.normalize('NFD', word) if unicodedata.category(c) != 'Mn')

# Generate list of words without accents
accent_free_words = [remove_accents(word) for word in french_words_with_accents]

# Save to text file
with open("french_words_no_accents.txt", "w", encoding="utf-8") as f:
    for word in accent_free_words:
        f.write(word + "\n")