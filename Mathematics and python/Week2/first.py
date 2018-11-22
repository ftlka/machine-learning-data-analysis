import numpy as np
from scipy.spatial.distance import cosine
import re

lines = open('sentences.txt', 'r').read().lower().split('\n')
number_of_lines = len([line for line in lines if line != ''])

tokens = re.split('[^a-z]', ' '.join(lines))
tokens = [token for token in tokens if token != '']

d = {}
for idx, token in enumerate(set(tokens)):
    d[idx] = token

matrix = np.zeros((number_of_lines, len(d)))
for i in range(number_of_lines):
    for j in range(len(d)):
        current_word = d[j]
        count = sum(1 for match in re.finditer(r'\b%s\b' % re.escape(current_word), lines[i]))
        matrix[i, j] = count

for i in range(1, number_of_lines):
    print(i, cosine(matrix[0], matrix[i]))
