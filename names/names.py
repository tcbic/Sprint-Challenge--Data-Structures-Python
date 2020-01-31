import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# ORIGINAL SOLUTION
# Time complexity: O(n^2) --> double for loop
# runtime ~ 11 seconds

# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# Implement binary search to improve runtime...

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree.
    def insert(self, value):
        # Start at the root node which is represented by self.value.
        # Check if the value is less than the current node.
        if value < self.value:
            # See if there is a value on the left.
                # If there is not a value on the left...
                if self.left is None:
                # Create a new node in that position.
                    self.left = BinarySearchTree(value)
                else:
                    # We need to repeat. Best way to do this is recursion.
                    self.left.insert(value)
        else:
            # Repeat the same logic as above except for the right side.
            # If it's not less than we know the value is greater.
                if self.right is None:
                    self.right = BinarySearchTree(value)
                else:
                    self.right.insert(value)

    # Return True if the tree contains the value, and
    # False if it does not.
    def contains(self, target):
        # If the target is equal to the root node, return True.
        if target == self.value:
            return True
        # If the target is smaller, go left.
        elif target < self.value:
            # If there is no value to the left.
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

duplicates = []

bst = BinarySearchTree(names_1[0])
for name_1 in names_1:
    bst.insert(name_1)
for name_2 in names_2:
    if bst.contains(name_2):
        # Append name to dupliccates list.
        duplicates.append(name_2)

# The runtime is now less than a second.

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?