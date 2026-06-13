from deep_translator import GoogleTranslator


def translate_to_english(text):
    return GoogleTranslator(
        source="auto",
        target="en"
    ).translate(text)


def translate_to_hindi(text):
    return GoogleTranslator(
        source="auto",
        target="hi"
    ).translate(text)


def translate_to_tamil(text):
    return GoogleTranslator(
        source="auto",
        target="ta"
    ).translate(text)