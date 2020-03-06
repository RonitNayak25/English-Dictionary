import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(w):
    w = w.lower()
    if w in data.keys():
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did You Mean %s instead?\nEnter Y for Yes or N for No\n" % get_close_matches(w, data.keys())[0])
        if yn == "y" or yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "n" or yn == "N":
            return "The Word Doesn't Exist"
        else:
            return "Could Not Decipher Your Query"
    else:
        return "The Word Doesn't Exist"


word = input("Enter Word: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
