# defing a custom function to print the sequence in words rather than the keys
def printSeq(sequences, word_index):
  print("Sequences in words:")
  for seq in sequences:
    sentence = []
    for index in seq:
      for word, word_index_value in word_index.items():
        if index == word_index_value:
          sentence.append(word)
    print(sentence, "length:", len(sentence))