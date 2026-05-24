from nltk.stem import WordNetLemmatizer


# Initialize lemmatizer

lemmatizer = WordNetLemmatizer()


def lemmatize_tokens(tokens):

    """
    Apply lemmatization.
    """

    return [

        lemmatizer.lemmatize(token)

        for token in tokens

    ]