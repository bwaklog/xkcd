# from thefuzz import fuzz, process
from rapidfuzz import process, fuzz, utils
import pandas as pd
import numpy as np
import apiHelper
from nltk.corpus import stopwords

def closest(datasetColumn, query):
    return process.extract(
        query=query,
        choices=datasetColumn,
        scorer=fuzz.WRatio,
        limit=10,
        processor=utils.default_process
    )

def data_set_fuzz(matched_data, col):
    df = pd.read_csv('./src/resources/data.csv', names=['Number', 'Title', 'SafeTitle', 'Link', 'IMGLink', 'Transcript', 'Alt'])
    df.set_index('Number', inplace=True)
    for match, similarity, extra in matched_data[::-1]:
        querry_num = df.loc[df[col] == match].index.item()
        comic = apiHelper.Comic(num=querry_num)
        # comic.cli_display()
        print(f"Number : {comic.num}")
        print(f'{"Title".ljust(15)}{comic.title}')
        print(f'{"Alt".ljust(15)}{comic.alt}')
        print(f"Similarity = {similarity}")
        print("====================================")

def fuzzy_prompt():
        search_query = input("Enter a Title Name : ")
        matches_title = closest(
            datasetColumn=TITLE_COL, 
            query=search_query.title()
        )
        data_set_fuzz(matched_data=matches_title, col='Title')
        print("Search Other querry (s)")
        print("Quit (q)")
        comic_num = input("Enter Comic Number : ")
        if comic_num.isalnum and comic_num.lower() == 's':
            return 1
        elif comic_num.isalpha and comic_num.lower == 'q':
            quit()
        else:
            comic = apiHelper.Comic(num=int(comic_num))
            comic.cli_display()
            return comic

cahced_stopwords = stopwords.words("english")
def stop_word_filter(string):
    return ' '.join(
        [
            word
            for word in str(string).split()
            if word not in cahced_stopwords and word.isalnum()
        ]
    )

def alt_serach():
    alt_col = [str(string) for string in get_dataset('Alt')]
    # alt_json = get_json('Alt')
    # alt_col = [alt_json[num] for num in alt_json]
    # alt_col_filtered = [stop_word_filter(string=string)for string in list(alt_col)]
    title_col = TITLE_COL

    search_querry = input("🔍 Search : ")
    matched_title = like_fxn(datasetCol=title_col, search_querry=search_querry)
    match_pair_find('Title', matched_title)
    matched_alt = like_fxn(datasetCol=alt_col, search_querry=search_querry)
    match_pair_find('Alt', matched_alt)

    print("Search Other querry (s)")
    print("Quit (q)")
    comic_num = input("Enter Comic Number : ")
    if comic_num.isalnum and comic_num.lower() == 's':
        return 1
    elif comic_num.isalpha and comic_num.lower == 'q':
        quit()
    else:
        return apiHelper.Comic(num=int(comic_num))


def like_fxn(datasetCol, search_querry):
    return [
        alt
        for alt in datasetCol
        if search_querry in alt
    ]

def match_pair_find(datasetCol, data):
    df = pd.read_csv('./src/resources/data.csv', names=['Number', 'Title', 'SafeTitle', 'Link', 'IMGLink', 'Transcript', 'Alt'])
    df.set_index('Number', inplace=True)
    for match in data[::-1]:
        comic_num = df[df[datasetCol] == match].index.item()
        comic = apiHelper.Comic(num=comic_num)
        print(f"Number : {comic.num}")
        print(f'{"Title".ljust(15)}{comic.title}')
        print(f'{"Alt".ljust(15)}{comic.alt}')
        # print(f"Match Percentage {percent_match}%")
        print("====================================")



def get_dataset(datasetColumn):
    if datasetColumn in ['Title', 'SafeTitle', 'Link', 'IMGLink', 'Transcript', 'Alt']:
        df = pd.read_csv('./src/resources/data.csv', names=['Number', 'Title', 'SafeTitle', 'Link', 'IMGLink', 'Transcript', 'Alt'])
        df.set_index('Number', inplace=True)
        df.fillna('')
        return df[datasetColumn].to_list()
    else:
        print("Incorrect dataset column query")
        quit()

TITLE_COL = get_dataset('Title')
# ALT_COL = get_dataset('Alt')

if __name__=="__main__":
    # print(title_col)
    query = input("Enter a querry : ")
    matches = closest(TITLE_COL, query=query)
    filtered_matches = list(map(lambda x: x[0], matches))
    print(matches)
    print(filtered_matches)
    data_set_fuzz(matched_data=filtered_matches)
    
