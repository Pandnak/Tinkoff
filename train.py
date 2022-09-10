# train.py

import numpy as np
import re
import pickle 
import argparse

parser = argparse.ArgumentParser(description = 'Text for training model')
parser.add_argument('text', type=str, help='Path to train text')
parser.add_argument('model', type=str, help='Path to model')
args = parser.parse_args()


with open(args.text, 'r') as file:
    content = file.read()
#print(content)

content = content.lower()
#re.split('\n/, ./!/?/-',content)
reg = re.compile('[^a-z \n]')
content = reg.sub('', content)

for word in content.split():
    # do something with word
     print(word)
#with open(args.model, 'rb') as file:
#pickle.dump(content, file)
