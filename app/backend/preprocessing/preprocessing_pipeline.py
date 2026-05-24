from app.backend.preprocessing.cleaning import (
    basic_text_cleaning
)

from app.backend.preprocessing.normalization import (
    normalize_symbols
)

from app.backend.preprocessing.tokenization import (
    tokenize_text
)

from app.backend.preprocessing.stopwords import (
    remove_stopwords
)

from app.backend.preprocessing.lemmatization import (
    lemmatize_tokens
)


def reconstruct_text(tokens):

    """
    Reconstruct processed text.
    """

    return " ".join(tokens)


def preprocess_text(text):

    """
    Complete preprocessing pipeline.
    """

    text = basic_text_cleaning(text)

    text = normalize_symbols(text)

    tokens = tokenize_text(text)

    filtered_tokens = remove_stopwords(
        tokens
    )

    lemmatized_tokens = lemmatize_tokens(
        filtered_tokens
    )

    processed_text = reconstruct_text(
        lemmatized_tokens
    )

    return {

        "tokens":
        tokens,

        "filtered_tokens":
        filtered_tokens,

        "lemmatized_tokens":
        lemmatized_tokens,

        "processed_text":
        processed_text

    }