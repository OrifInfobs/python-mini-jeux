"""
Check letters for the random words game (Mots Aléatoires).
"""


def check_letters(word, secret_word):
    """
    Check each letter in the guessed word against the secret word.
    Args:
        word (str): The guessed word.
        secret_word (str): The secret word to guess.
    Returns:
        str: A string of symbols indicating correctness for each letter.
    """
    secret_counter = {
        char: secret_word.count(char) for char in set(secret_word)
    }
    seen_counter = {char: 0 for char in set(secret_word)}
    result = []
    for i in range(len(word)):
        char = word[i]
        if i < len(secret_word) and char == secret_word[i]:
            result.append("✔")
            if char in seen_counter:
                seen_counter[char] += 1
        elif (
            char in secret_word and
            seen_counter.get(char, 0) < secret_counter.get(char, 0)
        ):
            if word.count(char) <= secret_counter.get(char, 0):
                result.append("➕")
                if char in seen_counter:
                    seen_counter[char] += 1
            else:
                result.append("➖")
        else:
            result.append("❌")
    return "".join(result)
