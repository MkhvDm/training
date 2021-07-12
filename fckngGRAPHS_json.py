import json

input_json = json.loads('[ {"name": "D", "parents": ["B"]}, {"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]')
print(input_json)
print('START...')

parents = []
tmp = []
for obj in input_json:
    tmp.append(obj["name"])
    for obj_2 in input_json:
        if obj["name"] in obj_2["parents"]:
            tmp.append(obj_2["name"])
    parents.append(tmp)
    tmp = []

parent_dict = {}
for i in parents:
    parent_dict.update({i[0]:i[1:]})

childs_set = set()
def allchilds (parent):
    print('allchilds_start...', parent)
    global childs_set
    print(parent_dict.get(parent))
    for ch in parent_dict.get(parent):
        childs_set.add(ch)
        allchilds(ch)
    print('return:', childs_set)
    return list(childs_set)

out_stat = {}
out_list = []
for parent in parent_dict.keys():
    childs_set = set()
    out_stat.update({parent:len(allchilds(parent))+1})
    out_list.append(str(parent +" : "+ str(out_stat.get(parent))))
    print('_____', out_stat)
out_list.sort()
print(*out_list, sep='\n')




