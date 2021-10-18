import array
import numpy as np
from sys import getsizeof


###############################################################################
#  EXAMPLES OF THE ARRAY LIBRARY AND NUMPY ARRAYS.
###############################################################################

my_python_array = array.array('i')  # creates empty array of integers
my_python_array.append(10)  # Add values to the array one at a time.
my_python_array.append(9)
my_python_array.append(8)
my_python_array.append(7)
my_python_array.append(5)

print(f"my_python_array[0] = {my_python_array[0]}")  # Access the elements by their index.
print(f"my_python_array[4] = {my_python_array[4]}")  # Access the elements by their index.

my_python_array[0] = 100   # Change Values by index.
print(f"my_python_array[0] = {my_python_array[0]}")  # Access the elements by their index.

y = array.array('i', [10, 9, 8, 7, 5])  # creates an initialized array
print(f"Initialized Array: {y}")

############################
# NUMPY
############################

# SAMPLE CREATION OF NUMPY ARRAY
my_numpy_array = np.array([10, 9, 8, 7, 5])  # INITIALIZE A NUMPY ARRAY

# ACCESS THE ELEMENTS BY THEIR INDEX.
for i in range(0, my_numpy_array.size):
    print(f"my_numpy_array[{i}] = {my_numpy_array[i]}")

# Change values by index
print("Before Change:")
print(f"my_numpy_array[3] = {my_numpy_array[3]}")
my_numpy_array[3] = 10
print("After Change:")
print(f"my_numpy_array[3] = {my_numpy_array[3]}")

# CREATING A MULTI-DIMENSIONAL NP ARRAY
r1 = [1, 2, 3]
r2 = [4, 5, 6]
my_2d_array = np.array([r1, r2])
print(my_2d_array)

# ACCESS BY ROW THEN COLUMN
print(f"Row: 0, Column: 2 = {my_2d_array[0][2]}")

# JAGGED ARRAYS (ARRAYS WITH ROWS OF DIFFERENT LENGTHS
r1_short = np.array([1, 2, 3])   # INPUTS SHOULD BE NP ARRAYS NOT LISTS
r2_long = np.array([4, 5, 6, 7])
my_jagged_array = np.array([r1_short, r2_long], dtype="object")  # NEED TO SET DATATYPE

print("Implemented as an array of arrays:")
print(my_jagged_array)

# PERFORMING MATH ON NUMPY ARRAYS (SYNTACTIC SUGAR, BUT FAST IMPLEMENTATION TOO)
print(my_2d_array)
print("Times Two:")
print(my_2d_array * 2)
print("Element Wise Squared:")
print(my_2d_array ** 2)
print("Even works on arrays of arrays:")
print(my_jagged_array)
print("Times Two:")
print(my_jagged_array * 2)

# COMPARING MEMORY FOOTPRINT OF DIFFERENT ARRAY TYPES, PYTHON ARRAY, NUMPY ARRAY AND PYTHON LIST.

ARRAY_SIZE = 1000
array_data = np.linspace(1, ARRAY_SIZE, ARRAY_SIZE, dtype=int)

# CREATE A NEW ARRAYS
my_big_python_array = array.array('i', array_data)
my_big_numpy_array = np.array(array_data)
my_big_list = my_big_numpy_array.tolist()

# COMPARE THE SIZES OF THE ARRAYS
print(f" Array Size: {getsizeof(my_big_python_array)} bytes for {ARRAY_SIZE} elements.")
print(f" Numpy Array Size: {getsizeof(my_big_numpy_array)} bytes bytes for {ARRAY_SIZE} elements..")
print(f" List Size: {getsizeof(my_big_list)} bytes bytes for {ARRAY_SIZE} elements.")


###############################################################################
#  BASIC NODE INTRODUCTIONS, A BASIC NODE, AND A MAP NODE AND SOME SAMPLE CODE
###############################################################################
class BasicNode:
    """
    Introduction to a node object.  Simple objeft that contains some data and a single
    link to another node.
    """
    def __init__(self, data=None, link=None):
        self.data = data
        self.link = link


