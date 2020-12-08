import sys
import urllib
import urllib.request
import os

os.system('cls')

sys.ps1 = '\033[01;32m '

print(sys.ps1)

print('''
 ████████╗██████╗ ██████╗ ██████╗ 
╚══██╔══╝██╔══██╗╚════██╗╚════██╗
   ██║   ██████╔╝ █████╔╝ █████╔╝
   ██║   ██╔══██╗ ╚═══██╗ ╚═══██╗
   ██║   ██║  ██║██████╔╝██████╔╝
   ╚═╝   ╚═╝  ╚═╝╚═════╝ ╚═════╝ 
                                 
                       
''')



url = input("Enter your url with ID paramenters : ")

if (url == "help"):
      print('''

            for example:
          http://example.com/index.php?id=1

            ''')
      sys.exit()
else:
     req = urllib.request.urlopen(url + "\'")
     b10 = req.read()
     fb100 = b10.decode('utf-8')
     if "You have an error in your SQL syntax" in fb100:
         print(url, " is vulnerable")
     else:
          print(url, " is not vulnerable")
