def merge_dicts(dict1 , dict2):
    dict1.update(dict2)
    return dict1
print(merge_dicts({'a':1,'b':2} , {'c':3,'d':4}))