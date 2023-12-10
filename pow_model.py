import csv
import os
import json
from keras.preprocessing.text import Tokenizer
import numpy as np
import pandas as pd

#TODO:
# - Create a csv file that shows which recommendation goes to which

# A list of both the PVAS file and Reddit file.
pvas = []
with open('Senior-Project-F23\PVAS Abridged.csv', newline=None, encoding='utf-8-sig') as line:
  reader = csv.reader(line)
  pvas.extend(reader)

reddit = []
with open('Senior-Project-F23\RedditDataFormatted2.csv', newline=None, encoding='utf-8-sig') as line:
  reader = csv.reader(line)
  reddit.extend(reader)

pvas.pop(0)
reddit.pop(0)

# Combine both files for processing
combined = pvas + reddit

# Tokenize the combined file to give us the matrix
tokenize = Tokenizer(filters='!"#$%&()*+,-/:;<=>?@[\\]^_`{|}~\t\n', lower=True)
tokenize.fit_on_texts(combined)

print(f'Vocabulary: {list(tokenize.word_index.keys())}')

vectors = tokenize.texts_to_matrix(combined, mode='count')

convert = vectors.tolist()
convert = [row[1:] for row in convert]

# Separate the two matrices (PVAS and Reddit data) for cosine similarity
PVASMatrix = convert[:88]
RedditMatrix = convert[88:]

recommendation, cosineSim, bestMatch = [], [], []

# Cosine Distance and Cosine Similarity
for i, redLine in enumerate(RedditMatrix):
  print(f"Recommendation on: {reddit[i]}")
  biggestRec, biggestRecIndex = -1, -1

  for j, PVASLine in enumerate(PVASMatrix):
    # Find Cosine Similiarity
    cosOut = np.dot(redLine, PVASLine) / (np.linalg.norm(redLine) * np.linalg.norm(PVASLine))
    if biggestRec < cosOut:
      biggestRec = cosOut
      biggestRecIndex = j

  print(f"Cosine Similarity: {biggestRec} \nBest Recommendation: {pvas[biggestRecIndex]} \n")

  recommendation.append(reddit[i])
  cosineSim.append(biggestRec)
  bestMatch.append(pvas[biggestRecIndex])

df = pd.DataFrame(data={"Recommendation: ": recommendation, "Similiarty Cosine: ": cosineSim, "Best Match: ": bestMatch})
df.to_csv("recommendationOutput.csv", sep=',', index=False)