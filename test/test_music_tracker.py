import pytest
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

def test_list_songs_returns_song():
   
    music_tracker = MusicTracker()
    music_tracker.track("Fireflies")
    music_tracker.track("Let it go")
    assert music_tracker.list_songs() == ["Fireflies", "Let it go"] # > returns a list with fireflies and let it go inside.


def test_no_song_raises_error():

    music_tracker = MusicTracker()
    with pytest.raises(Exception) as e:
        music_tracker.track("")

    error_message = str(e.value)
    assert error_message == "No song given"


def test_incorrect_type_song_raises_error():

    music_tracker = MusicTracker()
    with pytest.raises(Exception) as e:
        music_tracker.track([3])
    error_message = str(e.value)
    assert error_message == "Incorrect type given"


def test_duplicate_songs_are_not_tracked():
    music_tracker = MusicTracker()
    music_tracker.track("Toxic")
    music_tracker.track("Let it go")
    music_tracker.track("Toxic")
    music_tracker.track("Let it go")
    assert music_tracker.listOfSongs == ["Toxic", "Let it go"]




# > raises exception here: No song given