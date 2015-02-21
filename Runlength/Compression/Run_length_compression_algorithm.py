__author__ = 'vidit'

def compress(STR):
    """

    :rtype : string
    """
    prev_char=STR[0]
    output=""
    freq =0
    for new_char in STR:
        if(prev_char==new_char) :
            freq = freq +1
        else :
            output += prev_char
            output += str(freq)
            prev_char = new_char
            freq =1

    return output