import pickle

from nltk.tokenize import WordPunctTokenizer

from features import extract_features


def classify_named_entities(text):
    tokens = WordPunctTokenizer().tokenize(text)
    test_feats = extract_features(tokens)
    me_classifier = pickle.load(open(
        "./classifiers/wiki_gold_me_classifier.p", "rb"))
    predictions = get_entity_classifications(tokens, test_feats, me_classifier)

    return predictions


def get_entity_classifications(tokens, test_feats, sk_classifier):
    pred_list = make_predictions(test_feats, sk_classifier)
    return zip(tokens, pred_list)


def make_predictions(test_feats, sk_classifier):
    pred_list = []
    if type(test_feats[0]) is dict:
        for feats in test_feats:
            pred_list.append(sk_classifier.classify(feats))
    elif type(test_feats[0]) is tuple:
        for feats, label in test_feats:
            pred_list.append(sk_classifier.classify(feats))

    return pred_list
