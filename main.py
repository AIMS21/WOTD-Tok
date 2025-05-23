# main.py
import requests

def fetch_word_data(word="hello"):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)
    data = response.json()
    # print(data, '\n')
    if isinstance(data, list):
    #     for x in data:
    #         for key1 in x: 
                
    #             dict1 = x[key1]
    #             if isinstance(dict1, str):
    #                 print(key1, ":", x[key1])
    #             else: 
    #                 print(key1, ":")
    #             if isinstance(dict1, list):   
    #                 for index, y in enumerate(dict1): 
    #                     if isinstance(y, dict): 
    #                         for key2 in y:
    #                             print('\t', index, key2, ":", y[key2], '\n')
    #                     elif isinstance(y, list):    
    #                         for z in y:
    #                             print('HEEEEEEERE', z) 
    #             elif isinstance(dict1, dict):
    #                 for key3 in dict1:
    #                     print('\t', key3, ":", dict1[key3])
    #             print()
        meaning = data[0]['meanings'][0]['definitions'][0]['definition']
        example = data[0]['meanings'][0]['definitions'][0].get('example', '')
        return word, meaning, example
    else:
        raise Exception("Word not found.")

# Test
word, definition, example = fetch_word_data()
print(word, definition, example)

