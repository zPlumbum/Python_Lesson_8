# Задание №1
import json

all_words_json = []
top_words_json = {}

with open('newsafr.json', encoding='utf-8') as f:
    json_data = json.load(f)

for item in json_data['rss']['channel']['items']:
    text = item['description'].split()
    for word in text:
        if len(word) > 6:
            all_words_json.append(word)
for word in all_words_json:
    if word not in top_words_json.keys():
        top_words_json.setdefault(word, all_words_json.count(word))

def by_value(item):
    return item[1]

print('Топ-10 самых часто встречающихся слов в новостях (json):')
for key, value in sorted(top_words_json.items(), key=by_value, reverse=True)[:10]:
    print(key, '->', value)
print()

# Задание №2
import xml.etree.ElementTree as ET

all_words_xml = []
top_words_xml = {}

parser = ET.XMLParser(encoding='utf-8')
tree = ET.parse('newsafr.xml', parser)
root = tree.getroot()

news_list = root.findall('channel/item')

for news in news_list:
    text = news.find('description').text.split()
    for word in text:
        if len(word) > 6:
            all_words_xml.append(word)
for word in all_words_xml:
    if word not in top_words_xml.keys():
        top_words_xml.setdefault(word, all_words_xml.count(word))

print('Топ-10 самых часто встречающихся слов в новостях (xml):')
for key, value in sorted(top_words_xml.items(), key=by_value, reverse=True)[:10]:
    print(key, '->', value)