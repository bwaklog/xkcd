from apiHelper import Comic
import csv
import requests
import pandas as pd

def get_latest(verbose=False):
    df = pd.read_csv('./src/resources/data.csv', names=['Number', 'Title', 'SafeTitle', 'Link', 'IMGLink', 'Transcript', 'Alt'])
    df.set_index('Number')
    latest = df[-1:].index.item()
    found = True
    #checking if the latest comic number is in sync with whats online
    # checking for latest += 1
    while found:
        if requests.get(url=f"https://xkcd.com/{latest}/info.0.json").status_code == 404:
            return latest - 1
        else:
            latest += 1

def update_storage():
    latest = get_latest(verbose=False)
    for i in range(latest, 0, -1):
        if i == 404:
            print("404 page")
        elif not check_storage(i):
            comic = Comic(num=i)
            with open('./src/resources/data.csv', mode='a', newline='\n') as f:
                writer = csv.writer(f, delimiter=',')
                writer.writerow([comic.num, comic.title, comic.safe_title, \
                            comic.link, comic.img, comic.transcript, comic.alt])
                f.flush()
                print(f"Comic {i} added to storage")
        else:
            print(f"Comic {i} exists in storage")
            break

def check_storage(comic_number:int):
    df = pd.read_csv('./src/resources/data.csv', names=['Number', 'Title', 'SafeTitle', 'Link', 'IMGLink', 'Transcript', 'Alt'])
    df.set_index('Number', inplace=True)
    return not df.loc[df.index == comic_number].empty

if __name__=="__main__":
    update_storage()
