directions = {'north', 'south', 'east', 'west', 'down', 'up', 'left', 'right',
        'back'}

verbs = {'go', 'stop', 'kill', 'eat'}

stops = {'the', 'in', 'of', 'from', 'at', 'it'}

nouns = {'door', 'bear', 'princess', 'cabinet'}

modifiers = {'cool', 'very', 'quickly'}

def scan(phrase):
    if phrase == None:
        raise Exception("don't gimme None!")
    words = phrase.split()
    ret_words = []
    for word in words:
        temp = word.lower()
        if temp in directions:
            ret_words.append(('direction', word))
        elif temp in verbs:
            ret_words.append(('verb', word))
        elif temp in stops:
            ret_words.append(('stop', word))
        elif temp in nouns:
            ret_words.append(('noun', word))
        elif temp in modifiers:
            ret_words.append(('modifier', word))
        else:
            try:
                num = int(word)
                ret_words.append(('number', num))
            except ValueError:
                ret_words.append(('error', word))

    return ret_words
