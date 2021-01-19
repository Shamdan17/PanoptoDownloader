# Panopto Download

This tool allows you to download a playlist from Panopto. Tested with Koç University playlists only. Should theoretically work for others given the UI is not very different.

## Requirements

- [Selenium](https://selenium-python.readthedocs.io/installation.html) 
- [Gecko Webdriver](https://github.com/mozilla/geckodriver/releases) (Firefox)

## Usage

Place the webdriver somewhere in your path (Could be in the same folder as the repository)
Run the tool from the command line.

Example:
```python PanoptoDownloader.py "https://www.panoptolink.com/playlist"```

Arguments: 
- private: Whether the link is behind a login screen. Gives the user time to log into their account. Default is True, use the flag to disable this.
- pause: How much time to give the user to log in, default: 25 seconds
- URL: The url of the playlist