# Algorithm:
# 1. Input the grade.
# 2. If the grade is less than 40, do not round it up.
# 3. Otherwise, calculate the difference between the grade and the next multiple of 5.
# 4. If the difference is less than 3, round the grade up to the next multiple of 5.
# 5. Determine the final grade by comparing it to the following thresholds:
#     * Passing: 40% or higher
#     * Distinction: 80% or higher
# 6. Print the final grade and the student's status.

def round_grade(grade):
  if grade < 40:
    return grade

  next_multiple_of_5 = grade // 5 * 5 + 5
  difference = next_multiple_of_5 - grade

  if difference < 3:
    return next_multiple_of_5

  return grade


def main():
  grade = float(input("Enter the grade: "))
  rounded_grade = round_grade(grade)

  status = "Passed" if rounded_grade >= 40 else "Failed"
  if rounded_grade >= 80:
    status = "Distinction"

  print(f"The rounded grade is {rounded_grade}. The student's status is {status}.")

if __name__ == "__main__":
  main()