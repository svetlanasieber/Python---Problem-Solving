def start_spring(**kwargs):
    dic = {}
    for flower, type_flower in kwargs.items():
        if type_flower not in dic.keys():
            dic[type_flower] = []
        dic[type_flower].append(flower)
    result = []
    for t, f in sorted(dic.items(), key=lambda x: (-len(x[1]), x[0])):
        result.append(f'{t}:')
        for current_f in sorted(f):
            result.append(f'-{current_f}')
    return '\n'.join(result)


example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}
print(start_spring(**example_objects))