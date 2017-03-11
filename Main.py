import os
from Song import Song
from Jukebox import Jukebox
import mutagen
import pygame
import sys

songList = []
for songFile in os.listdir("."):
    if songFile.endswith(".mp3"):
        f = mutagen.File(songFile)
        title = ''
        artist = ''
        year = 0
        album = ''
        seconds = 0.0
        if 'TIT2' in f.tags:
            title = f.tags['TIT2']
        if 'TPE2' in f.tags:
            artist = f.tags['TPE2']
        if 'TYER' in f.tags:
            year = f.tags['TYER']
        if 'TALB' in f.tags:
            album = f.tags['TALB']
        
        seconds = f.info.length
        
        s = Song(title, artist, year, album, songFile, seconds)
        songList.append(s)

pygame.mixer.init()
jb = Jukebox(songList)
inp = ""

print("Welcome to cmdJukebox by Brad Paugh!")

while (inp != "e"):   
    inp = input("\nCurrent Balance: " + str(jb.getBalance()) \
                + "\nCurrently Playing: " + jb.getCurrentSong() \
                + "\nCurrently Selected: " + jb.getCurrentSelected() \
                + "\nEnter your command: left(l), right(r), play(p), money(any number), show queue(q), list songs(s), exit(e): ")
    
    if (inp == "l"):
        jb.scrollLeft()
        
    if (inp == "r"):
        jb.scrollRight()
        
    if (inp == "p"):
        jb.addSong()
        
    if (inp == "q"):
        jb.showQueue()
        
    if (inp == "s"):
        jb.listSongs()
        
    if inp.isdigit():
        jb.enterMoney(int(inp))