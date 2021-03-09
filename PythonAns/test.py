from string import ascii_lowercase

dic = {}
for c in ascii_lowercase:
    dic[c] = ord(c) - ord("a")
print(dic)
print(ord("a"))
print(ord("ab"))
print(ord("abc"))