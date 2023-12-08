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
with open('Senior-Project-F23\Altered-PVAS-Data.csv', newline=None, encoding='utf-8-sig') as line:
  reader = csv.reader(line)
  pvas.extend(reader)

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
        "content": "You are a help assistant. Your job is to go through a given list of dogs and create clusters based on the list that is given to you. You will create multiple clusters based on 3 different parameters for eacSh dog. For example, a dog that is a germen sheperd, friendly, and medium sized will be put into 1 cluster for each parameter. For breed he will be placed in a germen sheperd cluster, for size he will be placed in a medium sized cluster, and for temperment he will be placed in a friendly cluster. If temperment is not given determine based of the breed and age of the dog. If the breed is known to be energetic and active like a retriever then put in that cluster. \n"
      },
      {
        "role": "user",
        "content": "Example:\nName    Primary Breed    Size    Temperament\nMadam Camille    Shepherd, German    big    Energetic\nLedger    Retriever    medium    To be determined\nNutmeg    Terrier, Pit Bull    medium    Friendly\nBelle    Shepherd    big    Energetic\nLa Morena    Shepherd, German    big    Energetic\nNara    Boxer    medium    affectionate\nFauna    Shepherd    big    Unknown"
      },
      {
        "role": "assistant",
        "content": "Category: Breed\n    Cluster: Shepherd\n    \nMadam Camille\nBelle\nLa Morena\nFauna\nCluster: Retriever\nLedger\nCluster: Terrier\nNutmeg\nCluster: Boxer\nNara\nCategory: Size\n    Cluster: Big\n    \nMadam Camille\nBelle\nLa Morena\nFauna\nCluster: Medium \nNutmeg\nLedger\nNara\nCategory: Temperment\n    Cluster: Engergetic/Active\n    \nMadam Camille\nBelle\nLa Morena\nNara\nLedger\nCluster: Friendly/Sociable\nNutmeg\nNara\nFauna"
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