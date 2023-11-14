from thefuzz import fuzz, process
import pandas as pd
import numpy as np

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
        comic = apiHelper.Comic(num=querry_num)
        comic.cli_display()


def get_dataset(datasetColumn):
    if datasetColumn in ['Title', 'SafeTitle', 'Link', 'IMGLink', 'Transcript', 'Alt']:
        df = pd.read_csv('./resources/data.csv', names=['Number', 'Title', 'SafeTitle', 'Link', 'IMGLink', 'Transcript', 'Alt'])
        df.set_index('Number', inplace=True)
        df.fillna('')
        return df[datasetColumn].to_list()
    else:
        print("Incorrect dataset column query")
        quit()

if __name__=="__main__":
    title_col = get_dataset('Title')
    alt_col = get_dataset('Alt')
    # print(title_col)

    query = input("Enter a querry : ")
    matches = closest(title_col, query=query)
    filtered_matches = list(map(lambda x: x[0], matches))
    print(matches)
    print(filtered_matches)
    data_set_fuzz(matched_data=filtered_matches)
    
