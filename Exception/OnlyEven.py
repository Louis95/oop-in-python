'''
While this class is effective for demonstrating exceptions in action, it isn't very good at its job. 
It is still possible to get other values into the list using index notation or slice notation. 
This can all be avoided by overriding other appropriate methods, some of which are double-underscore methods.

'''

class OnlyEven(list):
    def append(self, integer):
        if not isinstance(integer, int):
            raise TypeError("Only integers can be added")
        if integer % 2:
            raise ValueError("Only even even numbers can be added")
        super().append(integer)

