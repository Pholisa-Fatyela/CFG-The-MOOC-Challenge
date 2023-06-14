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