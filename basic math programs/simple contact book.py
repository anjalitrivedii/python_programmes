from scipy.sparse.csgraph import breadth_first_tree

contacts= {}
while True:
    name = input("enter name (or'exit' to quit):")
    if name == 'exit':
        break
    phone = input("enter phone number:")
    contacts[name] = phone
print("Contacts:",contacts)