import webbrowser
import sys
import pyperclip

if (len(sys.argv) > 1):
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

address2 = input("Enter second location: ".strip())

webbrowser.open("https://google.com/maps/place/" + address)

webbrowser.open("https://google.com/maps/place/" + address2)

