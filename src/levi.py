import itertools

def leviDistance(word1:str, word2:str):
    # # creating 2d array
    cache = [[float("inf")] * (len(word2) + 1) for _ in range(len(word1) + 1)]

    for i, j in itertools.product(range(len(word1) + 1), range(len(word2) + 1)):
        if min(i, j) == 0:
            cache[i][j] = float(max(i, j))
        else:
            lev = lambda i, j: cache[i][j]

            t1 = lev(i-1, j) + 1
            t2 = lev(i, j-1) + 1
            t3 = lev(i-1, j-1) + [2, 0][word2[j-1] == word1[i-1]]

            cache[i][j] = min(t1, t2,t3)

    return int(cache[len(word1)][len(word2)])


ld = leviDistance("Back", "Book")
def leviRatio(w1, w2):
    d = leviDistance(w1, w2)
    # l = max(len(w1), len(w2))
    l = len(w1) + len(w2)
    return {
        'word1' : w1,
        'word2' : w2,
        'ratio' : 1 - (d/l),
        'distance' : d
    }

print(leviRatio("cat", "bat"))