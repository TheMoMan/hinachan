from datetime import datetime, timezone

class DateTimeService():
    @staticmethod
    def steamMaintenanceImminent():
        # Check if the current date and time is soon (Tuesday between 22 and 23 utc)
        # Should probably make this an env var... maybe when I can be bothered to refactor

        now = datetime.now(timezone.utc)

        # Check Tuesday
        if now.weekday() != 1:
            return

        hour = now.hour
        if hour == 23:
            return 'imminent'

        if hour == 22:
            return 'soon'

        return

    @staticmethod
    def withinMinutesPastHour(minutes: int):
        now = datetime.now(timezone.utc)

        if now.minute <= minutes:
            return True

        return False

