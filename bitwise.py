# python_bitwise_demo.py

# Define two integers for demonstration
x = 10  # Binary: 1010
y = 4   # Binary: 0100

print(f"Base Values:")
print(f"x = {x} (Binary: {bin(x)[2:].zfill(4)})")
print(f"y = {y} (Binary: {bin(y)[2:].zfill(4)})\n")
print("-" * 40)

# 1. Bitwise AND (&)
# Sets each bit to 1 if both bits are 1
and_result = x & y
print(f"1. Bitwise AND (&): {x} & {y} = {and_result}")
print(f"   {bin(x)[2:].zfill(4)} & {bin(y)[2:].zfill(4)} -> {bin(and_result)[2:].zfill(4)}\n")

# 2. Bitwise OR (|)
# Sets each bit to 1 if at least one of the bits is 1
or_result = x | y
print(f"2. Bitwise OR (|): {x} | {y} = {or_result}")
print(f"   {bin(x)[2:].zfill(4)} | {bin(y)[2:].zfill(4)} -> {bin(or_result)[2:].zfill(4)}\n")

# 3. Bitwise XOR (^)
# Sets each bit to 1 only if one of the bits is 1 (but not both)
xor_result = x ^ y
print(f"3. Bitwise XOR (^): {x} ^ {y} = {xor_result}")
print(f"   {bin(x)[2:].zfill(4)} ^ {bin(y)[2:].zfill(4)} -> {bin(xor_result)[2:].zfill(4)}\n")

# 4. Bitwise NOT (~)
# Inverts all the bits (Formula: ~x = -x - 1)
not_result = ~x
print(f"4. Bitwise NOT (~): ~{x} = {not_result}")
print(f"   ~({bin(x)[2:].zfill(4)}) -> {bin(not_result)}\n")

# 5. Bitwise Left Shift (<<)
# Shifts bits to the left by pushing zeros in from the right
left_shift = x << 2
print(f"5. Bitwise Left Shift (<<): {x} << 2 = {left_shift}")
print(f"   {bin(x)[2:].zfill(4)} << 2 -> {bin(left_shift)[2:]}\n")

# 6. Bitwise Right Shift (>>)
# Shifts bits to the right by removing the rightmost bits
right_shift = x >> 2
print(f"6. Bitwise Right Shift (>>): {x} >> 2 = {right_shift}")
print(f"   {bin(x)[2:].zfill(4)} >> 2 -> {bin(right_shift)[2:].zfill(4)}")