# CREATING BASIC NODES AND LINKING THEM TOGETHER
n1 = BasicNode("Hello")
n2 = BasicNode("World")
n1.link = n2

print(f"{n1.data}, {n1.link.data}")

# DEMONSTRATION OF POINTERS, CHANGING THE DATA OF N2 AND ACCESSING IT THROUGH N1
n2.data = "Universe"
print(f"{n1.data}, {n1.link.data}")

# DEMONSTRATION OF MULTIPLE LINKS TOGETHER AND LOOPING THROUGH THEM.
n4 = BasicNode("Moon")
n3 = BasicNode("Goodnight", n4)
n2 = BasicNode("World", n3)
n1 = BasicNode("Hello", n2)

print(f"{n1.data}, {n2.data}, {n3.data}, {n4.data}")
print(f"{n1.data}, {n1.link.data}, {n1.link.link.data}, {n1.link.link.link.data}")
# Hello, World, Goodnight, Moon

# Demonstrate looping through nodes using current pointer.
curr = n1
while curr:
    print(f"{curr.data}", end=", ")
    curr = curr.link

print("\b\b")


class MapCellNode:
    """ Toy implementation of a Map Cell Node to demonstrate the flexibility of
    node structures and how they needn't only be lienar objects.
    """

    def __init__(self, data=None):
        """
        Creates a new MapCellNode containing the provided data.
        :param data: The data to store in the node.
        """
        self.data = data
        self.north = None
        self.east = None
        self.south = None
        self.west = None


# DEMONSTRATION OF CREATING NODES THAT RELATE TO EACH OTHER IN A NON LINEAR WAY.
n1 = MapCellNode("Danger")
n2 = MapCellNode("Danger")
n3 = MapCellNode("Safe")
n4 = MapCellNode("Safe")
n5 = MapCellNode("Danger")
n1.east = n2
n1.south = n3
n2.west = n1
n2.south = n4

##################################################
# SIMPLE IMPLEMENTATION OF A SINGLY LINKED LIST
##################################################
class SinglyLinkedList:
    """
    A basic implementation of a singly linked list allowing for search, delete, contains, append.
    """
    class SingleLinkNode:
        """
        A simple node to be used for the SinglyLinkedList containing a next pointer and data field.
        """
        def __init__(self, data):
            """
            Creates a new node containing the provided data.
            :param data: Any datatype that supports equality (for search/contains/delete).
            """
            self.data = data
            self.next = None

    def __init__(self):
        """
        Creates a new empty LinkedList.
        """
        self.first = None
        self.last = None
        self.count = 0

    def __str__(self):
        """
        Generates the string representation of the linked list.  Basically a comma-seperated value
        list of the element values followed by the size.
        Example:  "String1, String2, String3: Size: 3"
        :return: A string representation of the linked list.
        """
        r = ', '.join([x for x in self.iter()])
        r = "[Empty]" if len(r) == 0 else r
        r += f": Size: {self.size()}"
        return r

    def append(self, data):
        """
        Adds a new element to the end of the list.
        :param data: The data to add to the end of the list.
        :return: None
        """
        n = SinglyLinkedList.SingleLinkNode(data)
        # Special case for empty lists
        if self.first is None:
            self.first = n
            self.last = n
        else:
            self.last.next = n
            self.last = n

        self.count += 1

    def contains(self, data):
        """
        Searches the linked list for the provided data.
        :param data: The data (needle) for which to search.
        :return: True if a node contains data matching the searched for data, False otherwise
        """
        curr = self.first

        while curr:
            if curr.data == data:
                return True
            curr = curr.next

        return False

    def clear(self):
        """
        Removes all elements from the list.
        :return:
        """
        self.first = None
        self.last = None
        self.count = 0

    def delete(self, data):
        """
        Searches for an element that contains the provided data.
        :param data: The data for which to search for and delete.
        :return: True if the deletion was successful, False otherwise.
        """
        curr = self.first
        prev = self.first

        while curr:
            if curr.data == data:
                if curr == self.first:  # SPECIAL CASE FOR DELETING THE FIRST NODE
                    self.first = curr.next
                else:
                    prev.next = curr.next
                    if curr == self.last:  # SPECIAL CASE FOR DELETING THE LAST NODE
                        self.last = prev
                self.count -= 1
                return True

            prev = curr
            curr = curr.next

        return False

    def is_empty(self):
        """
        Common implementation to determine if the list contains any elements.
        :return: False if list contains no elements, True otherwise.
        """
        return self.count == 0

    def iter(self):
        """
        Manual implementation of an iterator for the linked list.  When called successively
        will return the next element in the list.  Will return None when the end of the list
        is found.
        :return: The next element of the list.
        """
        curr = self.first
        while curr:
            ret = curr.data
            curr = curr.next
            yield ret

    def search(self, data):
        """
        Searches linearly through the list for an element containing data that matches the data
        for which is being searched.  If found, returns a pointer to the node containing the data.
        Otherwise returns None.

        :param data: The data for which the function will search.
        :return: A pointer to the node that contains the data that was being searched for.
        False otherwise.
        """
        curr = self.first

        while curr:
            if curr.data == data:
                return curr
            curr = curr.next

    def size(self):
        """
        Return the number of elements in the linked list.
        :return: An integer representing the numbrer of elements in the list.  0 if list is empty.
        """
        return self.count


