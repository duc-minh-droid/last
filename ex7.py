lst = [5, 1, 8, 92, -1, 30]
print(f"Original list\n{lst}")

def find_min(l):
    min1 = l[0]
    for i in range(len(l)):
        if l[i] < min1:
            min1 = l[i]
    return min1

sorted_lst = []

for i in range(len(lst)):
    min = find_min(lst)
    sorted_lst.append(min)
    lst.remove(min)
    
print(f"Sorted list\n{sorted_lst}" )