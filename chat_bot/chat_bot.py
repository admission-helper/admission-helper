from my_lib import *

from model import create_model
from chat_bot.correct import correct_msg

words = []
classes = []
documents = []
ignore_words = stopwords.words("russian")

with open("data/intents.json", "r", encoding="utf-8") as data_file:
    intents = json.load(data_file)

lemmatizer = WordNetLemmatizer()

for intent in intents['intents']:
    for pattern in intent['patterns']:

        w = nltk.word_tokenize(pattern)
        words.extend(w)
        # adding documents
        documents.append((w, intent['tag']))

        # adding classes to our class list
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_words]

words = sorted(list(set(words)))
classes = sorted(list(set(classes)))

pickle.dump(words,open('model/words.pkl', 'wb'))
pickle.dump(classes,open('model/classes.pkl', 'wb'))

# training data
training = []
output_empty = [0] * len(classes)
for doc in documents:
    # bag of words
    bag = []
    # list of tokenized words for the pattern
    pattern_words = doc[0]
    # lemmatize each word - create base word, in attempt to represent related words
    pattern_words = [lemmatizer.lemmatize(word.lower()) for word in pattern_words]
    # create our bag of words array with 1, if word match found in current pattern
    for w in words:
        bag.append(1) if w in pattern_words else bag.append(0)

    # output is a '0' for each tag and '1' for current tag (for each pattern)
    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1

    training.append([bag, output_row])
# shuffle our features and turn into np.array
random.shuffle(training)
training = np.array(training)
# create train and test lists. X - patterns, Y - intents
train_x = list(training[:,0])
train_y = list(training[:,1])

def get_model():
    name = 'model/chatbot_model.h5'
    if (os.path.exists('./' + name)):
        return load_model(name)
    else:
        return create_model(name, train_x, train_y)

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence

def bow(sentence, words, show_details=True):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bag of words - matrix of N words, vocabulary matrix
    bag = [0] * len(words)
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s:
                # assign 1 if current word is in the vocabulary position
                bag[i] = 1
                # if show_details:
                #     print ("found in bag: %s" % w)
    return(np.array(bag))

def predict_class(sentence, model):
    # filter out predictions below a threshold
    p = bow(sentence, words,show_details=False)
    res = model.predict(np.array([p]))[0]
    error = 0.3
    results = [[i,r] for i, r in enumerate(res) if r > error]

    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list

def get_response(ints, intents_json):
    tag = ints[0]['intent']
    list_of_intents = intents_json['intents']

    for i in list_of_intents:
        if(i['tag']== tag):
            result = ''.join(i['responses'])
            break
    return result

def chatbot_response(msg, model):
    ints = predict_class(msg, model)
    res = get_response(ints, intents)
    return res



# def start(model):
#     while True:
#         msg = input('You: ')
#         msg = correct_msg(msg)

#         if msg.lower() == "выход!":
#             break

#         res = chatbot_response(msg, model)
#         print(res)

def start(msg, model):
    msg = correct_msg(msg)
    res = chatbot_response(msg, model)
    # print(res)
    return res

model = get_model()
# start(model)