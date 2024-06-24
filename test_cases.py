# Test Case 1
assert is_palindrome("A man, a plan, a canal, Panama") == True, 'Test Case 1 Failed'

# Test Case 2
assert is_palindrome("racecar") == True, 'Test Case 2 Failed'

# Test Case 3
assert is_palindrome("hello") == False, 'Test Case 3 Failed'

# Test Case 4 - Empty string
assert is_palindrome("") == True, 'Test Case 4 Failed'

# Test Case 5 - Single character
assert is_palindrome("a") == True, 'Test Case 5 Failed'

# Test Case 6 - Non-alphanumeric characters
assert is_palindrome("A man, a plan, a canal, Panama!") == True, 'Test Case 6 Failed'

# Test Case 7 - Case sensitivity
assert is_palindrome("Racecar") == True, 'Test Case 7 Failed'