from collections import Counter

def print_top_10(words_list, file_type):
    top_10 = Counter(words_list).most_common(10)
    print(f'Топ-10 самых часто встречающихся слов в новостях ({file_type}):')
    for place in top_10:
        print(f'{place[0]} -> {place[1]}')

def add_words_to_list(list_of_items, list_to_add):
    for word in list_of_items:
        if len(word) > 6:
            list_to_add.append(word)


# Задание №1
import json

all_words_json = []

with open('newsafr.json', encoding='utf-8') as f:
    json_data = json.load(f)

for item in json_data['rss']['channel']['items']:
    text = item['description'].split()
    add_words_to_list(text, all_words_json)
print_top_10(all_words_json, 'json')
print()

# Задание №2
import xml.etree.ElementTree as ET

all_words_xml = []

parser = ET.XMLParser(encoding='utf-8')
tree = ET.parse('newsafr.xml', parser)
root = tree.getroot()

news_list = root.findall('channel/item/description')

for news in news_list:
    text = news.text.split()
    add_words_to_list(text, all_words_xml)
print_top_10(all_words_xml, 'xml')