from bs4 import BeautifulSoup as bs

with open('map2.osm', 'r', encoding='utf-8') as osm_xml:
    osm_str = osm_xml.read()

my_tree = bs(osm_str, 'lxml')
fuel_station_cnt = 0
for node in my_tree.find_all('node'):
    if node.tag:
        if node.tag['k'] == 'amenity' and node.tag['v'] == 'fuel':
            fuel_station_cnt += 1
print(fuel_station_cnt)
