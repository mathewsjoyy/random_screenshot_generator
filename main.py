# importing modules
import urllib.request
from PIL import Image
import requests
from bs4 import BeautifulSoup
import urllib
import string
import random
from colorama import Fore
from colorama import Style


def randomize_url(url: str, max: int): 
  # This is just a long string of all possible letters and numbers
  choices = string.ascii_lowercase + string.digits
    
  result = url
    
  # Adds x amount of random choices from choices to given url
  for i in range(max):
    choice = random.choice(choices) # Get 1 random value
    result+=choice
    
  return result

def userInteract():
  while(True):
    try:
      user_option = input(f"> Types {Fore.GREEN}yes{Style.RESET_ALL} to generate another image, or {Fore.RED}no{Style.RESET_ALL} to exit.\n")
      
      if user_option in ["yes", "Yes", "YES", "y", "Y"]:
        return True # Carry on/nothing happens
      if user_option in ["no", "No", "NO", "n", "N"]:
        return False # Exit successfully
    except:
      print("! Unexpected error occurred, Try again !")
  

while(True):
  # Get randomized url for site print.sc, with random 6 letter/digit combo
  URL = randomize_url("https://prnt.sc/", 6)

  # Set headers otherwise urllib gives us 403 forbidden error
  headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
  req = urllib.request.Request(url=URL, headers=headers)

  # Use beautiful soup to read url
  url = urllib.request.urlopen(req).read()
  soup = BeautifulSoup(url, features="lxml")

  # Filter out for images
  srcs = [img['src'] for img in soup.find_all('img')]

  # Gets the image
  image_path = srcs[0]

  # Certain sites reject urlretrieve request (many reasons) so we add different headers
  opener = urllib.request.build_opener()
  opener.addheaders = [('User-Agent', 'MyApp/1.0')]
  urllib.request.install_opener(opener)

  # Download the image
  urllib.request.urlretrieve(
    image_path,
    "screenshot_random.png")

  # Open up and display the image
  img = Image.open("screenshot_random.png")
  img.show()
  
  # Ask user for what they want to do, generate more images, or exit
  if userInteract() == False:
    exit(0)
  
