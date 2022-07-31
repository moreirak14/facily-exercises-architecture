 
import string
import random


class Veiculo():
    # init method or constructor
    def __init__(self, catalogue_price):
        self.id = VehicleRegistry().generate_vehicle_id(12)
        self.license_plate = VehicleRegistry().generate_vehicle_license(id)
        self.model = 
        


 
class VehicleRegistry:

    def generate_vehicle_id(self, length):
        return ''.join(random.choices(string.ascii_uppercase, k=length))

    def generate_vehicle_license(self, id):
        first_section = id[:2]
        second_section = ''.join(random.choices(string.digits, k=2))
        third_section = ''.join(random.choices(string.ascii_uppercase, k=2))
        return f"{first_section}-{second_section}-{third_section}"
