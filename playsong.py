import numpy

def play(song):
    if song[len(song)-4:] == ".com":
        return  #search link directly
    else:
        return  #search in youtube search bar and take first link