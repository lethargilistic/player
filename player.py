import gi
gi.require_version('Gtk', '3.0') 
from gi.repository import Gtk

import os
import vlc

class Player:
    def __init__(self):
        # Front End
        self.builder = Gtk.Builder()
        self.builder.add_from_file("player.ui")
        
        # Connect handlers
        handlers = {
                "last_song_button_clicked": lambda x: self.last_song_button_clicked(),
                "play_button_clicked": lambda x: self.play_button_clicked(),
                "next_song_button_clicked": lambda x: self.next_song_button_clicked()
                }
        self.builder.connect_signals(handlers)

        #Load player
        self.playlist_directory = os.path.expanduser("~/Music/DoctorWho/TheFearmonger/")
        self.player = self.fill_playlist()

        #Set up window, display
        self.title = "Player!"
        self.win = self.builder.get_object("dialog1")
        self.win.connect('destroy', lambda w: Gtk.main_quit())
        self.win.show_all()

    ###### ACTIONS
    def fill_playlist(self):
        """Returns a vlc.MediaListPlayer with all the mp3 files from the
        self.playlist_directory"""
        songs = []
        for roots, dirs, files in os.walk(self.playlist_directory):
            for f in files:
                if f.endswith("mp3"):
                    filepath = os.path.join("file://", self.playlist_directory, f)
                    songs.append(filepath)

        playlist = vlc.MediaList()
        for song in sorted(songs):
            playlist.add_media(vlc.Media(song)) 
        
        player = vlc.MediaListPlayer()
        player.set_media_list(playlist)
        return player

    ###### EVENTS
    def last_song_button_clicked(self):
        self.player.previous()

    def play_button_clicked(self):
        #TODO: Update for MediaListPlayer
        if self.player.get_state() == vlc.State.Ended: #Play. 
            self.player.play()
        else: #Pause/un-pause
            self.player.pause()
        

    def next_song_button_clicked(self):
        self.player.next()

    ###### MISC
            
    def main(self):
        Gtk.main()

if __name__ == '__main__':
    app = Player()
    app.main()
