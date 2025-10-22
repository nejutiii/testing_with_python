num = int(input("Enter a number: "))

print(f"\nOriginal: {num} -> {bin(num)}")


left = num << 1
print(f"Left shift (num << 1): {left} -> {bin(left)}")


right = num >> 1
print(f"Right shift (num >> 1): {right} -> {bin(right)}")
