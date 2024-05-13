from datetime import datetime, timezone

class DateTimeService():
    @staticmethod
    def steamMaintenanceImminent():
        # Check if the current date and time is soon (Tuesday between 22 and 23 utc)

        now = datetime.now(timezone.utc)

        # Check Tuesday
        if now.weekday() != 1:
            return

        hour = now.hour
        if hour == 22:
            return 'imminent'

        if hour == 21:
            return 'soon'

        return

    @staticmethod
    def withinMinutesPastHour(minutes: int):
        now = datetime.now(timezone.utc)

        if now.minute <= minutes:
            return True

        return False

