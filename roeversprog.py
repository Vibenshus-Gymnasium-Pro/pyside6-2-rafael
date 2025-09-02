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


def oversaet_fra_roeversprog(inputtekst):
    """ This function translates into normal language. """
    outputtekst = ""
    skip = 0

    for i in inputtekst:
        if skip > 0:
            skip -= 1
        else:
            if i.lower() in consonants:
                outputtekst += i
                skip = 2
            else:
                outputtekst += i
    return outputtekst
