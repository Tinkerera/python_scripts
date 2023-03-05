import argparse
import requests

parser = argparse.ArgumentParser()

parser.add_argument("-u","--url",help="Target Url")
parser.add_argument("-w","--wordlist",help="Wordlist")

args = parser.parse_args()

wordlist = open(args.wordlist).read()
dirs = wordlist.splitlines()
url = args.url

for dir in dirs:
    dirs_open = f"http://{url}/{dir}.html"
    r = requests.get(dirs_open)
    if r.status_code==404:
        pass
    else:
        print("Directory found : ",dirs_open)
    dirs_open = f"http://{url}/{dir}.php"
    r = requests.get(dirs_open)
    if r.status_code==404:
        pass
    else:
        print("Directory found : ",dirs_open)
    dirs_open = f"http://{url}/{dir}"
    r = requests.get(dirs_open)
    if r.status_code==404:
        pass
    else:
        print("Directory found : ",dirs_open)
    
    
