from bs4 import BeautifulSoup
import requests

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[91m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


print(bcolors.FAIL+bcolors.BOLD+"==========WELCOME TO AMARTYA's SHOP========= "+bcolors.ENDC)
a = str(input(bcolors.OKGREEN+"Search for product you want to buy: "+bcolors.ENDC))
params = {"q": a}
req = requests.get("http://www.google.com/search", params=params)
soup = BeautifulSoup(req.text, 'html.parser')
result = soup.find("a", {"class": "eZt8xd"})
ans = result.findAll("href")
print(bcolors.FAIL+bcolors.WARNING+bcolors.UNDERLINE+"------------------------------------------------------------------------"+bcolors.ENDC)
print(bcolors.OKBLUE+"              ============="+result.text+" item fond!!=============="+bcolors.ENDC)
if(result.text == "Shopping"):
    print(bcolors.FAIL+bcolors.WARNING+bcolors.UNDERLINE+"------------------------------------------------------------------------"+bcolors.ENDC)
    print(bcolors.OKGREEN+bcolors.BOLD+"LINK: ""http://www.google.com"+result.attrs["href"]+bcolors.ENDC)
    print(bcolors.BOLD+"\n          THANK YOU FOR CHOOSING US :)"+bcolors.ENDC)
else:
    print(bcolors.FAIL+"Search for shopping items :("+bcolors.ENDC)