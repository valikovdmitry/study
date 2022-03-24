lst = [1,2,3,4,5,6,7,8,9]

d = dict()
for value in lst:
    d[value] = []
    for check in lst:
        sum = value + check
        if sum % 3 != 0 and sum % 5 != 0 and sum % 7 != 0 and value != check:
            d[value].append(check)
print(d)


result = dict()
path = frozenset()


def get_chain_recursive(actual_node_value, path):
    node = dict()
    path_ = path.copy()
    path_.add(actual_node_value)
    for allowed in d[actual_node_value]:
        if allowed not in path_:
            node[allowed] = get_chain_recursive(allowed, path_)
    return node


result[1] = get_chain_recursive(1, set())

print(result)


import json

with open('result.json', 'w') as f:
    json.dump(result, f, indent=4)


# def get_result(node, path):


# TODO: вернуться когда будем проходить рекурсию




