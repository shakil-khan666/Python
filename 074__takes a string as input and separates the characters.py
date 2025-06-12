# Input from user
input_string = input("Enter a string: ")

# Initialize variables before using
upper_case = ""
lower_case = ""
digit = ""
other = ""

# Loop through each character
for char in input_string:
    if char.isupper():
        upper_case += char
    elif char.islower():
        lower_case += char
    elif char.isdigit():
        digit += char
    else:
        other += char

# Output (use correct variable names)
print("Uppercase letters:", upper_case)
print("Lowercase letters:", lower_case)
print("Digits:", digit)
print("Other characters:", other)

        
        