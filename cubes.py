from lxml import etree


# root = etree.fromstring(input())

tree = etree.parse('tmp_xml.xml')
root = tree.getroot()

prices = {'red': 0, 'green': 0, 'blue': 0}
def get_childs(parent, deep=1):
    if parent.getchildren() != []:
        print('Tag:', parent.tag, '\tAttrib:', parent.attrib['color'], '\t', deep)
        prices[parent.attrib['color']] += deep
        for child in parent:
            get_childs(child, deep + 1)
    else:
        prices[parent.attrib['color']] += deep
        print('Tag:', parent.tag, '\tAttrib:', parent.attrib['color'], '\t', deep)

get_childs(root)
print(*prices.values())
