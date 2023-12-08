import csv
import os
import json
from keras.preprocessing.text import Tokenizer
import numpy as np
import torch

#TODO:
# - Fix tokenizer (Should most of the list be 0?)
# - Create the alternate way of calculating Cosine Similarity
# - Finish the recommendation algorithm

# A list of both the PVAS file and Reddit file.
pvas = []
with open('Senior-Project-F23\PVAS Abridged.csv', newline=None, encoding='utf-8-sig') as line:
  reader = csv.reader(line)
  pvas.extend(reader)

reddit = []
with open('Senior-Project-F23\RedditDataFormatted2.csv', newline=None, encoding='utf-8-sig') as line:
  reader = csv.reader(line)
  reddit.extend(reader)

print(pvas)
pvas.pop(0)
reddit.pop(0)

# Combine both files for processing
combined = pvas[0]

tokenize = Tokenizer()
tokenize.fit_on_texts(combined)

print(f'Vocabulary: {list(tokenize.word_index.keys())}')

vectors = tokenize.texts_to_matrix(pvas, mode='count')

convert = vectors.tolist()
# Separate the two matrices (PVAS and Reddit data)
PVASMatrix = convert[:88]
RedditMatrix = convert[88:]
#RedditMatrix = np.split(vectors, vectors[88:])


print(f"PVASMatrix: {PVASMatrix}")


# Cosine Distance and Cosine Similarity
""" cos = torch.nn.CosineSimilarity(dim=0)
cosOut = cos(torch.from_numpy(PVASVectors), torch.from_numpy(redditVectors))
print(f"Cosine Simlilarity: {cosOut} \n Cosine Distance: {1-cosOut}") """