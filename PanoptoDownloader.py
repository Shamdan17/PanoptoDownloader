import time

from selenium import webdriver
import subprocess
import argparse
import os.path
from tqdm import tqdm


parser = argparse.ArgumentParser(description='Downloads all videos from a panopto folder.')

parser.add_argument('url', metavar='URL', type=str,
                    help='The link of the playlist')
# parser.add_argument('path', metavar='IDMPath', help='The path to the IDM executable')
parser.add_argument('-private', action='store_false', help='Indicates that the video is private, give the user a pause to log in. Default: True')
parser.add_argument('-pause', default=25, help="Pause time to log in. Default is 25 seconds. Change it if the pause is too short.")

args = parser.parse_args()

# Is the video private (Protected behind a login screen)
# If true, gives the user time to login to their account
private_video = args.private
# Time window during which the user can log in (in seconds)
login_pause = args.pause
# Path of the IDM executable
# PathIDM = args.path
# URL of the folder of videos to download
URL = args.url

# Make sure that the maximum possible results per page are displayed (250)
URL = URL.split("&maxResults=")[0] + "&maxResults=250"

# create a new Firefox session
driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.maximize_window()

# Load the page
driver.get(URL)

# Give user time to login if videos are private
if private_video:
    time.sleep(login_pause)

# To ensure correct page in case of any redirection
driver.get(URL)
# Make sure correct link loads
time.sleep(5)

# Find all video thumbnails
el = driver.find_elements_by_class_name("thumbnail-link")
urls = []

for element in el:
    if(element.get_attribute("aria-label")!=None):
        name = element.get_attribute("aria-label")
        url = element.get_attribute("href")
        tokens = url.split('Pages/Viewer.aspx?id=')
        download_url = "{}Podcast/Social/{}.mp4".format(tokens[0], tokens[1])
        urls.append([download_url, name])


if private_video:
    temp_urls = urls
    urls = []
    for download_url, name in temp_urls:
        driver.get(download_url)
        time.sleep(2)
        download_url = driver.current_url
        urls.append([download_url, name])

print("Parsed URLs: ")
print(urls)

# tqdm iterator
t = tqdm(enumerate(urls), desc = "Downloading files", leave=True)
for idx, el in tqdm(urls):
    print(el)
    URL, name = el
    name = '{}'.format(name.replace("/", "-").replace(" ", ""))+'.mp4'
    if os.path.exists(name):
        i = 1
        while os.path.exists(f"{name[:-4]}({i}).mp4"):
            i+=1
        name = f"{name[:-4]}({i}).mp4"
    t.set_description(f"Downloading file number {idx}, Name: {name}")
    subprocess.call(['wget', '-O', name, URL])

driver.close()

