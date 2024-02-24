class Car:
    def __init__(self, id, make, model, size, price_per_day, registration_number, is_rented=False):
        self.id = id
        self.make = make
        self.model = model
        self.size = size
        self.price_per_day = price_per_day
        self.registration_number = registration_number
        self.is_rented = is_rented

    def to_dict(self):
        return {
            "id": self.id,
            "make": self.make,
            "model": self.model,
            "size": self.size,
            "price_per_day": self.price_per_day,
            "registration_number": self.registration_number,
            "is_rented": self.is_rented
        }
