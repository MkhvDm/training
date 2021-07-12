s = 'ccAcc'
a = 'cAc'
b = 'cAc'

# s, a, b = input(), input(), input()

cnt = 0
if a not in s:
    print(cnt)
else:
    while a in s:
        if a in b or cnt > 1000:
            cnt = 0
            break
        count_before = s.count(a)
        s = s.replace(a, b, s.count(a))
        if (s.count(a) >= count_before):
            break
        cnt += 1
    print(cnt if cnt else 'Impossible')


