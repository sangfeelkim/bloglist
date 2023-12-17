
import random
# num = []
# for i in range(0, 46):
#     num.append(i)
# print(num)

# lotto = random.sample(num, 6)
# print(lotto)

num = list(range(1, 46))
lotto = random.sample(num, 7)
sorted_lotto = sorted(lotto[:6]) + lotto[6:]
print(lotto)
print(sorted_lotto)
