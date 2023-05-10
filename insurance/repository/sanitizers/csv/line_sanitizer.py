from abc import ABC, abstractmethod


class LineSanitizer(ABC):
    """Sanitizer class for sanitizing CSV lines."""

    def __init__(self, line: list):
        """Initialize LineSanitizer class."""
        self.line = line

    @abstractmethod
    def valid(self):
        """Validate line."""
        raise NotImplementedError


class PaymentsLineSanitizer(LineSanitizer):
    """
    Sanitizer class for sanitizing CSV lines
    of the payments CSV file.
    """

    def __init__(self, line: list):
        """Initialize PaymentsLineSanitizer class."""
        self.line = line

    def valid(self):
        """Validate line."""
        return len(self.line) == 16
