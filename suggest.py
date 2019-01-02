from bisect import bisect_left

file = open('processed.txt')
w_list = []
freq_list = []

for i in file:
    tup = i.split(' ')
    w_list.append(tup[0])
    freq_list.append(int(tup[1]))


def binary_search(word, low=0, high=None):  # find index of first occurrence of word
    if high is None:
        high = len(w_list) - 1

    mid = int((low + high) / 2)

    if low == high:
        if w_list[mid][:len(word)] == word:
            return low
        else:
            return -1
    elif low > high:
        return -1

    if w_list[mid][:len(word)] == word and w_list[mid - 1][:len(word)] < word:
        return mid

    elif w_list[mid][:len(word)] >= word:
        high = mid - 1
    else:
        low = mid + 1
    return binary_search(word, low, high)


def suggest(word, i):
    ind = binary_search(word)

    suggestion_list = []
    count = 0
    while ind < len(w_list) and w_list[ind][:len(word)] == word:
        suggestion_list.append(ind)
        ind += 1
    suggestion_list = sorted(suggestion_list, key=lambda x: freq_list[x])
    suggestion_list = suggestion_list[:i]
    suggestions = []
    for i in suggestion_list:
        suggestions.append(w_list[i])
    return suggestions
