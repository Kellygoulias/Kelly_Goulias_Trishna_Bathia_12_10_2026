
class MusicTracker:
    # User-facing properties:
    #   name: string

    def __init__(self):
        # Parameters:
        #   no parameters
        # Side effects:
        #   Creates self empty list. 
        self.listOfSongs = []

    def track(self, song):
        # Parameters:
        #   task: string representing a single song
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the song to the self object
        # if song not entered, throws an exception, if song doenst = string, throws an excpetion.
        self.listOfSongs.append(song)

    def list_songs(self):
        # Returns:
        #   A list reminding the user in order of their songs.
        # Side-effects:
        # 
        pass # No code here yet