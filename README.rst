Player
------

Player is a basic media player for MP3 and FLAC files. It's intended for use
playing Big Finish audio dramas. As such, the files are stored in one directory
and are played to completion in numeric order. You can skip to the next track or
skip back to the last track. If displays the name of the track, and perhaps the
cover, from the metadata.

It is crossplatform, created with Python3 and GTK. The developer currently only
has a Linux machine, so people willing to confirm its function on Windows and/or
Mac would be appreciated.

Installation
------------
Player relies on vlc.py_, maintained by the `VideoLAN Organization`_. You need a copy of that file, and you need to install VLC Player for Player to work.

.. _vlc.py: http://git.videolan.org?p=vlc/bindings/python.git;a=tree;f=generated;b=HEAD
.. _VideoLAN Organization: http://www.videolan.org>

.. code:: zsh

    git clone https://github.com/lethargilistic/player.git
    cd player
    sudo apt-get install vlc
    wget -O vlc.py "http://git.videolan.org?p=vlc/bindings/python.git;a=blob_plain;f=generated/vlc.py;hb=HEAD"
    python3 player.py

License
-------
Player, as an application, is released under the MIT License. See LICENSE.txt

Also, vlc.py is released under LGPL 2.1. As such, a copy of those terms is also included.

TODO
----

[x] Set a custom directory to use as a playlist

    [ ] A button or taskbar option for choosing a playlist
    
[x] Play/Pause, then restart with another press of the play/pause button after finish

[x] Skip to next track

[x] Skip to last track

[ ] Show cover/title from metadata
