def remove_duplicate_list(list):
    if len(list) == 0:
        return []
    visited = set()
    new_list = []
    i = 0

    # brute force
    while i < len(list):
        if list[i] not in visited:
            visited.add(list[i])
            new_list.append(list[i])
        i += 1

    return new_list

print(remove_duplicate_list([1, 3, 3, 2, 5, 6, 8, 9, 5, 2]))
