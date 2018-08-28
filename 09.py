import numpy as np


def f(s):
    words = s.split(" ")
    r = ""
    for word in words:
        if len(word) < 3:
            r += word + " "
        else:
            subword = [c for c in word[1:-1]]
            np.random.shuffle(subword)
            r += word[0] + "".join(subword) + word[-1] + " "
    return r


s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

print(f(s))
