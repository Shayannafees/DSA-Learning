# Create an array with 100 strings
array = ["string_" + str(i) for i in range(100)]

# Generate simple hash values for each item in the array
hash_values = []
for item in array:
    hash_value = sum(ord(char) for char in item)  # Simple hash: sum of ASCII values
    hash_values.append(hash_value)

# Output the results
print("Original Strings and Their Hash Values:\n")
for original, hash_value in zip(array, hash_values):
    print(f"String: {original} -> Hash: {hash_value}")
