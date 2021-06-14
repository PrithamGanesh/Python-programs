#Lists methods
A = [1,2,3,4,'a','b','c','d']
B = [2,4,6,8,10]

A.append(5)
print(A)

A.extend(B)
print(A)

A.insert(0,0)
print(A)

A.remove(10)
print(A)

A.pop(-1)
print(A)

B.clear()
print(B)

print("Index: ",A.index('a',0,-1))

print("Count: ",A.count(2))

A.reverse()
print(A)

A.copy()
print(A)
