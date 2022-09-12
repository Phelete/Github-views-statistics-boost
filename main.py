import requests
import threading
import bs4

nick = input("Nick: ")
count = input("Boost count: ")
thread = int(input("Thread count: "))
typ = input("Boost type(G,D): ")

if "+" in count:
    count = int(count)
else:
    link = f"https://gpvc.arturio.dev/{nick}"
    current=bs4.BeautifulSoup(requests.get(link).text, 'html.parser').find("title").text.split(":")[1]
    count = int(count) - int(current)
if count > 0:
    print(f"Boosting: {count}")
else:
    print(f"Counts more on: {abs(count)}")

def add(nick, count, typ):
    link=""
    if typ == "G":
        link += f"https://github.com/{nick}"
    elif typ == "D":
        link += f"https://gpvc.arturio.dev/{nick}"
    else:
        link += f"https://gpvc.arturio.dev/{nick}"
    for i in range(count):
        req=requests.get(link)
        text=req.text
        vc = bs4.BeautifulSoup(text, 'html.parser').find("title").text
        print(f"\n{vc}")

for i in range(thread):
    threading.Thread(target=add, args=(nick, count//thread, typ)).start()