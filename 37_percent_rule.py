#github test: origin -> master (github -> local)

from random import random

a = [None] * 100
max_num = 0
all_max = 0
#look
for i in range(100):
    a[i] = int((100 * random()))
    if all_max < a[i]:
        all_max = a[i]
    if i < 37 and max_num < a[i]:
        max_num = a[i]
#leap
for j in range(37, 100):
    if max_num < a[j]:
        max_num = a[j]
        print("stopped at: ", j)
        break
print("Look then leap max is: ", max_num)
print("The actual max is: ", all_max)
print(a)
