'''
Player is an MP3 player made with Python and Gtk.
This software is released under the MIT License.
Copyright © 2016 Mike Overby 
'''

import gi
gi.require_version('Gtk', '3.0') 
from gi.repository import Gtk

import glob
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

        #Set up window, display
        self.title = "Player!"
        self.win = self.builder.get_object("dialog1")
        self.win.connect('destroy', lambda w: Gtk.main_quit())
        self.win.set_resizable(False)
        self.win.show_all()

        #Load player
        self.choose_playlist()

    ###### ACTIONS
    def choose_playlist(self):
        #TODO: activate from taskbar
        self.playlist_directory = self.select_directory()
        self.player = self.fill_playlist()
        #TODO: The library seems broken. Awaiting patch.
        #self.event_manager = self.player.event_manager()
        #self.event_manager.event_attach(vlc.EventType.MediaListPlayerNextItemSet,
        #                               self.songchanged(listplayer=self.player))

    def select_directory(self):
        chooser = Gtk.FileChooserDialog("Please select a playlist directory.",
                self.win,
                Gtk.FileChooserAction.SELECT_FOLDER,
                (Gtk.STOCK_CANCEL,
                    Gtk.ResponseType.CANCEL,
                    Gtk.STOCK_OPEN,
                    Gtk.ResponseType.OK))
        chooser.run()
        directory = chooser.get_filename()
        chooser.destroy()
        return directory


    def fill_playlist(self):
        """Returns a vlc.MediaListPlayer with all the mp3 files from the
        self.playlist_directory"""
        playlist = vlc.MediaList()

        songs = glob.glob(os.path.join(self.playlist_directory, "*.mp3"))
        for song in sorted(songs):
            playlist.add_media(vlc.Media(song)) 
        
        player = vlc.MediaListPlayer()
        player.set_media_list(playlist)
        return player

    def fetch_tracknumber(self, media):
        media.parse()
        return int(media.get_meta(vlc.Meta.TrackNumber))

    def fetch_art(self, media):
        media.parse()
        return media.get_meta(vlc.Meta.ArtworkURL)

    def fetch_title(self, media):
        media.parse()
        return media.get_meta(vlc.Meta.Title)

    ###### EVENTS
    def songchanged(self, listplayer):
        #TODO, update picture and text
        media = listplayer.get_media_player().get_media()
        self.builder.get_object("song_name").set_label(self.fetch_title(media))
        print(self.builder.get_object("song_name").props.label)
        print("CHANGE")

    def last_song_button_clicked(self):
        self.player.previous()

    def play_button_clicked(self):
        #TODO: Check if there are songs in the player.
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
