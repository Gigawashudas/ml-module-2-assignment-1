


def find_duplicates(list):
    duplicates = []
    for item in list:
        if list.count(item) > 1 and item not in duplicates:
            duplicates.append(item)
    return duplicates

list = [1, 5, 6, 5, 1, 2, 3]
print("Original list:", list)
duplicates = find_duplicates(list)
print("Duplicates in the list:", duplicates)