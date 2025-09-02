# Dette er et modul til oversættelse mellem almindelige sprog og røversprog

consonants = "bcdfghjklmnpqrstvwxz"

def oversaet_til_roeversprog(inputtekst):
    """ This function translates from nornal language."""
    outputtekst = ""

    for i in inputtekst:
        if i.lower() not in consonants:
            outputtekst += i
        else:
            outputtekst += f"{i}o{i}"
    return outputtekst


def oversaet_fra_roeversprog_til_andet_sprog(inputtekst):
    outputtekst = "Her skal røversproget fjernes og almindeligt sprog skal returneres.\nGiv gerne fejlmeddelelser, hvis røversproget ikke er korrekt."
    return outputtekst
