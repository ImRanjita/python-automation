# Original dictionary
original_dict = {'a': 1, 'b': 2, 'c': 3}

# Swapping keys and values
swapped_dict = {value: key for key, value in original_dict.items()}

# Display the result
print("Original dictionary:", original_dict)
print("Swapped dictionary:", swapped_dict)
