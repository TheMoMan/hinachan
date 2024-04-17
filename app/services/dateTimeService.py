from datetime import datetime, timezone

class DateTimeService():
    @staticmethod
    def steamMaintenanceImminent():
        # Check if the current date and time is Tuesday between 22 and 23 utc

        now = datetime.now(timezone.utc)

        # Check Tuesday
        if now.weekday() != 1:
            return False

        hour = now.hour
        if hour != 22:
            return False
        
        return True
    
    @staticmethod
    def withinMinutesPastHour(minutes: int):
        now = datetime.now(timezone.utc)

        if now.minute <= minutes:
            return True
        
        return False

