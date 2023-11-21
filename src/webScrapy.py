import requests, re
from bs4 import BeautifulSoup
import apiHelper

def extract_links(query:str):
    """
    making the query ready for google search
    xkcd emacs -> /search?q=xkcd+emacs
    ^^^^ This prompt would be kinda shit

    prompt : emacs programming
    corrected prompt : emacs+programing
    search querry : "xkcd+"+corrected prompt
    """
    query = "xkcd+"+"+".join(query.strip().split(' '))
    comic_numbers = []
    print(query)
    page = requests.get(f"https://google.com/search?q={query}")
    print(page)
    soup = BeautifulSoup(page.content, features='html.parser')
    links = soup.find_all("a")
    xkcd_com_re = re.compile(r'https:\/\/xkcd\.com\/\d+\/') 
    comic_num_re = re.compile(r'\d+')
    for link in links:
        unfiltered = link.get('href')
        if match:= xkcd_com_re.search(unfiltered):
            if num:= comic_num_re.search(match.group()):
                comic = apiHelper.Comic(num=num.group())
                comic.cli_display()

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
