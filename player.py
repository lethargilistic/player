import gi
gi.require_version('Gtk', '3.0') 
from gi.repository import Gtk

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

        self.player = vlc.MediaPlayer()
        self.begun = False

        self.playlist_directory = "~/Music/The Fearmonger Audiobook MP3/"
        self.next_tracks = self.fill_playlist(self.playlist_directory)
        self.current_track = None
        self.past_tracks = []

        self.win = self.builder.get_object("dialog1")
        self.win.connect('destroy', lambda w: Gtk.main_quit())
        self.win.show_all()

    ###### ACTIONS
    def fill_playlist(self, directory):
        track1 = vlc.Media(directory + "01 The Fearmonger - Introduction.mp3")
        print(directory + "01 The Fearmonger - Introduction.mp3")
        track2 = vlc.Media(directory + "02 The Fearmonger Part 1 Track 01.mp3")
        return [track1, track2]
        #for each mp3 file in directory, 
        #   create vlc.Media and add to queue

    ###### EVENTS
    def last_song_button_clicked(self):
        pass

    def play_button_clicked(self):
        if not self.player.is_playing(): #Play
            if self.next_tracks and not self.past_tracks:
                self.current_track = self.next_tracks.pop(0)
                self.player.set_media(self.current_track)
                self.player.play()
            else:
                self.player.pause()
        else: #Pause
            self.player.pause()
            self.begun = True
        
        #if self.playlist:
        #    if self.playing: #Pause
        #        p.pause()
        #        self.playing = False
        #    else: #Play
        #        p = vlc.MediaPlayer("file:///:/home/lethargilistic/Music/The Fearmonger Audiobook MP3/01 The Fearmonger - Introduction.mp3")
        #        self.playing = True
        #elif not self.playlist_directory:
        #    Gtk.MessageDialog(self.win, buttons=Gtk.ButtonsType.OK, message_format="You need to select a folder to play").run()

        #else:
        #    Gtk.MessageDialog(self.win, buttons=Gtk.BUTTONS_OK, message_format="The playlist is over").run()

    def next_song_button_clicked(self):
        pass

    ###### MISC
            
    def main(self):
        Gtk.main()

if __name__ == '__main__':
    app = Player()
    app.main()
