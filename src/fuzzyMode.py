from thefuzz import fuzz, process
import pandas as pd
import numpy as np
import apiHelper

def closest(datasetColumn, query):
    return process.extract(
        query=query,
        choices=datasetColumn,
        scorer=fuzz.token_sort_ratio,
        limit=10
    )

def data_set_fuzz(matched_data):
    import apiHelper
    df = pd.read_csv('resources/data.csv', names=['Number', 'Title', 'SafeTitle', 'Link', 'IMGLink', 'Transcript', 'Alt'])
    df.set_index('Number', inplace=True)
    for match_title in matched_data:
        # print(match_title)
        querry_num = df.loc[df['Title'] == str(match_title)].index.item()
        # comic = apiHelper.Comic(num=querry_num)
        # comic.cli_display()
        print(f"Comic {querry_num}      : {match_title}")

def fuzzy_prompt(inp='init'):
        search_query = input("Enter a Title Name : ")
        matches = list(map(lambda x: x[0],
                            closest(
                            datasetColumn=TITLE_COL,
                            query=search_query
                        )))
        data_set_fuzz(matched_data=matches)
        print("Search Other querry (s)")
        print("Quit (q)")
        comic_num = input("Enter Comic Number : ")
        if comic_num.isalnum and comic_num.lower() == 's':
            return 1
        elif comic_num.isalpha and comic_num.lower == 'q':
            return 0
        else:
            comic = apiHelper.Comic(num=int(comic_num))
            comic.cli_display()
            return comic




def get_dataset(datasetColumn):
    if datasetColumn in ['Title', 'SafeTitle', 'Link', 'IMGLink', 'Transcript', 'Alt']:
        df = pd.read_csv('./resources/data.csv', names=['Number', 'Title', 'SafeTitle', 'Link', 'IMGLink', 'Transcript', 'Alt'])
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
    
