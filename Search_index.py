n = [1,2,3,4,5]
k = 1
for i in range(len(n)):
    if n[i] == k:
       print(f"{k} appears at index {i}")
else:
    print("not Present")