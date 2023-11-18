import requests, re
from bs4 import BeautifulSoup
import apiHelper

def extract_links(query:str):
    # making the query ready for google search
    # xkcd emacs -> /search?q=xkcd+emacs
    query = "+".join(query.strip().split(' '))
    comic_numbers = []
    page = requests.get(f"https://google.com/search?q={query}")
    soup = BeautifulSoup(page.content, features='html.parser')
    links = soup.find_all("a")
    xkcd_com_re = re.compile(r'https:\/\/xkcd\.com\/\d+\/')
    comic_no_re = re.compile(r'\d+')
    for link in links:
        unfiltered_link = link.get('href')
        if "https://xkcd.com" in unfiltered_link:
            if match := xkcd_com_re.search(unfiltered_link):
                url = match.group()
                # print(f"URL : {match.group()}", end=" -> ")
                comic_no = comic_no_re.search(url).group()
                comic_numbers.append(comic_no)
                # print(f"Comic No : {comic_no}")

    return list(set(comic_numbers))

def web_scrape():
    prompt = input("Search Comic : ")
    comic_nums = extract_links(prompt)

    for num in comic_nums:
        comic = apiHelper.Comic(num=num)
        comic.cli_display()
    print("Search Other querry (s)")
    print("Quit (q)")
    comic_num = input("Enter a comic Number : ")
    if comic_num == "s":
        return 1
    elif comic_num == "q":
        return 0
    elif comic_num.isdigit():
        return apiHelper.Comic(comic_num)

if __name__=="__main__":
    comic_numbers = extract_links("xkcd emacs")
    for num in comic_numbers:
        comic = apiHelper.Comic(num=num)
        comic.cli_display()
