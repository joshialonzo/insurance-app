from decimal import Decimal


class DecimalSanitizer:
    def __init__(self, data):
        """Initialize DecimalSanitizer class."""
        self.data = data
    
    def sanitize(self):
        """Transform string to decimal."""
        return round(
            Decimal(str(self.data)),
            ndigits=2,
        )


class IntegerSanitizer:
    def __init__(self, data):
        """Initialize IntegerSanitizer class."""
        self.data = data
    
    def sanitize(self):
        """Transform string to decimal."""
        return int(self.data)
