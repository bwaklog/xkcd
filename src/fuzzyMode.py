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

def return_closest_comics():
    return None

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
    print(title_col)

    query = input("Enter a querry : ")
    matches = closest(title_col, query=query)
    filtered_matches = list(map(lambda x: x[0], matches))
    print(filtered_matches)
