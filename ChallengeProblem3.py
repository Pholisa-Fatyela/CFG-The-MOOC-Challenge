# In this simplified version, we use a loop to iterate over each row in the matrix. Within the loop, we check if the target number is present in the current row. If it is found, we retrieve the column index of the target and return the location [row index, column]. If the loop completes without finding the target, we return the message "Number not found in the matrix."

# The flowchart reflects this simplified pseudocode. It starts by checking if the matrix is empty and returns the corresponding message if true. Otherwise, it iterates over each row in the matrix and checks if the target is present in the current row. If found, it retrieves the column index and returns the location. If the target is not found in any row, it returns the message indicating that the number is not in the matrix. Finally, the flowchart reaches the end after returning the result or the message.


# Solution 1
def search_in_sorted_matrix(matrix, target):
    if not matrix:
        return "Matrix is empty."

    rows = len(matrix)
    cols = len(matrix[0])

    # Start from the top-right element
    row = 0
    col = cols - 1

    while row < rows and col >= 0:
        current = matrix[row][col]
        if current == target:
            return [row, col]
        elif current < target:
            row += 1
        else:
            col -= 1

    return "Number not found in the matrix."


# Example matrix
matrix = [
    [1, 4, 7, 12, 15, 1000],
    [2, 5, 19, 31, 32, 1001],
    [3, 8, 24, 33, 35, 1002],
    [40, 41, 42, 44, 45, 1003],
    [99, 100, 103, 106, 128, 1004]
]

# Example target number
target = 44

# Search for the target number in the matrix
result = search_in_sorted_matrix(matrix, target)

# Print the result
print(result)


# Solution 2
# function search_in_sorted_matrix(matrix, target):
#     if the matrix is empty:
#         return "Matrix is empty."
    
#     for each row in the matrix:
#         if the target number is in the current row:
#             find the column index of the target in the row
#             return the location [row index, column index]
    
#     return "Number not found in the matrix."