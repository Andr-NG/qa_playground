# flake8: noqa
# Design a structure for validating different types of input data (strings, numbers, etc.) using a common interface.


# Base Class: Create a base class named BaseValidator.
# It must have an abstract or placeholder method validate(self, data).
# It must have a concrete method is_valid(self, data) that calls validate(data) and handles potential exceptions raised by child classes.

# Derived Class 1: TextValidator
# Inherits from BaseValidator.
# Initialization: Takes min_length and max_length as arguments.
# validate(self, data): Raises a ValueError if the data is not a string, or if its length is outside the min/max range.

# Derived Class 2: NumericalValidator
# Inherits from BaseValidator.
# Initialization: Takes min_value and max_value as arguments.
# validate(self, data): Raises a TypeError if the data cannot be converted to an integer, or a ValueError if the numerical value is outside the min/max range.

from abc import ABC, abstractmethod

class BaseValidator(ABC):

    @abstractmethod
    def validate(self, data):
        pass

    def is_valid(self, data):
        return self.validate(data)
    

class TextValidator(BaseValidator):

    def __init__(self, max_length, min_length):
        self.min_length = min_length
        self.max_length = max_length

    def validate(self, data):
        if not isinstance(data, str) or self.max_length < len(data) < self.min_length:
            raise ValueError("Wrong data value")
        
        if isinstance(data, str) and self.min_length <= len(data) <= self.max_length:
            return True
        else:
            return False

        
text_v = TextValidator(min_length=5, max_length=15)

print(f"Text 'hello world' is valid: {text_v.is_valid('hello world')}")
print(f"Data 123 is valid: {text_v.is_valid(123)}")