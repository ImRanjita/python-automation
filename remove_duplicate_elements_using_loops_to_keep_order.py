# Get user input
user_input = input("Enter items separated by commas: ")

# Convert to list and clean spaces
items = [item.strip() for item in user_input.split(',')]

# Use loop to keep only first occurrences
unique_items = []
for item in items:
    if item not in unique_items:
        unique_items.append(item)

# Calculate duplicates removed
duplicates_removed = len(items) - len(unique_items)

print("\nCleaned List (order preserved):", unique_items)
print("Duplicates Removed:", duplicates_removed)
