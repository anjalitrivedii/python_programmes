from collections import defaultdict


def number_to_string(argument):
    match argument:
        case 0:
            return "zero"
        case 1:
            return "one"
        case 2:
            return "two"
        case default :
            return "something"
head = number_to_string(0)
print(head)