class WordSanitizer:
    """Sanitizer class for sanitizing words."""
    DICTIONARY = {
        "periodicity": {
            "MENSUAL": "monthly",
            "MENSUAL S REC": "monthly",
            "monthly": "monthly",
            "TRIMESTRAL": "quarterly",
            "TRIMESTRAL S RC": "quarterly",
            "quarterly": "quarterly",
            "SEMESTRAL": "biannual",
            "SEMESTRAL S REC": "biannual",
            "biannual": "biannual",
            "ANUAL": "annual",
            "ANUAL S REC": "annual",
            "annual": "annual",
        },
        "status": {
            "PAGO NORM.": "normal",
            "normal": "normal",
        },
        "payment_method": {
            "AGENTE": "agent",
            "TARJ.CRED.": "credit",
            "credit": "credit",
            "AMEX": "amex",
            "amex": "amex",
            "TAR DEBITO": "debit",
            "debit": "debit",
        },
    }

    def __init__(self, field, data):
        """Initialize WordSanitizer class."""
        self.field = field
        self.data = data

    def sanitize(self):
        """Sanitize data."""
        return self.DICTIONARY[self.field][self.data]
