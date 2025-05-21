def check_letters(word, secret_word):                # Function to check letters in the word 
    secret_counter = {char: secret_word.count(char) for char in set(secret_word)}
    seen_counter = {char: 0 for char in set(secret_word)}
    result = []
    for i in range(len(word)):
        if word[i] == secret_word[i]:                # Correct letter and position
            result.append("✔")
            seen_counter[word[i]] += 1
        elif word[i] in secret_word and seen_counter[word[i]] < secret_counter[word[i]]: # Correct letter but wrong position
            if word.count(word[i]) <= secret_counter[word[i]]:                           # Check if the letter has already been counted
                result.append("➕")
                seen_counter[word[i]] += 1
            else:                                   # All occurrences already accounted for
                result.append("➖") 
        else:
            result.append("❌")                    # Letter not in the word
    return "".join(result)