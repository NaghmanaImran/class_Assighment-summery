# count = 1

# while count <= 3 :
#     print("pakistan")
#     count += 1
# iftar_items: list = ["khajur","samosa","roohafza","pakore",]
# for items in iftar_items:
#     print(items)

# def items(*n):
#      print(n)

# items(1,2,3,4,5)
# def items(*n):
#     sum = 0
#     for items in n:
#         sum += items
#     print(sum)
# items(2,3,5,6)

# 🔹 is Operator:
# Used for identity comparison (checks if two variables point to the same memory location).
# Example:
# python
# Copy
# Edit

a = [1, 2, 3]
b = a
print(a is b)  # True (same memory reference)

c = [1, 2, 3]
print(a is c)  # False (different memory reference)

# 🔹 in Operator:
# Used for membership testing (checks if a value exists in a sequence like list, tuple, or string).
# Example:
# python
# Copy
# Edit

numbers = [1, 2, 3, 4, 5]
print(3 in numbers)  # True (3 is in the list)

text = "Hello Python"
print("Python" in text)  # True ("Python" is in the string)

