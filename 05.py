s = "I am an NLPer"


def ngram(words, N=2):
    d = {}
    for i in range(len(words)):
        if i + N - 1 >= len(words):
            continue
        key = tuple(words[i:i + N])
        if key in d:
            d[key] += 1
        else:
            d[key] = 1

    return d


print(ngram(s))
print(ngram(s.split(" ")))
