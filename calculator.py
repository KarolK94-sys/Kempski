
"""
Moduł calculator.py
Zawiera klasę Calculator do wykonywania podstawowych operacji matematycznych.
"""

class Calculator:
    """Klasa reprezentująca prosty kalkulator operacji arytmetycznych."""

    def __init__(self, op1: float, op2: float):
        """Inicjalizuje kalkulator z dwoma operandami."""
        self.__op1 = op1
        self.__op2 = op2

    def sum(self):
        """Zwraca sumę dwóch operandów."""
        return self.__op1 + self.__op2

    def subtract(self):
        """Zwraca różnicę dwóch operandów."""
        return self.__op1 - self.__op2

    def multiply(self):
        """Zwraca iloczyn dwóch operandów."""
        return self.__op1 * self.__op2

    def divide(self):
        """Zwraca iloraz dwóch operandów. Podnosi wyjątek przy dzieleniu przez zero."""
        if self.__op2 == 0:
            raise ZeroDivisionError("Nie można dzielić przez zero")
        return self.__op1 / self.__op2
