def overlap(a, b):
    al, ar = a['positions']
    bl, br = b['positions']
    min_len = min(ar - al, br - bl)
    intersect = max(0, min(ar, br) - max(al, bl))
    return intersect >= (min_len / 2)

def combine_lists(list1, list2):
    result = []
    i, j = 0, 0

    while i < len(list1) and j < len(list2):
        if overlap(list1[i], list2[j]):
            combined = {
                "positions": list1[i]['positions'],
                "values": list1[i]['values'] + list2[j]['values']
            }
            result.append(combined)
            i += 1
            j += 1
        elif list1[i]['positions'][0] < list2[j]['positions'][0]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1

    result.extend(list1[i:])
    result.extend(list2[j:])
    return result


list1 = [{"positions": [0, 5], "values": [1]}]
list2 = [{"positions": [3, 8], "values": [2]}]
print(combine_lists(list1, list2))
