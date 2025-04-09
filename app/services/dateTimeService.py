import os
from datetime import datetime, timezone

class DateTimeService():
    @staticmethod
    def steamMaintenanceImminent():
        # Check if the current date and time is soon (Tuesday between 22 and 23 utc)

        maintenanceHour = os.environ['STEAM_MAINTENANCE_HOUR_UTC']

        now = datetime.now(timezone.utc)

        # Check Tuesday
        if now.weekday() != 1:
            return

        hour = now.hour
        if hour == maintenanceHour:
            return 'imminent'

        if hour == (maintenanceHour + 23) % 24:
            return 'soon'

        return

    @staticmethod
    def withinMinutesPastHour(minutes: int):
        now = datetime.now(timezone.utc)

        if now.minute <= minutes:
            return True

        return False

