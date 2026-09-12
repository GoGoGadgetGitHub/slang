meme_dict = {
            "CRINGE": "Something exceptionally weird or embarrassing",
            "LOL": "A common response to something funny ",
            "ROFL": "ROFL is used as a reaction to something funny, similar to LOL"
            }

word = input("Type in a modern word you don't understand (use all capital letters!): ")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("We don't have this word yet... But we're working on it!")
