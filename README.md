# spotipy-jukebox
A Python application for setting up a Raspberry Pi + SenseHAT Spotify jukebox. Press a button to add a random Top 20 song from a chosen genre to a collaborative playlist. 

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites
This project is built in Python3. The jukebox relies on VLC (`sudo apt-get install vlc`), Spotipy (`sudo pip3 install spotipy`), and the Python VLC library (`sudo pip3 install python-vlc`).

This implementation also uses the SenseHAT for button presses and displaying the track title. Make sure that is connected to your Pi before booting up.

Lastly, for modifying playlists, you'll need to authenticate Spotipy and make an app on the [Spotify Developer site](//developer.spotify.com).

### Installing
* Install dependencies (see above)
* Register a new app on the Spotify Developer site
* Create a `spotifycreds.py` file in the same directory. In this file, create 3 variables that will store your Client Secret, Client ID, and Redirect URL (for the URL, it's easiest to simply put http://localhost)
* Create a PUBLIC playlist on Spotify that you can use. Click "Share" and copy the ID of the playlist with which to replace `pl_id` variable value
* Run your application once to pull up the redirect URL; then, copy/paste the full URL it tried to access into your Python shell as prompted
Run the code a second time, and you should be good to go! Test with the sample code: enter a genre ('rock', 'pop', 'hiphop', etc) to see the Top 20 tracks onscreen, choose a random song, add it to the playlist

## Built With
* [Spotipy](https://github.com/plamere/spotipy) - Lightweight Python Spotify API library
* [Python-vlc](https://pypi.python.org/pypi/python-vlc) - Python wrapper for VLC commands

## Authors
* **Kevin Olson** - *Initial work* - [olsonk](https://github.com/olsonk)

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments
* Thanks to Paul Lamere for Spotipy!
