import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download("stopwords")

from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

import json
import pickle

import numpy as np
import random

from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD