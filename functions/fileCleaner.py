import os
import glob

def cleanMusics():
    folder = 'E:\\ProgrammingVelocity\\barrosSpotifyBot\songs'
    files = os.listdir(folder)
    for f in files:
        print(f)
        os.remove(folder + "/" + f)