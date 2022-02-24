import webbrowser
import sys

x = input("To open the secret link, type your password: ")

def command():
    if x == "open":
        webbrowser.open("https://www.w3schools.com/python/python_json.asp")
        print("password accepted")
    else:
        print("Sorry, your password has been denied, shutting down")
        sys.exit()

command()

