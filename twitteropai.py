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

csv_reddit = []
with open('Senior-Project-F23/Altered-Twitter-Data.csv', newline=None, encoding='utf-8-sig') as line:
  reader = csv.reader(line)
  csv_reddit.extend(reader)

print(csv_reddit)
output = []

# Initial Input
for i, line in enumerate(csv_reddit):
  print(f"Your are in iteration {i}")
  time.sleep(2)
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {
        "role": "system",
        "content": "Analyze the given string for pet information.\nFormat the output to a dictionary.\nI want to have five keys named, 'Breed', 'Size', 'Temperament', and 'Personality'.\nThe values of these keys should be based on the content of the string given. If the info provided cannot be put into any category, try a guess based on what you've read. Otherwise, put 'N/A' instead. Only output in this format.",
      },
      {
        "role": "user",
        "content": "A POUND FAVORITE, 13yo Ramsey 171067 has waited so long for his chance, now TBK in NYCACC Saturday. Friendly, affectionate and lovable, he allows all handling and was relaxed and playful with the child he lived with. Everybody loves Ramsey, heâ€™s adoptable from any location and is suited as a solo dog in a family with age 13+ kids. Please pledge RT!",
      },
      {
        "role": "assistant",
        "content": '{"Breed": "N/A", "Size": "small", "Temperament": "Social", "Personality": "intelligent, affectionate"}'
      },
      {       
        "role": "user", "content": line[0] + " " + line[1]
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