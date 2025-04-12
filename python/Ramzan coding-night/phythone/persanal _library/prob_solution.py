# 🚀 1. Find Second Largest Number in a List
# Explanation:

# Pehle list ko unique banayenge (duplicate values hata denge).
# Phir us list ko descending order mein sort karenge.
# Second element ko return karenge.
def second_largest(numbers):
    unique_numbers = list(set(numbers))  # Duplicate values hata diye
    unique_numbers.sort(reverse=True)  # Descending order mein sort kiya
    return unique_numbers[1] if len(unique_numbers) > 1 else None  # Second largest return kiya

# Example
nums = [10, 20, 4, 45, 99, 99, 20]
print("Second Largest:", second_largest(nums))  # Output: 45

# 🚀 2. Check If a String is a Palindrome
# Explanation:

# Ek string palindrome hoti hai agar uska reverse bhi wahi ho.
# Simple comparison string == string[::-1] se check kar sakte hain.

def is_palindrome(s):
    return s == s[::-1]  # Reverse check

# Example
word = "madam"
print(f"Is '{word}' a palindrome?", is_palindrome(word))  # Output: True

# 🚀 3. Find Factorial Using Recursion
# Explanation:

# Factorial n! = n * (n-1)! hota hai.
# Recursion ka istemal karke factorial(n-1) call karenge.
# Base case: Jab n == 0 or n == 1 ho, to return 1 karenge.

def factorial(n):
    if n == 0 or n == 1:  # Base case
        return 1
    return n * factorial(n - 1)  # Recursive call

# Example
num = 5
print(f"Factorial of {num}:", factorial(num))  # Output: 120
