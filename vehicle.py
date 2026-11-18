import datetime

class Vehicle:

    def __init__(self, brand, model, year, mileage_km, engine_cc, fuel_type, transmission, steering, purchase_price_jpy):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage_km = mileage_km
        self.engine_cc = engine_cc
        self.fuel_type = fuel_type
        self.transmission = transmission
        self.steering = steering
        self.purchase_price_jpy = purchase_price_jpy

    def validate_steering(self) -> bool:
        try:
            if type(self.steering) != str:
                raise TypeError
            
            elif self.steering.strip().upper() == "LHD":
                return True
                
            else:
                return False
            
        except TypeError:
            print("Please insert valid type of data")
            return False
        

    def calculate_age(self):
        return datetime.datetime.now().year - self.year

    def validate_mileage(self) -> bool:
        try:
            if type(self.mileage_km) != int:
                raise TypeError
            
            elif self.mileage_km < 0:
                raise ValueError

            else:
                return True

        except (ValueError, TypeError) as e:
            print("Please enter valid mileage", e)
            return False

    
    def validate_price(self) -> bool:
        try:
            if type(self.purchase_price_jpy) != float and type(self.purchase_price_jpy) != int:
                raise TypeError

            if self.purchase_price_jpy <= 0:
                raise ValueError

            else:
                return True

        except (TypeError, ValueError) as e:
            print("Price cannot be negative", e)
            return False

    def validate_year(self) -> bool:
        try:
            if type(self.year) != int:
                raise TypeError

            elif self.year < 0:
                raise ValueError
            
            elif not 1950 <= self.year <= datetime.datetime.now().year:
                raise ValueError

            else:
                return True


        except (ValueError, TypeError) as e:
            print("Please enter valid year", e)
            return False


    def validate_vehicle(self) -> bool:
        validations = [
        self.validate_steering(),
        self.validate_mileage(),
        self.validate_price(),
        self.validate_year()
    ]

        return all(validations)