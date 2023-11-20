import requests, urllib.request
import os, sys, subprocess
from PIL import Image
from io import BytesIO
import pandas as pd
import pytesseract
import nltk


STOPWORDS = nltk.corpus.stopwords.words('english')


def check_storage(num):
    # headers -> Number, Title, Img, Transcript, Alt, Content
    df = pd.read_csv('./src/resources/comics.csv', names=["Number", "Title", "Img", "Transcript", "Alt", "Content"])[1:]
    df.set_index('Number', inplace=True)

    return str(num) in df.index.tolist()
    # check if record exists for `num`





"""
The Comic object and some neat tools that come
along with it
1.  cli_display([, alt=False]) is a tool to display
    the details of the retrived comic in the CL
2.  comic_display([, ql=False])
"""
class Comic():

    # defining the structure of the object
    def __init__(self, num):
        
        # check if comic metadata exists within the local csv
        if check_storage(num):
            print("Using data from local storage")
            # if the record exists withn the csv file
            df = pd.read_csv('./src/resources/comics.csv', header=0)
            df.set_index('Number', inplace=True)
            
            # get the row content
            data = df.loc[int(num)].to_dict() 

            # Columns
            # Number, Title, Img, Transcript, Alt, Content
            self.num = num
            self.url = f"https://xkcd.com/{num}"
            self.title = data[" Title"]
            self.img = data[" Img"]
            self.trans = data[" Transcript"]
            self.alt = data[" Alt"]
            self.content = data[" Content"]

        
        # if it doenst exist in the csv
        # NOTE, there will never be a case where 404 is requested
        # The prompt will handle that part of the code, so i'm not
        # including the exception case here

        else:
            print("There is no data for this local, so fetching using api")
            comic_req = requests.get(f'https://xkcd.com/{num}/info.0.json')

            # Quits the code entirely, for safety purpose...
            if comic_req.status_code != 404:
                try:
                    comic_data = comic_req.json()
                    self.num = num
                    self.url = f"https://xkcd.com/{num}"
                    self.title = comic_data['title']
                    self.trans = comic_data['transcript']
                    self.alt = comic_data['alt']
                    self.img = comic_data['img']
                    self.content = ""

                    # Image processing using OCR to generate text
                    try:
                        comic_image_obj = Image.open(
                            BytesIO(requests.get(self.img).content)
                        )
                        
                        unfiltered_content_text = self.image_processing(comic_image_obj)

                        # removing stopwords
                        self.content = ' '.join(
                            word.lower() for word in unfiltered_content_text.split()
                            if word not in STOPWORDS
                        )
                    
                    except requests.HTTPError:
                        print("HTTPError")
                        self.content = ""
                
                except requests.HTTPError:
                    print("HTTPError")
                    self.content = ""
            
            else:
                print("404 Error")


    # used for OCR on comic images during initialization
    def image_processing(self, image_obj):
        try:
            # using pytesseract's OCR
            return pytesseract.image_to_string(image_obj)
        except pytesseract.TesseractError:
            print(f"[{self.num}] : Tesseract Error")
            return ""
        except pytesseract.TesseractNotFoundError:
            print(f"[{self.num}] : Tesseract Not Found Error")
            return ""
        


    # this is used in some part of code for searching data quicker
    def list_view(self):
        # Number, Title, Img, Transcript, Alt, Content
        return [self.num, self.title, self.img, self.trans, self.alt, self.content]

    
    # cli tool to give a short summary on the comic
    def cli_display(self, extra=False, broken_content=False):
        print(f"""
XKCD Comic {self.num} - {self.title}
> url       :   https://xkcd.com/{self.num}/
> expalin   :   https://explainxkcd.com/{self.num}/
> image     :   {self.img}
""")
        if extra:
            print(f"""
> alt       : {self.alt}
""")
        if broken_content:
            print(f"""
> content   : {self.content}
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


    
if __name__=="__main__":
    comic = Comic(2856)
    comic.cli_display()
    # comic.comic_display(True)