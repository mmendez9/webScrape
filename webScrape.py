import webbrowser
import requests

# Address for the first location
address = input("Enter starting address: ".strip())

# Address for the second location
address2 = input("Enter second location: ".strip())

# Tab for directions from first location to second location
direction = "https://google.com/maps/dir/" + address + "/" + address2

# Open the browser tabs
webbrowser.open("https://google.com/maps/place/" + address)
webbrowser.open("https://google.com/maps/place/" + address2)
webbrowser.open(direction)

# Download the directions page
directions = requests.get(direction)

try:
    directions.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' %(exc))

file = open("directions.txt", 'wb')

for data in directions.iter_content(100000):
    file.write(data)
file.close()


