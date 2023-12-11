import csv
from keras.preprocessing.text import Tokenizer
import numpy as np
import pandas as pd

# Warning: This is an absolutely atrociously written code.

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

vectors = tokenize.texts_to_matrix(combined, mode='count')

convert = vectors.tolist()
convert = [row[1:] for row in convert]

# Separate the two matrices (PVAS and Reddit data) for cosine similarity
PVASMatrix = convert[:88]
RedditMatrix = convert[88:]

origReddit = []
with open('Senior-Project-F23\\redditanimal.csv', newline=None, encoding='utf-8-sig') as line:
  reader = csv.reader(line)
  origReddit.extend(reader)

origPVAS = []
with open('Senior-Project-F23\Report for school.csv', newline=None, encoding='utf-8-sig') as line:
  reader = csv.reader(line)
  origPVAS.extend(reader)

origReddit.pop(0)

ogRed, ogP, recommendation, cosineSim, bestMatch = [], [], [], [], []

# Cosine Distance and Cosine Similarity
for i, redLine in enumerate(RedditMatrix):
  biggestRec, biggestRecIndex = [-1, -1, -1], [-1, -1, -1]

  for j, PVASLine in enumerate(PVASMatrix):
    # Find Cosine Similiarity
    cosOut = np.dot(redLine, PVASLine) / (np.linalg.norm(redLine) * np.linalg.norm(PVASLine))

    for k in range(3):
      if biggestRec[k] == -1 or biggestRec[k] < cosOut:
        biggestRec.insert(k, cosOut)
        biggestRecIndex.insert(k, j)
        break

    while (len(biggestRec) > 3):
      biggestRec.pop()
      biggestRecIndex.pop()

  recommendation.append(reddit[i])
  cosineSim.append(biggestRec)
  ogRed.append(origReddit[i])

  for x in biggestRecIndex:
    bestMatch.append(pvas[x])
    ogP.append(origPVAS[x])
  
  for y in range(2):
    recommendation.append(" ")
    cosineSim.append(" ")
    ogRed.append(" ")    

a = {"Original Post: ": ogRed, "Data Extracted: ": recommendation, "Similiarty Cosine: ": cosineSim, "Best Match Description: ": bestMatch, "Animal Identity: ": ogP}
df = pd.DataFrame.from_dict(a, orient='index')
df = df.transpose()
df.to_csv("recommendationOutput.csv", sep=',', index=False)