from abc import ABC, abstractmethod

from .line_sanitizer import PaymentsLineSanitizer


class FileSanitizer(ABC):
    """Sanitizer class for sanitizing CSV files."""

    def __init__(self, lines: list):
        """Initialize FileSanitizer class."""
        self.lines = lines

    @abstractmethod
    def sanitize(self):
        """Sanitize lines."""
        raise NotImplementedError


class PaymentsFileSanitizer(FileSanitizer):
    """Sanitizer class for sanitizing CSV files."""

    def __init__(self, lines: list):
        """Initialize FileSanitizer class."""
        self.lines = lines

    def sanitize(self):
        """Sanitize lines."""
        sanitized_lines = [
            line for line in self.lines
            if PaymentsLineSanitizer(line).valid()
        ]
        return sanitized_lines
