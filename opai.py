import csv
from dotenv import load_dotenv
import os
import openai

load_dotenv()

# ISSUES:
# Currently, the output is not returning the desire format...


# Make sure you create and .env file in the same directory and place your APIKey from the OpenAi website in it using
# OPENAI as the variable. (Ex: OPENAI=yourKeyHere)
openai.api_key = os.getenv("OPENAI")

csv_reddit = []
with open('testshort.csv', newline='', encoding='utf-8') as line:
  reader = csv.reader(line)
  for row in reader:
    csv_reddit.extend(row)

output = []

print(len(csv_reddit))
# Initial Input
for i in range(len(csv_reddit)):
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {
        "role": "system",
        "content": "Analyze the given csv file for pet adoption preferences.\nFor each row, format the output to a csv table using a comma as the delimiter.\nI want to have five columns named, 'Breed', 'Size', 'Temperament', 'Personality', and 'Other Characteristics'.\nThe rows afterward should be based on the input columns provided. If a cell is empty, put 'N/A' instead.\n\nOutput only the resulting csv table.",
      },
      {
        "role": "user",
        "content": "Here is a sample input from the csv file: \"Introduction\n\nHello all!! We are a family that has always had dogs. We have always had big rescues and we enjoyed putting in the work. But, we have made some lifestyle changes and we are now looking for a 'lower maintenance\"\" apartment dog that will be part of the family (with boundaries, ofc). We have no experience with small dogs and are looking for advice.   \n1) Will this be your first dog? If not, what experience do you have owning/training dogs?  \nNo. We have had 3 rescues over the past 20 years. All were lovely, beautiful dogs. One was very easy and relaxed, one was super anxious, and one was very aggressive and required A LOT of work (2 years of intense training with a specialist). We loved them all, but they have all passed now. We both also grew up with dogs.   \n2) Do you have a preference for rescuing a dog vs. going through a reputable breeder?  \nMy preference is always to rescue. Unfortunately, our new circumstances may dictate that we find a reputable breeder.  \n3) Describe your ideal dog.  \nWe have always had large dogs that had access to hiking with us and roaming free on our large property. Unfortunately we have moved to the United Arab Emirates and live in a condo. The kind of dogs we have had before would no longer be suitable to this lifestyle.\n\nSo, we need a dog who:\n\n\\-can be happy in an apartment (with LOTS of attention)\n\n\\-can get by with minimal exercise when it's 45 degrees C (113 F) \n\n\\-is social with people and other dogs \n\n\\-affectionate (need the snuggles)\n\n\\-intelligent \n\n\\-not barky\n\n\\-easygoing \n\n4) What breeds or types of dogs are you interested in and why?\n\nWe have very open to any breed. For once, non shedding would be nice, but not a requirement. We've had Shepherds and Goldens... hair doesn't scare us!\n\n5) What sorts of things would you like to train your dog to do?\n\nJust basic stuff. We definitely will have a well trained dog. We did high level agility with one of our dogs and that was fun, but we aren't looking to do anything like that again.\n\n6) Do you want to compete with your dog in a sport (e.g. agility, obedience, rally) or use your dog for a form of work (e.g. hunting, herding, livestock guarding)? If so, how much experience do you have with this work/sport?\n\nNo.  \nCare Commitments  \n7) How long do you want to devote to training, playing with, or otherwise interacting with your dog each day?  \nAs much as needed. Especially at the puppy phase. The dog will receive several hours a day of attention, but must be ok to be left for a few hours if we go out for dinner or something.   \n8) How long can you exercise your dog each day, on average? What sorts of exercise are you planning to give your dog regularly and does that include using a dog park?  \nWe are looking for a lower energy dog who is happy with an hour or less of outdoor exercise. It gets VERY hot where we live- too hot to go out sometimes. Happy to take it to the dog park if that is something it enjoys. Walks on the beach (when the sand won't burn), neighbourhood walks etc.  \n9) How much regular brushing are you willing to do? Are you open to trimming hair, cleaning ears, or doing other grooming at home? If not, would you be willing to pay a professional to do it regularly?  \nWe have always had shedding dogs who we brushed regularly. We are willing to take the dog to the groomer, if needed.   \nPersonal Preferences  \n10) What size dog are you looking for?  \nSmall  \n11) How much shedding, barking, and slobber can you handle?  \nâ€¢ Some shedding is ok.  \nâ€¢ No barking beyond \"\"hello\"\" barks for visitors  \nâ€¢ No slobber.  \n12) How important is being able to let your dog off-leash in an unfenced area?  \nNot really. It would be nice, but not requied.  \nDog Personality and Behavior  \n13) Do you want a snuggly dog or one that prefers some personal space?  \nDefinitely a snuggler! But also one that can handle being on it's own. Separation anxiety or clingyness will be a problem.   \n14) Would you prefer a dog that wants to do its own thing or one thatâ€™s more eager-to-please?  \nEager to please  \n15) How would you prefer your dog to respond to someone knocking on the door or entering your yard? How would you prefer your dog to greet strangers or visitors?  \nA couple \"\"hello\"\" barks until I say \"\"enough\"\" is ok. Friendly and welcoming. No guard dog required.  \n16) Are you willing to manage a dog that is aggressive to other dogs?  \nNo. I have been there done that and I loved that dog!! But, I would like a social dog at this point.   \n17) Are there any other behaviors you canâ€™t deal with or want to avoid?  \nNo aggression  \nNot a lot of barking  \nHas to be good with kids- mine are grown, but I have friends with littles.  \nLifestyle  \n18) How often and how long will the dog be left alone?  \nMostly only a couple hours here and there. As they get older, there could be times we need to go out for the day, but we would make sure they were ready for it.  \n19) What are the dog-related preferences of other people in the house and what will be their involvement in caring for the dog?  \nMy husband and I will be the primary care givers for the dog and equally involved. My children are older and love dogs! They will certainly interact and help out, but not be responsible for anything. My daughter would die for a Pomeranian and my son seems to think a Dachshund is the way to go. But, ultimately, we have no preference as long as we are a good fit for the dog.   \n20) Do you have other pets or are you planning on having other pets? What breed or type of animal are they?  \nNo  \n21) Will the dog be interacting with children regularly?  \nTeenagers mostly. But, I do have friends with younger children who come over occasionally.   \n22) Do you rent or plan to rent in the future? If applicable, what breed or weight restrictions are on your current lease?  \nUnder 25 lbs. Ideally, we would like to travel with our dog, so if it fits in a carry on case, even better.  ",
      },
      {
        "role": "assistant",
        "content": "Breed,Size,Temperament,Personality,Other Characteristics\nN/A,small,social,affectionate,intelligent,not barky,easygoing"
      },
      {       
        "role": "user", "content": csv_reddit[i]
      }
    ],
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )
  gptResponse = response["choices"][0]["message"]["content"]
  output.append(gptResponse)

with open('testOutput.csv', 'w') as out:
  for row in range(len(output)):
    out.write(f"{output}\n")

print(len(output))