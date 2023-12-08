import csv
import os
import json
from keras.preprocessing.text import Tokenizer
import numpy as np
import torch


# A list of both the PVAS file and Reddit file
pvas = []
with open('Senior-Project-F23\PVAS Abridged.csv', newline=None, encoding='utf-8-sig') as line:
  reader = csv.reader(line)
  pvas.extend(reader)

reddit = []
with open('Senior-Project-F23\RedditDataFormatted2.csv', newline=None, encoding='utf-8-sig') as line:
  reader = csv.reader(line)
  reddit.extend(reader)

PVAStokenize = Tokenizer()
PVAStokenize.fit_on_texts(pvas)

redditTokenize = Tokenizer()
redditTokenize.fit_on_texts(reddit)

print(f'Vocabulary: {list(PVAStokenize.word_index.keys())}')
print(f'Vocabulary: {list(redditTokenize.word_index.keys())}')


PVASVectors = PVAStokenize.texts_to_matrix(pvas, mode='count')
print(f"PVAS: {PVASVectors}")

redditVectors = redditTokenize.texts_to_matrix(reddit, mode='count')
print(f"Reddit: {redditVectors}")

# Cosine Distance and Cosine Similarity

cos = torch.nn.CosineSimilarity(dim=0)
cosOut = cos(torch.from_numpy(PVASVectors), torch.from_numpy(redditVectors))
print(f"Cosine Simlilarity: {cosOut} \n Cosine Distance: {1-cosOut}")

""" cos_before_norm = np.dot(PVASVectors, redditVectors) / (np.linalg.norm(PVASVectors)*np.linalg.norm(redditVectors))
print(f'Cosine similarity before normalisation is {cos_before_norm}')
normalized_PVAS = PVASVectors / np.linalg.norm(PVASVectors)
normalized_reddit = redditVectors / np.linalg.norm(redditVectors)

cos_after_norm = np.dot(normalized_PVAS, normalized_reddit) / (np.linalg.norm(normalized_PVAS)*np.linalg.norm(normalized_reddit))
print(f'Cosine similarity after normalisation with length is {cos_after_norm}') """