# Panopto Download

This tool allows you to download a playlist from Panopto. Tested with Koç University playlists only. Should theoretically work for others given the UI is not very different.

## Requirements

- Internet Download Manager (Please suggest other tools if you know any. IDM is very convenient for pausing/resuming, is much better than browser default downloads, and has convenient command line capabilities)
- Selenium
- Gecko Webdriver (Firefox)

## Usage

Run the tool from the command line.

Example:
```python PanoptoDownloader.py "https://www.panoptolink.com/playlist" "C:/IDMMan.exe"```

Arguments: 
- private: Whether the link is behind a login screen. Gives the user time to log into their account
- pause: How much time to give the user to log in, default: 25 seconds
- URL: The url of the playlist
- IDMPath: The path to the IDM executable