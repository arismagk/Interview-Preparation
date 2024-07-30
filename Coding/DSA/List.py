# ---------------------------------Definition-------------------------------------------------------
# An Abstract Data Type (ADT) is a collection with specific (essential) properties and a minimal interface (behavior).
# List is a linear and ordered collection of objects --> In computer science, a list or sequence is
# a collection of items that are finite in number and in a particular order. An instance of a list is a computer
# representation of the mathematical concept of a tuple or finite sequence.
#
# --------------------------------Essential Properties----------------------------------------------
# 1)Orderedness 2) Finiteness
#
# --------------------------------Accidental Properties---------------------------------------------
# 1) Repetitions allowed (orderedness)
#
# --------------------------------Conventions-------------------------------------------------------
# Heterogenous --> Our lists will be nested
# We will implement single linked list (there is also doubly linked list)
#
# --------------------------------Minimal Interface---------------------------------------------
# 1) Create an empty list
# 2) Fuse an element to a list
# 3) Head
# 4) Tail
# --------------------------------Examples-----------------------------------------------------------
# In python lists use the [] annotation but in our implementation we will use the (). () is more common
# In python lists are actually dynamic arrays and not lists. This is actually a misnomer.
# Below some examples:
# (3, 5, 7, 8)
# (1, 5, "i")
# (4)
# (90, 5.65, "a", (32, "y"), ())
# ()
# (())
#
# --------------------------------Interview Questions--------------------------------------------------
# 1) Can you define a linked list inductively (recursively)? --> A list is either an empty list (nil) or a cons of an element (head) and a list (tail, rest).
# 2) What would happen if we drop the finiteness from the definition of list --> Infinite sequences are called streams.
# 3) What is the difference between a list and an array? --> Array consists of elements of same memory size (that can be identified by
#    at least one array index or key). Dynamic array hence is a list but a list is not a dynamic array.
