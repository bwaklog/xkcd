import requests
import sys
import subprocess
from PIL import Image
from io import BytesIO
import os


def get_latest_comic(verbose):
    exists = True
    # Check last saved latest checkpoint
    with open("/Users/adityahegde/Documents/GitHub/xkcd_view/resources/latest.txt", "r") as f:
        comic = int(f.read())
    while exists:
        if verbose:
            print(f"    current comic =====> {comic}")
        req = requests.get(f"https://xkcd.com/{str(comic)}/info.0.json")
        if req.status_code != 404:
            # open latest.txt in write mode and write
            # the latest comic to file
            with open("/Users/adityahegde/Documents/GitHub/xkcd_view/resources/latest.txt", "w") as f:
                f.write(str(comic))
                f.flush()
            comic += 1
        if req.status_code == 404:
            exists = False
            return comic - 1


class Comic:
    def __init__(self, comic):
        self.comic = comic

        self.num = comic['num']
        self.link = comic['link']
        self.year = comic['year']
        self.alt = comic['alt']
        self.img = comic['img']
        self.title = comic['title']

    def display(self):
        display_text = f"""
XKCD Comic {self.num}
    > year {self.year}
    > title {self.title}
    > comic {self.img}
    > alt {self.alt}
        """
        print(display_text)

    def show(self):
        Image.open(BytesIO(requests.get(self.img).content)).show()


def get_comic(verbose=False, comic="latest"):
    latest_comic = get_latest_comic(verbose)
    if comic.isdigit() and int(comic) > latest_comic:
        return f"ERROR, latest comic is {latest_comic}"

    if comic == "latest":
        comic_request = requests.get(
            f"https://xkcd.com/{str(latest_comic)}/info.0.json")
        comic = Comic(comic_request.json())
        return comic

    else:
        comic_number = str(comic)
        comic_request = requests.get(
            f"https://xkcd.com/{comic_number}/info.0.json")
        comic = Comic(comic_request.json())
        return comic


verbose, comic = False, "latest"
flags = sys.argv[1:]
# print(flags)
if flags != []:
    if flags[0] in ['-l', '--latest']:
        print("🚀 Getting latest comic")
        comic = get_comic(verbose, comic)
        comic.display()
    elif flags[0].isdigit():
        print(f"🔎 Fetching comic {flags[0]}")
        comic = get_comic(verbose, flags[0])
        comic.display()
    elif flags[0] in ['-a', '--all']:
        pass
    if len(flags) > 1:
        if flags[1] in ['-q', '--ql']:
            print("Trying Quick Look")

            comic_img = Image.open(
                BytesIO(requests.get(comic.img).content)).save('buff.png')

            try:
                subprocess.Popen(["qlmanage", "-p", 'buff.png'])
            except FileNotFoundError:
                print("Quick Look is not available on this system")

            os.wait()
            os.remove('buff.png')
            print("👋🐍 hiss.")
else:
    print("No flags passed")
