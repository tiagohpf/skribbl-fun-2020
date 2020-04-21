SPECIAL_CHARS = ['.', ';', '-', '/']


class StringParser:

    @staticmethod
    def refactor_sentence(text):
        text = text.strip()

        if text[0] in SPECIAL_CHARS:
            text = text[1:]
        if text[-1] in SPECIAL_CHARS:
            text = text[:-1]

        # Capitalize each word of phrases
        words = text.split(' ')
        if len(words) > 1:
            return ' '.join([word.capitalize() for word in words])
        return words[0].capitalize()