from datetime import datetime, timezone

class DateTimeService():
    @staticmethod
    def steamMaintenanceImminent():
        # Check if the current date and time is Tuesday between 20 and 21 utc

        now = datetime.now(timezone.utc)

        # Check Tuesday
        if now.weekday() != 1:
            return False

        hour = now.hour
        if hour != 20:
            return False
        
        return True
