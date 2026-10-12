from lib.music_tracker import *

def test_music_tracker_initial_empty_list():
    music_tracker = MusicTracker()
    assert music_tracker.listOfSongs == []

def test_music_tracker_added_one_song():
    music_tracker = MusicTracker()
    music_tracker.track("Toxic")
    assert music_tracker.listOfSongs == ["Toxic"]

def test_music_tracker_if_multiple_songs_added():
    music_tracker = MusicTracker()
    music_tracker.track("Toxic")
    music_tracker.track("Let it go")
    assert music_tracker.listOfSongs == ["Toxic", "Let it go"]
    # musictracker.list_songs() # > returns a list with toxic and let it go inside.