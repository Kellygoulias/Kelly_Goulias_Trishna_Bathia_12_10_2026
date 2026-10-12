
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
        if len(song) == 0:
            raise Exception("No song given")
        elif type(song) != str:
            raise Exception("Incorrect type given")
        elif song not in self.listOfSongs:
            self.listOfSongs.append(song)
        

    def list_songs(self):
        # Returns:
        #   A list reminding the user in order of their songs.
        # Side-effects:
        return self.listOfSongs