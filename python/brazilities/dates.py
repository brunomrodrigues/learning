from datetime import datetime

class DatesBrazil:
    def __init__(self) -> None:
        self._datetime_account_created = datetime.today()

    def month(self):
        return self._datetime_account_created.month
    
    def day(self):
        return self._datetime_account_created.day