from src.utils import json_operation




if __name__ == '__main__':
    #turne = json_operation("../data/operations.json")
    data = "../data/json_string_03.json"
    turne = json_operation(data)
    print(turne)
    print(type(turne))