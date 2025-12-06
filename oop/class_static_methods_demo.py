class Calculator:
    """
    A simple calculator class demonstrating the difference
    between @staticmethod and @classmethod.
    """
    # Class attribute shared by all instances and accessible via class methods
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a: float, b: float) -> float:
        """
        Static method: Performs addition.
        Does NOT receive 'self' or 'cls' — behaves like a regular function
        but lives in the class namespace for logical grouping.
        """
        return a + b

    @classmethod
    def multiply(cls, a: float, b: float) -> float:
        """
        Class method: Performs multiplication and shows class-level information.
        Receives the class itself as the first argument (conventionally named 'cls').
        Can access/modify class state (e.g., cls.calculation_type).
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b