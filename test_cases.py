# Basic Test Cases

# Test Case 1: Test for n = 0
# Expected Output: 0
assert Fibonacci(0) == 0

# Test Case 2: Test for n = 1
# Expected Output: 1
assert Fibonacci(1) == 1

# Test Case 3: Test for n = 2
# Expected Output: 1
assert Fibonacci(2) == 1

# Edge Test Cases

# Test Case 4: Test for negative input
# Expected Output: 'Incorrect input'
assert Fibonacci(-1) == 'Incorrect input'

# Test Case 5: Test for large input
# Expected Output: Large Fibonacci number
assert Fibonacci(10) == 55