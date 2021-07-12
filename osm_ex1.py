from bs4 import BeautifulSoup as bs

with open('map1.osm', 'r', encoding='utf-8') as osm_xml:
    osm_str = osm_xml.read()

my_tree = bs(osm_str, 'lxml')
# print(my_tree)

cnt_has_tag = 0
cnt_hasnt_tag = 0

for node in my_tree.find_all('node'):
    if node.find('tag'):
        cnt_has_tag += 1
    else:
        cnt_hasnt_tag += 1

print(cnt_has_tag, cnt_hasnt_tag)
