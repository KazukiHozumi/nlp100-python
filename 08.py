def ciper(s):
    r = ""
    for c in s:
        n = ord(c)
        if n >= ord("a") and n <= ord("z"):
            r+=(chr(219 - n))
        else:
            r+=c
    return r


s = "Hello youtube"
c = ciper(s)
r = ciper(c)
print(s)
print(c)
print(r)
