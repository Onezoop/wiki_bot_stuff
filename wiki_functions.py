import json
import Levenshtein as lv

with open("WIKI_URL.txt", 'r') as wiki_url_file:
    WIKI = wiki_url_file.read()[:-1]
if WIKI[-1] != '/':
    WIKI += '/'
def parse_json_into_dict():
    with open('pages.json') as pages_table:
        main_list = json.load(pages_table)['query']['allpages']
    page_dict = {}
    for i in main_list:
        page_dict[i['title']] = i['pageid']
    return page_dict

def find_closest_page_from_input(text_input:str):
    data = parse_json_into_dict().keys()
    string_vals = {}
    for i in data:
        string_vals[i] = (lv.distance(text_input, i))
    current_min = list(string_vals)[0]
    for i in string_vals:
        if string_vals[i] < string_vals[current_min]:
            current_min = i
    return current_min

def return_a_pageurl(user_input:str):
    page_dict = parse_json_into_dict()
    closest_user_input = find_closest_page_from_input(user_input)
    return f"{WIKI}?curid={page_dict[closest_user_input]}"
