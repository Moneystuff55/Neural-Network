import json
from pprint import pprint

data = json.load(open('data.json'))
output = open('input.txt', 'w')
for name, card in data.items():
    out_string = []
    out_string.append(name)
    if('cmc' in card.keys()):
        out_string.append("Converted:" + str(card['cmc']))
    if('manaCost' in card.keys()):
        out_string.append("Cost:" + card['manaCost'])
    if('type' in card.keys()):
        out_string.append("Typing:" + card['type'])
    if('text' in card.keys()):
        out_string.append("Text:" + card['text'])
    if('power' in card.keys()):
        out_string.append("Power:" + card['power'])
    if('toughness' in card.keys()):
        out_string.append("Toughness:" + card['toughness'])
    output.write("::".join(out_string) + ",\n")