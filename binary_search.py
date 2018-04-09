def bin_search(l, target):
    start = 0
    end = len(l) - 1
    for stuff in range(len(l)):
        middle = (start + end) // 2
        if l[middle] == target:
            return middle
        elif l[middle ] < target:
            start = middle + 1
        elif l[middle] > target:
            end = middle
    return -1