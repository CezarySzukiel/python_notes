def create_sentence(fn, text):
    return fn(text)


def capitalize(text):
    return text.capitalize()


def lower(text):
    return text.lower()


# ala ma kota => "AlA Ma kOtA"

def mocking_caps(text):
    return ''.join(letter.lower() if index % 2 else letter.upper() for index, letter in enumerate(text))


sentence = "ala ma kota"
r1 = create_sentence(capitalize, sentence)
r2 = create_sentence(lower, sentence)
r3 = create_sentence(mocking_caps, sentence)

print(r1, r2, r3, sep='\n')
