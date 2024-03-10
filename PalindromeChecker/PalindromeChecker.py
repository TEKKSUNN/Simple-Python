""" PALINDROME CHECKER IN PYTHON """

def is_palindrome(strng : str):
    rev_string = strng[::-1]
    if rev_string == strng:
        return True
    return False

print("*** Welcome to Palindrome Checker ***")
word = str(input("Enter your string: "))
print("\n\n*** RESULT ***\n")
result = is_palindrome(word)
if result == True:
    print(f"\"{word}\" is a Palindrome.")
else:
    print(f"\"{word}\" is not a Palidrome.")
