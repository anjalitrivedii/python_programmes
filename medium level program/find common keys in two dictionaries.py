def common_keys(dict1 ,dict2):
    return dict1.keys() & dict2.keys()
print(common_keys({'a':1,'b':2},{'b':3,'c':4}))
