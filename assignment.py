# assignment_operators.py
# A complete guide combining all Python assignment operators

print("--- 1. Basic Assignment ---")
x = 10  # Assigns the value 10 to variable x
print(f"Initial x = {x}\n")

print("--- 2. Arithmetic (Compound) Assignment Operators ---")
x += 3  # Equivalent to: x = x + 3
print(f"After x += 3:  {x}")

x -= 2  # Equivalent to: x = x - 2
print(f"After x -= 2:  {x}")

x *= 4  # Equivalent to: x = x * 4
print(f"After x *= 4:  {x}")

x /= 3  # Equivalent to: x = x / 3 (results in a float)
print(f"After x /= 3:  {x}")

x %= 5  # Equivalent to: x = x % 5 (remainder of division)
print(f"After x %= 5:  {x}")

x //= 2  # Equivalent to: x = x // 2 (floor division)
print(f"After x //= 2: {x}")

x **= 3  # Equivalent to: x = x ** 3 (exponent / power)
print(f"After x **= 3: {x}\n")

print("--- 3. Bitwise Assignment Operators ---")
# Resetting x to an integer for bitwise operations
x = 5  # Binary: 0101

x &= 3  # Equivalent to: x = x & 3 (Bitwise AND with 0011)
print(f"After x &= 3:  {x}")

x |= 4  # Equivalent to: x = x | 4 (Bitwise OR with 0100)
print(f"After x |= 4:  {x}")

x ^= 2  # Equivalent to: x = x ^ 2 (Bitwise XOR with 0010)
print(f"After x ^= 2:  {x}")

x >>= 1  # Equivalent to: x = x >> 1 (Right shift by 1 bit)
print(f"After x >>= 1: {x}")

x <<= 2  # Equivalent to: x = x << 2 (Left shift by 2 bits)
print(f"After x <<= 2: {x}\n")

print("--- 4. Walrus Operator (Assignment Expression) ---")
# Introduced in Python 3.8: Assigns a value within an expression
if (n := len("Python")) > 5:
    print(f"The string length is {n}, which is greater than 5.")