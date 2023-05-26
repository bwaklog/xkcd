import requests
import json
import sys


def get_latest_comic(verbose):
    exists = True
    # Check last saved latest checkpoint
    with open("latest.txt", "r") as f:
        comic = int(f.read())
    while exists:
        if verbose:
            print(f"    current comic =====> {comic}")
        req = requests.get(f"https://xkcd.com/{str(comic)}/info.0.json")
        if req.status_code != 404:
            # open latest.txt in write mode and write
            # the latest comic to file
            with open("latest.txt", "w") as f:
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


def get_comic(verbose=False, comic="latest"):
    latest_comic = get_latest_comic(verbose)
    if comic.isdigit() and int(comic) > latest_comic:
        return f"ERROR, latest comic is {latest_comic}"

    if comic == "latest":
        comic_request = requests.get(
            f"https://xkcd.com/{str(latest_comic)}/info.0.json")
        comic = Comic(comic_request.json())
        comic.display()
        return "👋🐍 hisss."

    else:
        comic_number = str(comic)
        comic_request = requests.get(
            f"https://xkcd.com/{comic_number}/info.0.json")
        comic = Comic(comic_request.json())
        comic.display()

        return "👋🐍 hisss."


if __name__ == "__main__":
    verbose, comic = False, "latest"
    flags = sys.argv[1:]
    print(flags)
    if flags != []:
        if flags[0] in ['-l', '--latest']:
            print("🚀 Getting latest comic")
            print(get_comic(verbose, comic))
        elif flags[0].isdigit():
            print(f"🔎 Fetching comic {flags[0]}")
            print(get_comic(verbose, flags[0]))
    else:
        print("No flags passed")
