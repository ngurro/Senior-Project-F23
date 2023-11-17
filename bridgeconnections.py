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
with open('Senior-Project-F23\Report for school.csv', newline=None, encoding='utf-8-sig') as line:
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
        "content": "Analyze the given string for pet information.\nFormat the output to a dictionary.\nI want to have three keys named, 'Size', 'Temperament', and 'Personality'.\nThe values of these keys should be based on the content of the string given. If the info provided is not sufficient, take a close estimate based on the breed and size of the dog. Otherwise, put 'N/A' instead. Only output in this format.",
      },
      {
        "role": "user",
        "content": "11/16/2019	PVAS-A-102283	Madam Camille	Dog	Shepherd, German	Female	7Y/ 10M/ 26D	Brown	Yes		Available Foster",
      },
      {
        "role": "assistant",
        "content": '{"Size": "big", "Temperament": "Energetic", "Personality": "loyal, affectionate"}'
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