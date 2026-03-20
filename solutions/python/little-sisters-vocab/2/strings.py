"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    """Take the given word and add the 'un' prefix.

    :param word: str - containing the root word.
    :return: str - of root word prepended with 'un'.
    """

    return f"un{word}"


def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words into a string with the prefix followed by the words with prefix prepended.

    :param vocab_words: list - of vocabulary words with prefix in first index.
    :return: str - of prefix followed by vocabulary words with
            prefix applied.

    This function takes a `vocab_words` list and returns a string
    with the prefix and the words with prefix applied, separated
     by ' :: '.

    For example: list('en', 'close', 'joy', 'lighten'),
    produces the following string: 'en :: enclose :: enjoy :: enlighten'.
    """

    prefix = vocab_words[0]
    # 把剩下的單字每個都加上 prefix，變成 ['enclose', 'enjoy']
    applied_words = [prefix + word for word in vocab_words[1:]]

    # 把原本的 prefix 放回最前面，變成 ['en', 'enclose', 'enjoy']
    # 然後用 ' :: ' 把它們全部串起來
    return " :: ".join([prefix] + applied_words)


def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.

    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.

    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """

    new_word = word[:-4]

    if new_word.endswith("i"):
        return new_word[:-1] + "y"
    return new_word
def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    For example, ("It got dark as the sun set.", 2) becomes "darken".
    """

    words = sentence.split()  #把句子分开
    target_word = words[index].strip(".") #找出形容词位置，把.去除

    return target_word + "en" #在词后加 en
