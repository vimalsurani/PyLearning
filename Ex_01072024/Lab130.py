# Inheritance
# Acquire the Attributes and Behaviour
# Data members and Methods

# E.g. 3BHK House -F -> Inheritance - Son
# Inheritance is concept in object-oriented programming (OOP) that allows a class (child class)
# to inherit attributes and methods from another class (parent class)

# Types of Inheritance

# Single - 80%
# Multiple
# Multi level
# Hybrid
# Hierarchical


# Single Inheritance


class Grandparent:  # Parent Class, Base Class

    key = "abc123"

    def grandparent_method(self):
        return "Grandparent's method"


class Father(Grandparent):  # Child Class, Sub Class

    def parent_method(self):
        return "Parent's Method"


grandfather = Grandparent()
grandfather.grandparent_method()
# grandfather.parent_method()

parent = Father()
print(parent.parent_method())
print(parent.grandparent_method())  # how parent is able to call the grandparent? inheritance
print(parent.key)
