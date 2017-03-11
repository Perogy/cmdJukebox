import Song
import pygame
import sys
from threading import Thread
from threading import Timer

class Jukebox:
    
    def __init__(self, songList):
        self.songList = songList
        self.songSelectedIndex = 0
        self.moneyEntered = 0.00
        self.songPlayQueue = []
        
    def scrollLeft(self):
        if (self.songSelectedIndex == 0):
            print("Cannot scroll any further left")
        else:
            self.songSelectedIndex = self.songSelectedIndex - 1
            print("You've selected " + str(self.songList[self.songSelectedIndex]))
            
    def scrollRight(self):
        if (self.songSelectedIndex == (len(self.songList) - 1)):
            print("Cannot scroll any further right")
        else:
            self.songSelectedIndex = self.songSelectedIndex + 1
            print("You've selected " + str(self.songList[self.songSelectedIndex]))

    def addSong(self):
        if (self.moneyEntered >= 1.00):
            self.moneyEntered = self.moneyEntered - 1.00
            self.songPlayQueue.append(self.songList[self.songSelectedIndex])
            if (len(self.songPlayQueue) == 1):
                self.playNextSong()
            else:
                print(str(self.songList[self.songSelectedIndex]) + " has been added to the queue in position " + str(len(self.songPlayQueue)))
        else:
            print("not enough money in the machine, sorry!")
            
    def playNextSong(self):
        pygame.mixer.music.load(self.songPlayQueue[0].filename)
        pygame.mixer.music.play()
        self.runSongTimer()
        
        Thread(target=print, args=("\nNow playing: " + str(self.songPlayQueue[0])), kwargs={'flush':True, 'sep':''}).start()
            
    def enterMoney(self, amount):
        self.moneyEntered = self.moneyEntered + amount
    
    def getBalance(self):
        return self.moneyEntered
        
    def getCurrentSong(self):
        if not self.songPlayQueue:
            return "None"
        else:
            return str(self.songPlayQueue[0])
            
    def getCurrentSelected(self):
        return str(self.songList[self.songSelectedIndex])
        
    def showQueue(self):
        i = 0
        for s in self.songPlayQueue:
            i = i + 1
            if (i == 1):
                print("Currently Playing: " + str(s))
            else:
                print(str(i) + ": " + str(s))
            
    def listSongs(self):
        for s in self.songList:
            print(str(s))
            
    def runSongTimer(self):
        t = Timer(self.songPlayQueue[0].seconds, self.songFinished)
        t.daemon = True
        t.start()
        
            
    def songFinished(self):
        self.songPlayQueue.remove(self.songPlayQueue[0])
        if (len(self.songPlayQueue) > 0):
            self.playNextSong()
        