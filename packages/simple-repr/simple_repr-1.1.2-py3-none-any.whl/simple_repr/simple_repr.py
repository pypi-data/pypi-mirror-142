"""Module to create __repr__ method for classes."""


class SimpleRepr:
    """
    Class to generate a string representation of an object.

    Examples:
        Inheritance:
            >>> from simple_repr import SimpleRepr
            >>> class User(SimpleRepr):
            ...     def __init__(self, name: str, age: int):
            ...         self.name = name
            ...         self.age = age
            ...
            >>> user = User('John', 25)
            >>> print(user)
            User(name='John', age=25)

        Function:
            >>> from simple_repr import SimpleRepr
            >>> class User:
            ... def __init__(self, name: str, age: int):
            ...     self.name = name
            ...     self.age = age
            ...
            ... def __repr__(self) -> str:
            ...     return SimpleRepr.make_repr(self)
            ...
            >>> user = User('John', 25)
            >>> print(user)
            User(name='John', age=25)
    """

    def __repr__(self) -> str:
        """Use when SimpleRepr is inherited from."""
        return self.make_repr(self)

    @staticmethod
    def make_repr(obj: object) -> str:
        """
        Generate a __repr__ method for any object.

        Args:
            obj: object
                The object to generate a __repr__ method for.

        Returns: str
            A string representation of the object.

        Excepts: AttributeError
            If the object provided is not a class
            the object is cast as str and returned.
        """
        try:
            attrs = obj.__dict__.items()
            as_str = f"{str(obj.__class__.__qualname__)}("

            for i, (key, value) in enumerate(attrs):
                as_str += f"{key}={SimpleRepr._check_type(value)}"

                if i != len(attrs) - 1:
                    as_str += ", "

                else:
                    as_str += ")"

            return as_str

        except AttributeError:
            return str(obj)

    @staticmethod
    def _check_type(value: any) -> any:
        """Add single quotes around strings."""
        if isinstance(value, str):
            return f"'{value}'"
        return value
