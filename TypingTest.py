import time
from PyRTF import *

typed = []
correct, incorrect = 0, 0

for i in typed:
    if typed[i] == wordList[i]:
        correct += 1
    else:
        incorrect += 1

print("You typed " + correct + " words per minute with " + correct/(correct+incorrect) + "% accuracy")
    