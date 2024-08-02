def flatten(nested_list, depth=0):
    flat_list = []
    max_depth = depth

    for item in nested_list:
        if isinstance(item, list):
            sublist, subdepth = flatten(item, depth + 1)
            flat_list.extend(sublist)
            max_depth = max(max_depth, subdepth)
        else:
            flat_list.append(item)

    return flat_list, max_depth


nested_list = [1, [2, [3, 4], 5], [6, 7]]
result = flatten(nested_list)
print(result)  
