import gi
gi.require_version('Gtk', '3.0') 
from gi.repository import Gtk

import os
import vlc

class Player:
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("player.ui")
        handlers = {
                "last_song_button_clicked": lambda x: self.last_song_button_clicked(),
                "play_button_clicked": lambda x: self.play_button_clicked(),
                "next_song_button_clicked": lambda x: self.next_song_button_clicked()
                }
        self.builder.connect_signals(handlers)

        self.title = "Player!"

        self.playlist_directory = os.path.expanduser("~/Music/DoctorWho/TheFearmonger/")
        self.player = self.fill_playlist()

        self.win = self.builder.get_object("dialog1")
        self.win.connect('destroy', lambda w: Gtk.main_quit())
        self.win.show_all()

    ###### ACTIONS
    def fill_playlist(self):
        # TODO - use vlc.MediaList.add_media([])
        # MediaList.event_manager()?
        # MediaListPlayer!!!!!!!!

        #for each mp3 file in directory, 
        #   create vlc.Media and add to queue
        print(self.playlist_directory)
        songs = []
        for roots, dirs, files in os.walk(self.playlist_directory):
            print(roots)
            for f in files:
                if f.endswith("mp3"):
                    filepath = os.path.join("file://", self.playlist_directory, f)
                    print(filepath)
                    songs.append(filepath)

        playlist = vlc.MediaList()
        print(sorted(songs))
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
