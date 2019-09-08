import json
from difflib import get_close_matches
data = json.load(open("data.json"))

def dict(word):
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys(),cutoff=0.7)) > 0:
        rec = input("did you mean %s instead? Enter Y or N: " % get_close_matches(word, data.keys())[0])
        if rec == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif rec == "N":
            return "Recheck the word as it does not exists"
        else:
            return "I said Y or N, don't type random shit"
    else:
        return "Recheck the word as it does not exists"


search = input("Enter word: ")
output = dict(search)
if type(output) == list:
    for item in output:
        print("> ", item)
else:
    print(output)