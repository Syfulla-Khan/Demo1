# Basic Test Cases

# Test Case 1: Palindrome string with special characters
assert is_palindrome("A man, a plan, a canal, Panama") == True

# Test Case 2: Non-palindrome string
assert is_palindrome("race a car") == False

# Test Case 3: Palindrome string with spaces and special characters
assert is_palindrome("Was it a car or a cat I saw?") == True