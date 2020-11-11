from pyaspeller import YandexSpeller
from pymorphy2 import MorphAnalyzer


def correct_msg(msg):
    cur_msg = msg
    try:
        speller = YandexSpeller()
        morph = MorphAnalyzer()
        changes = {change['word']: change['s'][0] for change in speller.spell(msg)}
        for word, suggestion in changes.items():
            msg = msg.replace(word, suggestion)
        msg = morph.parse(msg)[0].inflect({'sing', 'nomn'}).word
    except:
        msg = cur_msg

    return msg