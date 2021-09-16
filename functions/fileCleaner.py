import os
import glob

def cleanMusics():
    folder = '/mnt/f/Programming/botDiscord/newGroovy/songs/'
    files = os.listdir(folder)
    for f in files:
        print(f)
        os.remove(folder + "/" + f)