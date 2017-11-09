import webbrowser
import sys
import requests
# import pyperclip

# if (len(sys.argv) > 1):
#     address = ' '.join(sys.argv[1:])
# else:
#     address = pyperclip.paste()

# Address for the first location
address = input("Enter starting address: ".strip())
webbrowser.open("https://google.com/maps/place/" + address)

# Address for the second location
address2 = input("Enter second location: ".strip())
webbrowser.open("https://google.com/maps/place/" + address2)

# Tab for directions from first location to second location
direction = "https://google.com/maps/dir/" + address + "/" + address2
webbrowser.open(direction)

# Download the directions page
directions = requests.get(direction)

try:
    directions.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' %(exc))

