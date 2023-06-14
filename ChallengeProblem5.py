# Pseudocode:

# Generate a random credit card number with 16 digits and store it in a variable.
# Create an empty string variable called "hiddenCardNumber".
# Iterate through each digit in the credit card number using a loop.
# If the current digit's index is less than 12, append "X" to the hiddenCardNumber.
# If the current digit's index is greater than or equal to 12, append the digit to the hiddenCardNumber.
# If the current digit's index is divisible by 4 (excluding 0), append a space character to the hiddenCardNumber.
# Repeat steps 4-6 for each digit in the credit card number.
# Print the hiddenCardNumber.

import random

# Step 1: Generate a random credit card number with 16 digits
credit_card_number = str(random.randint(10**15, 10**16 - 1))

# Step 2: Initialize hiddenCardNumber
hidden_card_number = ""

# Step 3: Iterate through each digit in the credit card number
for i in range(len(credit_card_number)):
    # Step 4: Check if the current digit's index is less than 12
    if i < 12:
        # Step 5: Append "X" to hiddenCardNumber
        hidden_card_number += "X"
    else:
        # Step 5: Append the digit to hiddenCardNumber
        hidden_card_number += credit_card_number[i]
    
    # Step 6: Check if the current digit's index is divisible by 4 (excluding 0)
    if (i + 1) % 4 == 0 and i < 15:
        # Step 6: Append a space character to hiddenCardNumber
        hidden_card_number += " "

# Step 7: Print hiddenCardNumber
print(hidden_card_number)
