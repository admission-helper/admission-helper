# from urllib.request import urlopen

# logo = urlopen("https://clck.ru/NaVg2").read()
# f = open("docs.pdf", "rb")
# f.write(logo)
# f.close()

url = 'https://bit-ly.ru/qNb7'
 
# downloading with urllib
 
# import the urllib package
import urllib.request
 
# Copy a network object to a local file
urllib.request.urlretrieve(url, "tutorial.pdf")
 
 
# downloading with requests
 
# import the requests library
import requests
 
# download the file contents in binary format
r = requests.get(url)
 
# open method to open a file on your system and write the contents
with open("doc", "wb") as code:
    code.write(r.content)