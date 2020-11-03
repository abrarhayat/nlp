from utils import printSeq
import urllib3, json
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences


url = "https://storage.googleapis.com/laurencemoroney-blog.appspot.com/sarcasm.json"
http = urllib3.PoolManager()
response = http.request('GET', url)
datastore = json.loads(response.data)
#print(datastore)

sentences = []
labels = []
urls = []
for item in datastore:
    sentences.append(item['headline'])
    labels.append(item['is_sarcastic'])
    urls.append(item['article_link'])

tokenizer = Tokenizer(oov_token="<OOV>")
tokenizer.fit_on_texts(sentences)

word_index = tokenizer.word_index
print(len(word_index))
#print(word_index)
sequences = tokenizer.texts_to_sequences(sentences)
padded = pad_sequences(sequences, padding='post')
print(sentences[2])
print(padded[2])
print(padded.shape)
#printSeq(padded, word_index)