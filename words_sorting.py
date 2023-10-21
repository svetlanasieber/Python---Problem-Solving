import os

def words_sorting(*args):
    dictionary = {}
    for word in args:
        dictionary[word] = 0
    for word in dictionary:
        for ch in word:
            dictionary[word] += ord(ch)
    result = []
    if sum(dictionary.values()) % 2 == 0:
        for key, value in sorted(dictionary.items(), key=lambda x: x[0]):
            result.append(key + ' - ' + str(value))
    else:
        for key, value in sorted(dictionary.items(), key=lambda x: -x[1]):
            result.append(key + ' - ' + str(value))
    return os.linesep.join(result)