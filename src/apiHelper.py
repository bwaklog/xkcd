import requests, urllib.request
import os, sys, subprocess
from PIL import Image
from io import BytesIO
import pandas as pd

# ahh circular import
def check_storage(num):
    df = pd.read_csv('./src/resources/data.csv', names=['Number', 'Title', 'SafeTitle', 'Link', 'IMGLink', 'Transcript', 'Alt'])
    df.set_index('Number', inplace=True)
    return not df.loc[df.index == num].empty


"""
The Comic object and some neat tools that come
along with it
1.  cli_display([, alt=False]) is a tool to display
    the details of the retrived comic in the CL
2.  comic_display([, ql=False])
"""
class Comic():

    # defining the structure of the object
    def __init__(self, num) -> None:

        if not check_storage(num):
            url = f"https://xkcd.com/{num}/info.0.json"
            if requests.get(url=url).status_code != 404:

                comic = requests.get(url=url).json()

                self.num = comic['num']
                self.title = comic['title']
                self.safe_title = comic['safe_title']
                self.link = f"https://xkcd.com/{self.num}"
                self.img = comic['img']
                self.transcript = comic['transcript']
                self.alt = comic['alt']

            else:
                print("Out of range")
                quit()
        else:
            comic = csvTool(num=num)
            self.num = comic.index.item()
            self.title = comic['Title'].item()
            self.safe_title = comic['SafeTitle'].item()
            self.link = f"https://xkcd.com/{self.num}"
            self.img = comic['IMGLink'].item()
            self.transcript = comic['Transcript'].item()
            self.alt = comic['Alt'].item()

    def list_view(self):
        return [self.num, self.title, self.safe_title, self.link, self.img, self.transcript, self.alt]

    # cli tool to give a short summary on the comic
    def cli_display(self, alt=False):
        months = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
        print(f"""
XKCD Comic {self.num}
    > Title             :   {self.title}
    > Safe-Title        :   {self.safe_title}
    > url               :   {self.link}
    > imgage url        :   {self.img}
""")
        if alt:
            print(f"""
    > transcript        :   {self.transcript}
    > alt               :   {self.alt}
""")

    # comic display functionality
    def comic_display(self, ql=False):
        urllib.request.urlretrieve(self.img, f"comic_number_{self.num}.png")
        if (sys.platform != 'darwin') & ql:
            print("[ 🤓👆 ] : Aktually...that QL isn't there on your system")
        # if the platform code is being executed on is
        # a mac that supports quick look with qlmanage
        if (sys.platform == 'darwin') & ql:    
            try:
                subprocess.Popen(["qlmanage", "-p", f'comic_number_{self.num}.png'])
            except FileNotFoundError:
                print("Quick Look is not available on this system")

            os.wait()
            os.remove(f'comic_number_{self.num}.png')

        # If system is not "darwin"
        # This is for "linux-x86_64" or "win-32" etc.
        else:
            Image.open(f"comic_number_{self.num}.png").show()
            os.remove(f'comic_number_{self.num}.png')


        print("👋🐍 hiss.") 

    # system saving functionality

def csvTool(num):
    df = pd.read_csv('./src/resources/data.csv', names=['Number', 'Title', 'SafeTitle', 'Link', 'IMGLink', 'Transcript', 'Alt'])
    df.set_index('Number', inplace=True)
    # return not df.loc[df.index == comic_number].empty
    return df.loc[df.index == num]
    
if __name__=="__main__":
    comic = Comic(234)
    comic.cli_display(True)
    comic.comic_display(False)


def ComicInvavailibilityError():
    # raised when 404 is the status code for the request
    pass