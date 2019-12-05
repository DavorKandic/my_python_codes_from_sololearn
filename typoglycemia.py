from random import shuffle as shu
"""Mixes the order of letters in separate words in typed message,
 keeping the order of words and first and last letter"""

def shake_it(msg):
    if len(msg) <= 3:
        return msg
    lst = []
    for ch in msg:
        lst.append(ch)
    start = lst[0]
    end = lst[-1] if lst[-1].isalpha() else lst[-2]
    lst = lst[1:-1]
    tmp = lst[:]
    while True:
        shu(lst)
        if lst != tmp:
            break
    s = ''.join(lst)
    shaked = start + s + end
    return shaked


ans = ''
counter = 0
txt = input("Enter your message:\n")
if txt[-1].isalpha():
    dot = 0
else:
    dot = txt[-1]
lst = txt.split()
for word in lst:
    counter += 1
    shaky = shake_it(word)
    ans += shaky
    if counter < len(lst):
        ans += ' '
if dot != 0:
    ans += dot
print(ans)
