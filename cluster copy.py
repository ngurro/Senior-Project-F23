import csv
import os
import openai
import json
import pandas as pd
import time
from dotenv import load_dotenv

load_dotenv()

# Make sure you create and .env file in the same directory and place your APIKey from the OpenAi website in it using
# OPENAI as the variable. (Ex: OPENAI=yourKeyHere)
openai.api_key = os.getenv("OPENAI")

pvas = []
with open('Senior-Project-F23\RedditDataFormatted.csv', newline=None, encoding='utf-8-sig') as line:
  reader = csv.reader(line)
  pvas.extend(reader)

pvas.pop(0)
print(pvas)
output = []

# Initial Input
for i, line in enumerate(pvas):
  lineString = ", ".join(line)
  print(lineString)
  print(f"Your are in iteration {i}")
  time.sleep(2)
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {
        "role": "system",
        "content": "You are a help assistant. Your job is to go through a given list of adopters and create clusters based on the list that is given to you. You will create multiple clusters based on 3 different parameters for each adopter that follows these groups. Category Breed with Clusters of different dog breeds. Category: size with cluster of sizes from small to big. Category Temperment with the following temperment clusters (Calm/Tranquil/Intellegent), (Calm/Easygoing/Submissive), (Spirited/Energetic), (Friendly/Loving/Sweet/Endearing/Friendly/Charming/Social), (Affectionate/Mellow). For adopters that have N/A in the each category for that category put them in an N/A cluster and in categories that hve info put them in their respected cluster. Use the ID to identify and place them in their cluster. If an adopter looks as though they may fit into multiple clusters in any category, put them in each and mark them with (). The only exception to this is if they fit into N/A they should only be in that cluster the respective category."
      },
      {
        "role": "user",
        "content": "Example:\n7    Poodle mix (low-shedding)    small    Intelligent, eager-to-please    Cuddly, friendly\n8    N/A    N/A    N/A    affectionate\n9    N/A    small    Social    intelligent, affectionate\n11    Golden Doodle or Australian Golden Doodle    Small/Medium    Friendly and good with people and kids    Somewhat trainable, attentive"
      },
      {
        "role": "assistant",
        "content": "Category: Breed\n    Cluster: Shepherd\n\n\n  Cluster: Doodle\n11\nCluster: Poodle\n7\nCluster: N/A\n8\n9\nCategory: Size\n    Cluster: Big\n\n\n  Cluster: Medium \n11\n\n\n\n  Cluster: Small\n7\n9\n11*\nCluster: N/A\n8\nCategory: Temperment\n    Cluster: Calm/Tranquil/Intellegent\n\n7*\n9*\n11*\nCluster: Calm/Easygoing/Submissive\n\nCluster: Spirited/Energetic\nCluster: Friendly/Loving/Sweet/Endearing/Friendly/Charming/Social\n7*\n9*\n11*\nCluster: Affectionate/Mellow\n7*\n8\n9*\nCluster: N/A-"
      },
      {       
        "role": "user", "content": lineString
      }
    ],
    temperature=0.5,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )
  gptResponse = response["choices"][0]["message"]["content"]
  output.append(gptResponse)

print(output)

with open("textOutput.txt", "w") as txtF:
  for i in output:
    txtF.write(i)

""" 
dictOutput = []
print(output)
for i in output:
  try:
    res = json.loads(i)
    dictOutput.append(res)
  except json.decoder.JSONDecodeError:
    print(f"Something messed up. Here's the line error: {i}")

df = pd.DataFrame(dictOutput)
df.to_csv('testOutput.csv') 
"""