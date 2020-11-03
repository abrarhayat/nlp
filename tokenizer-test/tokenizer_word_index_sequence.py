from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer

from utils import printSeq

sentences = [
    'i love my dog',
    'I, love my cat',
    'You love my dog!'
]

tokenizer = Tokenizer(num_words = 100, oov_token="<UnknownWord>")
tokenizer.fit_on_texts(sentences)
word_index = tokenizer.word_index


sequences = tokenizer.texts_to_sequences(sentences)
print(word_index, sequences)
print('\n Sequences:')
print(sequences)
printSeq(sequences, word_index)

print('\n Padded Sequences:')
paddedSeq = pad_sequences(sequences, maxlen=10, padding='post', truncating='post')
print(paddedSeq)

test_data = [
             'My cat loves mice', 
             'I think I am a good cat',
             'Do you think my dog is amazing?',
             'Do you think my dog is amazing? Huh, Really, really, really?'
]

test_sequences = tokenizer.texts_to_sequences(test_data)
print('\nTest Sequences:')
print(test_sequences)
printSeq(test_sequences, word_index)

print('\nPadded Test Sequences:')
paddedTestSeq = pad_sequences(test_sequences, maxlen=10, padding='post', truncating='post')
print(paddedTestSeq)
printSeq(paddedTestSeq, word_index)
