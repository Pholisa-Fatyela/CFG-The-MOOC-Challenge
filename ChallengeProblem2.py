
# Algorithm:

# Read the input array.
# Initialize a variable n to hold the size of the array.
# Start a loop from i = 0 to n-1 (outer loop).
# Within the outer loop, start another loop from j = i+1 to n-1 (inner loop).
# Compare the elements at indices i and j.
# If the element at index j is smaller than the element at index i, swap their positions.
# Repeat steps 5-6 until the inner loop completes.
# Repeat steps 3-7 until the outer loop completes.
# The array is now sorted in ascending order.

def sort_array(array):
  """Sorts an array of distinct integers from smallest to largest.

  Args:
    array: The array to sort.

  Returns:
    The sorted array.
  """

  for i in range(len(array) - 1):
    for j in range(i + 1, len(array)):
      if array[i] > array[j]:
        array[i], array[j] = array[j], array[i]

  return array

def main():
  array = float(input("Enter the list: "))
  print(f"The new list is {array}")



if __name__ == "__main__":
  main()