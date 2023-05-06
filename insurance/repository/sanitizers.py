from datetime import datetime
from decimal import Decimal


class WordSanitizer:
    """Sanitizer class for sanitizing words."""
    DICTIONARY = {
        "periodicity": {
            "MENSUAL": "monthly",
            "MENSUAL S REC": "monthly",
            "TRIMESTRAL": "quarterly",
            "TRIMESTRAL S RC": "quarterly",
            "SEMESTRAL": "biannual",
            "SEMESTRAL S REC": "biannual",
            "ANUAL": "annual",
            "ANUAL S REC": "annual",
        }        
    }

    def __init__(self, field, data):
        """Initialize WordSanitizer class."""
        self.field = field
        self.data = data

    def sanitize(self):
        """Sanitize data."""
        return self.DICTIONARY[self.field][self.data]


class DateSanitizer:
    def __init__(self, format="%d/%m/%Y", data=None):
        """Initialize DateSanitizer class."""
        self.format = format
        self.data = data

    def sanitize(self):
        """
        Transform date with day/month/year format
        to year-month-day format.
        Example: 30/03/2023 -> 2023-03-30
        """
        date = datetime.strptime(self.data, self.format)
        date_string = date.strftime("%Y-%m-%d")
        return date_string


class DecimalSanitizer:
    def __init__(self, data):
        """Initialize DecimalSanitizer class."""
        self.data = data
    
    def sanitize(self):
        """Transform string to decimal."""
        return Decimal(self.data)


class IntegerSanitizer:
    def __init__(self, data):
        """Initialize IntegerSanitizer class."""
        self.data = data
    
    def sanitize(self):
        """Transform string to decimal."""
        return int(self.data)