my_singly_linked_list = SinglyLinkedList()

my_singly_linked_list.append("Hello")
print(f"Size Should be 1: {my_singly_linked_list.size()}")
print(f"First and Last should be Hello: {my_singly_linked_list.first.data}, {my_singly_linked_list.last.data}")

my_singly_linked_list.append("World")
print(f"Size Should be 2: {my_singly_linked_list.size()}")
print(f"First (Hello), Last(World): {my_singly_linked_list.first.data}, {my_singly_linked_list.last.data}")

my_singly_linked_list.append("Goodnight")
my_singly_linked_list.append("Moon")

print(f"")

print(f"Should find Hello: {my_singly_linked_list.contains('Hello')}")
print(f"Should NOT find Hi: {my_singly_linked_list.contains('Hi')}")

results = my_singly_linked_list.search("Hello")
print(f"Results Should be Hello: {results.data}")

deleted = my_singly_linked_list.delete("Nope")
print(f"Deleting NOPE should be False, {deleted}")

print(f"Deleting Hello:{my_singly_linked_list.delete('Hello')}")
print(my_singly_linked_list)

print("Clearing...")
my_singly_linked_list.clear()
print(my_singly_linked_list)


##################################################
# SIMPLE IMPLEMENTATION OF A DOUBLY LINKED LIST
##################################################
class DoublyLinkedList:
    """
    A basic implementation of a singly linked list allowing for search, delete, contains, append.
    """
    class DoubleLinkNode:
        """
        A simple node to be used for the SinglyLinkedList containing a next pointer and data field.
        """
        def __init__(self, data):
            """
            Creates a new node containing the provided data.
            :param data: Any datatype that supports equality (for search/contains/delete).
            """
            self.data = data
            self.next = None
            self.prev = None

    def __init__(self):
        """
        Creates a new empty LinkedList.
        """
        self.first = None
        self.last = None
        self.count = 0

    def __str__(self):
        """
        Generates the string representation of the linked list.  Basically a comma-seperated value
        list of the element values followed by the size.
        Example:  "String1, String2, String3: Size: 3"
        :return: A string representation of the linked list.
        """

        r = ', '.join([x for x in self.iter()])
        r = "[Empty]" if len(r) == 0 else r
        r += f": Size: {self.size()}"
        return r

    def append(self, data):
        """
        Adds a new element to the end of the list.
        :param data: The data to add to the end of the list.
        :return: None
        """
        n = DoublyLinkedList.DoubleLinkNode(data)
        # Special case for empty lists
        if self.first is None:
            self.first = n
            self.last = n
        else:
            n.prev = self.last  # the old .last becomes the new node's prev
            self.last.next = n  # the old .last needs a new next (the new node)
            self.last = n  # the last node becomes the last node

        self.count += 1

    def contains(self, data):
        """
        Searches the linked list for the provided data.
        :param data: The data (needle) for which to search.
        :return: True if a node contains data matching the searched for data, False otherwise
        """
        curr = self.first

        while curr:
            if curr.data == data:
                return True
            curr = curr.next

        return False

    def clear(self):
        """
        Removes all elements from the list.
        :return:
        """
        self.first = None
        self.last = None
        self.count = 0

    def delete(self, data):
        """
        Searches for an element that contains the provided data.
        :param data: The data for which to search for and delete.
        :return: True if the deletion was successful, False otherwise.
        """
        curr = self.first
        deleted_fl = False

        if curr is None:  # SPECIAL CASE FOR EMPTY LISTS
            pass
        elif curr.data == data:  # SPECIAL CASE FOR REMOVE FROM FRONT
            self.first = curr.next
            if self.first is not None:  # IF LAST ELEMENT, SKIP CLEARING PREV LINK
                self.first.prev = None  # CLEAR PREV LINK TO NEW FRONT NODE.
            deleted_fl = True
        elif self.last.data == data:  # SPECIAL CASE FOR REMOVE FROM END
            self.last = self.last.prev
            self.last.next = None
            deleted_fl = True
        else:  # REGULAR CASE, LOOP THROUGH TO SEE IF EXISTS IN THE MIDDLE
            while curr:
                if curr.data == data:
                    curr.prev.next = curr.next
                    curr.next.prev = curr.prev
                    deleted_fl = True
                curr = curr.next

        if deleted_fl:
            self.count -= 1

        return deleted_fl

    def is_empty(self):
        """
        Common implementation to determine if the list contains any elements.
        :return: False if list contains no elements, True otherwise.
        """
        return self.count == 0

    def iter(self):
        """
        Manual implementation of an iterator for the linked list.  When called successively
        will return the next element in the list.  Will return None when the end of the list
        is found.
        :return: The next element of the list.
        """
        curr = self.first
        while curr:
            ret = curr.data
            curr = curr.next
            yield ret

    def search(self, data):
        """
        Searches linearly through the list for an element containing data that matches the data
        for which is being searched.  If found, returns a pointer to the node containing the data.
        Otherwise returns None.

        :param data: The data for which the function will search.
        :return: A pointer to the node that contains the data that was being searched for.
        False otherwise.
        """
        curr = self.first

        while curr:
            if curr.data == data:
                return curr
            curr = curr.next

    def size(self):
        """
        Return the number of elements in the linked list.
        :return: An integer representing the numbrer of elements in the list.  0 if list is empty.
        """
        return self.count

 
my_doubly_linked_list = DoublyLinkedList()

my_doubly_linked_list.append("Hello")
print(f"Size Should be 1: {my_doubly_linked_list.size()}")
print(f"First and Last should be Hello: {my_doubly_linked_list.first.data}, {my_doubly_linked_list.last.data}")

my_doubly_linked_list.append("World")
print(f"Size Should be 2: {my_doubly_linked_list.size()}")
print(f"First (Hello), Last(World): {my_doubly_linked_list.first.data}, {my_doubly_linked_list.last.data}")

my_doubly_linked_list.append("Goodnight")
my_doubly_linked_list.append("Moon")


print(f"Should find Hello: {my_doubly_linked_list.contains('Hello')}")
print(f"Should NOT find Hi: {my_doubly_linked_list.contains('Hi')}")

results = my_doubly_linked_list.search("Hello")
print(f"Results Should be Hello: {results.data}")

deleted = my_doubly_linked_list.delete("Nope")
print(f"Deleting NOPE should be False, {deleted}")

print(f"Deleting Hello:{my_doubly_linked_list.delete('Hello')}")
print(my_doubly_linked_list)

print("Clearing...")
my_doubly_linked_list.clear()
print(my_doubly_linked_list)