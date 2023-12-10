def merge_list(l1, l2):
    ml = []

# brute force
    i = j = 0
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            ml.append(l1[i])
            i += 1
        else:
            ml.append(l2[j])
            j += 1
    

    while i < len(l1):
        ml.append(l1[i])
        i += 1

    while j < len(l2):
        ml.append(l2[j])
        j += 1

    return ml

l1 = [1, 3, 4, 5]
l2 = [2, 6, 7, 8]

print(merge_list(l1, l2))
