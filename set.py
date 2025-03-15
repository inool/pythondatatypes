# Creating sets
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

# 1. Set copy - making a copy of a set
set_c = set_a.copy()
print("Copy of set_a:", set_c)

# 2. Discarding an element (does not raise an error if element is not present)
set_a.discard(3)
print("set_a after discarding 3:", set_a)

# 3. Pop an element (removes and returns an arbitrary element)
popped_element = set_a.pop()
print(f"Element popped from set_a: {popped_element}")
print("set_a after popping an element:", set_a)

# 4. Clearing all elements from a set
set_b.clear()
print("set_b after clearing all elements:", set_b)

# 5. Subset and Superset checks
set_d = {1, 2}
print("Is set_d a subset of set_a?", set_d.issubset(set_a))
print("Is set_a a superset of set_d?", set_a.issuperset(set_d))
# 6. Set equality
set_e = {1, 2, 4, 5}
print("Is set_a equal to set_e?", set_a == set_e)

# 7. Set symmetric difference (elements in either set but not in both)
set_f = {5, 6, 7}
symmetric_diff = set_a.symmetric_difference(set_f)
print("Symmetric difference between set_a and set_f:", symmetric_diff)

# 8. Set difference update (updates the set by removing elements found in the second set)
set_a.difference_update(set_f)
print("set_a after difference_update with set_f:", set_a)

# 9. Intersection update (modifies set_a to keep only elements found in both sets)
set_a.intersection_update(set_e)
print("set_a after intersection_update with set_e:", set_a)

# 10. Set Comprehension - Squares of numbers
squares_set = {x**2 for x in range(1, 6)}
print("Set of squares of numbers from 1 to 5:", squares_set)

# 11. Adding multiple elements (using update method)
set_a.update([9, 10, 11])
print("set_a after updating with multiple elements:", set_a)
