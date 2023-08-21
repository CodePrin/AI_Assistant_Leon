import random
import json
import torch
from Brain import NeuralNet
from NeuralNetworks import bag_of_words, tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open("intents.json", 'r') as json_data:
    intents = json.load(json_data)

FILE = "TrainData.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()


# Code For Leon
Name = "Leon"

from Listen import listen
from Speak import say
from Task import non_input_execution, input_execution

def main():
    sentence = listen()
    result = str(sentence)

    if sentence == "bye":
        exit()

    sentence = tokenize(sentence)
    x = bag_of_words(sentence, all_words)
    x = x.reshape(1, x.shape[0])
    x = torch.from_numpy(x).to(device)
    output = model(x)

    _, predicted = torch.max(output, dim = 1)
    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim = 1)
    prob = probs[0][predicted.item()]

    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                reply = random.choice(intent["responses"])

                if "time" in reply:
                    non_input_execution(reply)
                elif "date" in reply:
                    non_input_execution(reply)
                elif "day" in reply:
                    non_input_execution(reply)
                elif "wikipedia" in reply:
                    input_execution(reply, result)
                elif "google" in reply:
                    input_execution(reply, result)
                else:
                    say(reply)

while True:
    main()

