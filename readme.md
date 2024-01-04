# Python Containers: (List, Tuple, Set, Dictionary):

## Set:
* Main benefit of sets is the fact that time complexity of add, remove, contains are all **constant time** operations.

* In CPython, which is the default and most widely used implementation of the Python programming language, **sets** are internally implemented using a structure similar to **dictionaries**. **Dictionaries** in Python are data structures that consist of **key-value** pairs. In the case of sets, **the keys are the members (elements) of the set**, and there is no need for associated values. This is because sets are inherently unordered collections of unique elements.

* The **implementation of sets as dictionaries with dummy values means that each element in the set is essentially a key in the underlying dictionary, and the associated values are not significant**. The use of "dummy values" implies that the values associated with these keys are not used or don't carry meaningful information; they might exist only to satisfy the requirements of the dictionary data structure.

* The optimization mentioned in the statement likely refers to the fact that this implementation takes advantage of the fact that sets only require unique elements and don't have any associated values. By using a dictionary-like structure without the need for meaningful values, CPython can optimize certain operations and make the implementation more efficient for set-specific operations.