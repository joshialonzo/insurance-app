from datetime import datetime


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
