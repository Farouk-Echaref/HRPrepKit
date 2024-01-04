# Python Containers: (List, Tuple, Set, Dictionary):

## Set:
* Main benefit of sets is the fact that time complexity of add, remove, contains are all **constant time** operations.

* In CPython, which is the default and most widely used implementation of the Python programming language, **sets** are internally implemented using a structure similar to **dictionaries**. **Dictionaries** in Python are data structures that consist of **key-value** pairs. In the case of sets, **the keys are the members (elements) of the set**, and there is no need for associated values. This is because sets are inherently unordered collections of unique elements.

* The **implementation of sets as dictionaries with dummy values means that each element in the set is essentially a key in the underlying dictionary, and the associated values are not significant**. The use of "dummy values" implies that the values associated with these keys are not used or don't carry meaningful information; they might exist only to satisfy the requirements of the dictionary data structure.

* The optimization mentioned in the statement likely refers to the fact that this implementation takes advantage of the fact that sets only require unique elements and don't have any associated values. By using a dictionary-like structure without the need for meaningful values, CPython can optimize certain operations and make the implementation more efficient for set-specific operations.

* So basically a **set** uses a **hashtable** as its underlying data structure. This explains the **O(1)** membership checking, since looking up an item in a hashtable is an **O(1)** operation, on average.

* Note: Nowadays, set and dict's implementations have diverged significantly, so the precise behaviors (e.g. arbitrary order vs. insertion order) and performance in various use cases differs; they're still implemented in terms of hashtables, so average case lookup and insertion remains O(1), but set is no longer just "dict, but with dummy/omitted values".