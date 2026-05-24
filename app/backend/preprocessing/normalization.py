def normalize_symbols(text):

    text = text.replace(
        "\n",
        " "
    )

    text = text.replace(
        "\t",
        " "
    )

    return text