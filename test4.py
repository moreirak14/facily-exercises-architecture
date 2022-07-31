import string
import random


class VehicleRegistry:

    def generate_vehicle_id(self, length):
        return ''.join(random.choices(string.ascii_uppercase, k=length))

    def generate_vehicle_license(self, id):
        first_section = id[:2]
        second_section = ''.join(random.choices(string.digits, k=2))
        third_section = ''.join(random.choices(string.ascii_uppercase, k=2))
        return f"{first_section}-{second_section}-{third_section}"


class Vehicle:
    def __init__(self, registry, brand, value, tax, is_eletric):
        self.id = registry.generate_vehicle_id(12)
        self.plate = registry.generate_vehicle_license(self.id)
        self.brand = brand
        self.value = value
        self.tax = tax
        self.is_eletric = is_eletric

    '''
    catalogue_price = 0
        if brand == 'Tesla Model 3':
            catalogue_price = 445000
        elif brand == 'Chevrolet Bold':
            catalogue_price = 317000
        elif brand == 'BMW i3':
            catalogue_price = 319950
        elif 'Honda Civic LX':
            catalogue_price = 127900
    '''

class FactoriPrinter:

    @staticmethod
    def printer_vehicle(self, Vehicle):
        print(f'Marca: {Vehicle.brand}')
        print(f'ID: {Vehicle.vehicle_id}')
        print(f'Placa: {Vehicle.license_plate}')
        print(f'Imposto a ser pago: {Vehicle.payable_tax}')


class Application:

    def register_vehicle(self, brand: string):
        registry = VehicleRegistry()

        # gera um id com 12 caracteres
        # vehicle_id = registry.generate_vehicle_id(12)

        # gera a placa de baseado no id do veículo
        # license_plate = registry.generate_vehicle_license(vehicle_id)

        # determina o preco do veiculo
        v1 = Vehicle(registry, "BMW i3", 445000, 234, True)
        v2 = FactoriPrinter.printer_vehicle(v1)
        # calcula a taxa de imposto. o padrão é 5%. para carros eletréticos o valor é 2%
        tax_percentage = 0.05
        electric_models = ['Tesla Model 3',
                           'Chevrolet Bold', 'BMW i3', 'Honda Civic LX']
        if brand in electric_models:
            tax_percentage = 0.02

        # calcula a valor a ser pago
        #payable_tax = tax_percentage * catalogue_price

        

app = Application()
app.register_vehicle("112")
