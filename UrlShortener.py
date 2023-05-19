import pyshorteners

url= input("Enter the URl: ")

def shortner(url):
    s = pyshorteners.Shortener()
    print('Short url is')
    print(s.tinyurl.short(url))

shortner(url)    