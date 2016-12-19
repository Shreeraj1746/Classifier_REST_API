import re

from nltk import pos_tag, corpus


def extract_features(tokens):
    tagged_tokens = pos_tag(tokens)
    feature_list = []

    def shape(word):
        if re.match('[0-9]+(\.[0-9]*)?|[0-9]*\.[0-9]+$', word, re.UNICODE):
            return 'number'
        elif re.match('\W+$', word, re.UNICODE):
            return 'punct'
        elif re.match('\w+$', word, re.UNICODE):
            if word.istitle():
                return 'upcase'
            elif word.islower():
                return 'downcase'
            else:
                return 'mixedcase'
        else:
            return 'other'

    def simplify_pos(s):
        if s.startswith('V'):
            return "V"
        else:
            return s.split('-')[0]

    def _feature_extractor(tokens, index):
        word = tokens[index][0]
        pos = simplify_pos(tokens[index][1])
        english_wordlist = set(w.lower() for w in corpus.words.words())
        if index == 0:
            prevword = None
            prevpos = None
            prevshape = None
            nextword = tokens[index+1][0].lower()
            nextpos = tokens[index+1][1].lower()
        elif index == len(tokens)-1:
            prevword = tokens[index-1][0].lower()
            prevpos = tokens[index-1][1].lower()
            prevshape = shape(prevword)
            nextword = None
            nextpos = None
        else:
            prevword = tokens[index-1][0].lower()
            prevpos = tokens[index-1][1].lower()
            prevshape = shape(prevword)
            nextword = tokens[index+1][0].lower()
            nextpos = tokens[index+1][1].lower()

        # features dictionary
        features = {
            'bias': True,
            'shape': shape(word),
            'wordlen': len(word),
            'prefix3': word[:3].lower(),
            'suffix3': word[-3:].lower(),
            'pos': pos,
            'word': word,
            'en-wordlist': (word in english_wordlist),
            'prevpos': prevpos,
            'nextpos': nextpos,
            'prevword': prevword,
            'nextword': nextword,
            'word+nextpos': '%s+%s' % (word.lower(), nextpos),
            'word+prevpos': '%s+%s' % (word.lower(), prevpos),
            'prevshape': prevshape,
            }

        return features

    for token in tagged_tokens:
        features = _feature_extractor(tagged_tokens, tagged_tokens.index(token))
        feature_list.append(features)

    return feature_list
