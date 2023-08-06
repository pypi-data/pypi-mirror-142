import requests
import os

def download_word_lists():
    base_url = "https://raw.githubusercontent.com/3b1b/videos/master/_2022/" + \
               "wordle/data/"
    word_lists = ['allowed_words', 'possible_words']
    for word_list in word_lists:
        url = base_url + word_list + '.txt'
        r = requests.get(url)  
        if os.path.exists('data') is False:
            os.makedirs('data') 
        with open(f'data/{word_list}.txt', 'wb') as f:
            f.write(r.content)


if __name__ == "__main__":
    download_word_lists()
