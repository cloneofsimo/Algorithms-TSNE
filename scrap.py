import requests
from bs4 import BeautifulSoup as bs
from tqdm import tqdm
import json

pendings = []

def pender(page):

    raw = requests.get(page, headers={'User-Agent':'Mozilla/5.0'})
    html = bs(raw.text, "html.parser")
    alls = html.find_all('a')



    for As in alls:
        try:
            if As['href'].split('/')[-2] == 'tags':
                pendings.append(As['href'])
        except:
            pass

for i in range(1, 7):
    pender("https://solved.ac/problems/tags?page=" + str(i))

pendings = list(set(pendings))
print(pendings)
print(len(pendings))
pbar = tqdm(pendings)

IM = {}
cnt = 0
for algo in pbar:
    IM[algo] = []
    page = 'https://solved.ac' + algo + '?page='
    for idx in range(1, 20):
        page_ = page + str(idx)
        raw = requests.get(page_, headers={'User-Agent':'Mozilla/5.0'})
        html = bs(raw.text, "html.parser")
        alls = html.find_all('a')
        if len(alls) == 49:
            break
        for As in alls:
            try:
                if As['href'].split('/')[-2] == 'problem':
                    prob = As['href'].split('/')[-1]
                    IM[algo].append(prob)
                    cnt += 1
                    pbar.set_description(f"Done {cnt}, doing {prob}, has algo {algo}")
            except:
                0
    


with open('data.txt', 'w') as outfile:
    json.dump(IM, outfile)