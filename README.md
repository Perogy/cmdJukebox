#cmdJukebox

This is a very simple command line Jukebox simulator created for educational purposes.

#Usage

put your audio files into the same directory as the application and they will be read in when you start the application.

Valid commands after starting the application:

* left (l): select the next song to the left
* right (r): select the next song to the right
* play (p): play the currently selected song, or add to queue if a song is currently playing
* money (any number): enter any number to add that amount of money to the machine
* Show queue (q): show the queue of songs to be played (includes currently playing song)
* List songs (s): list all the songs available
* Exit (e): exits the application

#Required libraries:

You must have the following python libraries installed in order to run this application

* Mutagen: for reading ID3 data from audio files. Installation: pip install mutagen
* Pygame: for playing audio files. Installation: pip install pygame