directions = {'north', 'south', 'east', 'west', 'down', 'up', 'left', 'right',
        'back'}

verbs = {'go', 'stop', 'kill', 'eat'}

stops = {'the', 'in', 'of', 'from', 'at', 'it'}

nouns = {'door', 'bear', 'princess', 'cabinet'}

def scan(phrase):
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
        else:
            try:
                num = int(word)
                ret_words.append(('number', num))
            except ValueError:
                ret_words.append(('error', word))

    return ret_words
