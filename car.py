from datetime import datetime

class Car:
    def __init__(self, license_plate, start_date, end_date):
        self.license_plate = license_plate
        if isinstance(start_date, str):
            self.start_date = datetime.strptime(start_date, "%Y-%m-%d %H:%M:%S")
        else:
            self.start_date = start_date

        if isinstance(end_date, str):
            self.end_date = datetime.strptime(end_date, "%Y-%m-%d %H:%M:%S")
        else:
            self.end_date = end_date

    '''def calculate_price(self):
        duration_hours = (self.end_date - self.start_date).total_seconds() / 3600
        if duration_hours <= 24:
            return 3 * duration_hours
        else:
            days = duration_hours // 24
            extra_hours = duration_hours % 24
            return (30 * days) + (3 * extra_hours) if extra_hours <= 3 else (30 * (days + 1))'''