import time
start_time = time.time()

s = "ccccccccccccccccabccccabccc"*10000
t = "ab"

# cnt_out = 0
# diap = len(s) - len(t) + 1
# for i in range(diap):
#     if t == s[i:i+len(t)]:
#         cnt_out += 1
# print(cnt_out)

# print("--- %s seconds ---" % (time.time() - start_time))


count,i = 0,0
while s.find(t,i) >= 0:
  pos = s.find(t,i)
  count += 1
  i = pos + 1

print(count)

print("--- %s seconds ---" % (time.time() - start_time))
