from nltk.corpus import stopwords


# Load stopwords

custom_stopwords = set(
    stopwords.words("english")
)

# Preserve procedural terms

important_terms = {

    "not",
    "no",
    "must",
    "shall",
    "cannot"

}

custom_stopwords = (
    custom_stopwords
    -
    important_terms
)


def remove_stopwords(tokens):

    """
    Remove unnecessary stopwords.
    """

    return [

        token

        for token in tokens

        if token not in custom_stopwords

    ]