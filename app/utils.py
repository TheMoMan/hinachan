import os
import random

def pickRandomFile(directory: str):
    dir = 'lib/{}/'.format(directory)

    files = ([name for name in os.listdir(dir)])
    return dir + random.choice(files)
