
a = [1, 2, 3]
b = a 

print("a is b:", a is b)         
print("a is not b:", a is not b) 
print("id(a):", id(a))
print("id(b):", id(b))
print()


x = [1, 2, 3]
y = [1, 2, 3]

print("--- Example 2: Equal Values, Different Objects ---")
print("x == y:", x == y)          # True (values are equal)
print("x is y:", x is y)          # False (different memory locations)
print("x is not y:", x is not y)  # True
print("id(x):", id(x))
print("id(y):", id(y))
print()


# 3. Checking None (best practice use case for 'is')
result = None

print("--- Example 3: Checking None ---")
print("result is None:", result is None)          # True
print("result is not None:", result is not None)  # False