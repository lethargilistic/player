Player
------

Player is a basic media player for MP3 and FLAC files, written in Python3. It's intended for use
playing Big Finish audio dramas. As such, the files are stored in one directory
and are played to completion in numeric order. You can skip to the next track or
skip back to the last track. If displays the name of the track, and perhaps the
cover, from the metadata.

It is crossplatform, created with Python and GTK. The developer currently only
has a Linux machine, so people willing to confirm its function on Windows and
Mac would be appreciated.

Installation
------------
"""shell
git clone https://github.com/lethargilistic/player.git
python3 player.py
"""


TODO
----

( ) Set a custom directory to use as a playlist
( ) Play/Pause, then restart with another press of the play/pause button after finish
( ) Skip to next track
( ) Skip to last track
( ) Show cover from metadata
