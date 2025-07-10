# Get user input
user_input = input("Enter items separated by commas: ")

# Convert to list and clean spaces
items = [item.strip() for item in user_input.split(',')]

# Use set to remove duplicates
unique_items = list(set(items))

# Calculate duplicates removed
duplicates_removed = len(items) - len(unique_items)

print("\nCleaned List (unordered):", unique_items)
print("Duplicates Removed:", duplicates_removed)
