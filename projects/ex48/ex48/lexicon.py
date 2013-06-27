direction = ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right',
        'back']

verbs = ['go', 'stop', 'kill', 'eat']

stops = ['the', 'in', 'of', 'from', 'at', 'it']

nouns = ['door', 'bear', 'pincess', 'cabinet']

def scan(phrase):
    words = phrase.split()
    ret_words = []
    for word in words:
        ret_words.append(('direction', word))
    return ret_words
