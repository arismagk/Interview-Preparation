# --------------------------------------Theory-------------------------------------------------------------------------
# A hash table is a data structure that maps keys to values (associative array) for highly efficient lookup.
# A hash table can be implemented either with a Linked List or with a balanced binary tree.

# Linked List: Look up worst case is O(N) (if there is a high number of collisions) but assuming a good
# implementation that keeps collisions to minimum, gives an amortized look up time of O(1).

# Balanced binary tree: Look up time is O(log N) but this gives us the advantage of potentially allocating less space
# since we are not allocating a large array anymore.

# A load factor "a" is a critical statistic of a hash table and is defined as follows:
# load factor (a) = n / m, where n is the number of entries occupied in the hash table and
# m is the number of buckets

# Some theoretical computer science behind it...
# A hash function h:U -> {0,...,m-1} maps the universe U of keys to indices or slots within the table.
# A hash function is said to be perfect for a given set S if it is injective (one to one relation) on S, that is that
# for each elements on S there is exactly one value in 0,...,m-1

# Interesting concepts related to hash tables
# Space-time tradeoff: A case where an algorithm or program trades increased space usage with decreased time.
# Here, space refers to the data storage consumed in performing a given task (RAM, HDD, etc.), and time refers
# to the time consumed in performing a given task (computation time or response time).

# --------------------------------------Practice-------------------------------------------------------------------------

# Implementation with linked list

def compute_hash_code(key):
    key = ''.join(str(ord(c)) for c in key)
    return int(key) % 13


