# Test Cases for is_palindrome

def test_is_palindrome():
    assert is_palindrome("A man, a plan, a canal, Panama") == True
    assert is_palindrome("racecar") == True
    assert is_palindrome("hello") == False
    
# Additional edge cases can be added if needed