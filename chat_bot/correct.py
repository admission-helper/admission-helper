from pyaspeller import YandexSpeller
import pymorphy2

speller = YandexSpeller()
morph = pymorphy2.MorphAnalyzer()

def correct_msg(msg):
    cur_msg = msg
    try:
        changes = {change['word']: change['s'][0] for change in speller.spell(msg)}
        for word, suggestion in changes.items():
            msg = msg.replace(word, suggestion)
        msg = morph.parse(msg)[0].inflect({'sing', 'nomn'}).word
    except:
        msg = cur_msg

    return msg