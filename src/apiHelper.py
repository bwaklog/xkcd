import requests, urllib.request
import os, sys, subprocess
from PIL import Image
from io import BytesIO


"""
The Comic object and some neat tools that come
along with it
1.  cli_display([, alt=False]) is a tool to display
    the details of the retrived comic in the CL
2.  comic_display([, ql=False])

"""
class Comic():

    # defining the structure of the object
    def __init__(self, url) -> None:

        if requests.get(url=url).status_code != 404:

            comic = requests.get(url=url).json()

            self.month = comic['month']
            self.num = comic['num']
            self.link = f"https://xkcd.com/{self.num}"
            self.year = comic['year']
            self.news = comic['news']
            self.safe_title = comic['safe_title']
            self.transcript = comic['transcript']
            self.alt = comic['alt']
            self.img = comic['img']
            self.title = comic['title']
            self.day = comic['day']

        else:
            print("Out of range")
            quit()

    
    def list_view(self):
        return [self.num, self.title, self.safe_title, self.link, self.img, self.transcript, self.alt]

    # cli tool to give a short summary on the comic
    def cli_display(self, alt=False):
        months = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
        print(f"""
XKCD Comic {self.num}
    > Title             :   {self.title}
    > Safe-Title        :   {self.safe_title}
    > Date              :   {months[int(self.month) - 1]} {self.year}
    > url               :   {self.link}
    > imgage url        :   {self.img}
    > transcript        :   {self.transcript}
""")
        if alt:
            print(f"    > alt               :   {self.alt}")

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
    
if __name__=="__main__":
    comic = Comic("https://xkcd.com/234/info.0.json")
    comic.cli_display(True)


def ComicInvavailibilityError():
    # raised when 404 is the status code for the request
    pass