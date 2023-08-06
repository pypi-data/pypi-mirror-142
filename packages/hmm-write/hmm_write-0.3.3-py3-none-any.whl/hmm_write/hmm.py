import random
import requests
import math
import string

def rm_punctuation(x):
    return [i.translate(str.maketrans('', '', string.punctuation)).lower() for i in x.split()]

def write(prompt, length, bias = 0, training_data = "https://raw.githubusercontent.com/TobyCK/markov-chain-training/main/Training/mywriting.txt"):
    if 0 <= bias <= 1:
        training_data = requests.get(training_data).text.split(" ")
        nouns = requests.get("https://raw.githubusercontent.com/TobyCK/markov-chain/master/Training/nouns.txt").text.split("\n")
        final = prompt
        options_length = 0
        last_word = final.split()[-1]
        if last_word in training_data:
            for i in range(length):
                last_word = final.split()[-1]
                options = []
                for j in training_data:
                    if j == last_word:
                        options_length += 1
                for k in range(len(training_data)):
                    if training_data[k] == last_word:
                        next_word = "".join(rm_punctuation(training_data[k+1]))
                        if next_word in rm_punctuation(prompt) and next_word in nouns:
                            print(next_word)
                            print(rm_punctuation(prompt))
                            if bias > 0:
                                for l in range(math.ceil(options_length * bias)):
                                    options.append(training_data[k + 1 % len(training_data)])
                        else:
                            options.append(training_data[k + 1 % len(training_data)])
                final += " " + random.choice(options)
        else:
            print(f"Sorry, I don't know the word '{last_word}'.")
        return final
    else:
        print("Bias must be between 0 and 1.")
        return None