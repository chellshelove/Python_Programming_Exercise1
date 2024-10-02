# Get input strings from the user
first_string = input("Enter the first string: ")
second_string = input("Enter the second string: ")

# Initialize an empty list to store indexes
indexes = []

# Search for all occurrences of the second string in the first string
start = 0
while True:
    # Find the next occurrence of the second string
    index = first_string.find(second_string, start)
    
    # If found, add the index to the list
    if index != -1:
        indexes.append(index)
        # Move the start point for the next search
        start = index + 1
    else:
        break

# Print the indexes if any are found, otherwise print -1
if indexes:
    print(*indexes)  # Unpack the list to print all indexes
else:
    print(-1)