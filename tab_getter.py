import spotipy
import spotipy.util as util
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def get_tab(search_name, site):
	#Opens a browser window for Chrome with selenium
	browser =  webdriver.Chrome()
	#Opens up gooogle and makes a search using the currently playing song name + the type of data you want to search
	browser.get('http://www.google.com')
	searchBar = browser.find_element_by_name('q')
	searchBar.send_keys(search_name)
	searchBar.send_keys(Keys.ENTER)
	link = browser.find_element_by_partial_link_text(site)
	link.click()

def get_song():
	# Get this from your spotify account profile url
	username = 'xxxxxx' 
	#Defines what kind of info you're getting from the Spotify Api
	scope = "user-read-currently-playing"
	#Get these from the spotify dev site
	CLIENT_ID = 'xxxxxxx'
	CLIENT_SECRET = 'xxxxxxx'
	redirect_uri = "http://google.com/"

	#Authenticate the token using spotipy
	token = util.prompt_for_user_token(username, scope, CLIENT_ID, CLIENT_SECRET, redirect_uri)

	#Spotify object
	sp = spotipy.Spotify(auth=token)

	#Gets the data for the currently playing song.
	results = sp.currently_playing()

	#Takes the song from the currently playing dictionary.
	song = results['item']
	song_name = song['name']

	#Sorts through the artists dict and gets the artist name. 
	song_artists = song['artists']
	for item in song_artists:
		song_artist = (item['name'])


	#Takes user input for what kind of data to search and selects appropriate search results for get_tab()
	while True:
		choice = input("1 for lyrics, 2 for guitar tab, 3 for bass tab: ")
		if choice == '1':
			search_name = song_name + ' ' + song_artist + (' lyrics')
			site = 'genius'
			get_tab(search_name, site)
		elif choice == '2':
			search_name = song_name + ' ' + song_artist + (' guitar tab')
			site = 'ultimate'
			get_tab(search_name, site)
			
		elif choice == '3':
			search_name = song_name + ' ' + song_artist + (' bass tab')
			site = 'ultimate'
			get_tab(search_name, site)
		else:
			True




get_song()
