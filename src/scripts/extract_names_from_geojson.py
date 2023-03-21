from json import load

path_to_file = './export.geojson'
new_file_name = './bairros.txt'

with open(path_to_file) as f1:
    json_data = load(f1)
    lst = []

    for i in json_data['features']:
        i = i.get('properties').get('name')
        if i is not None:
            lst.append(i)

    with open(new_file_name, 'w') as f2:
        for item in lst:
            f2.write(item+'\n')