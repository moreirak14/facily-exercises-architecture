import string
import random


class VehicleRegistry:

    def generate_vehicle_id(self, length):
        return ''.join(random.choices(string.ascii_uppercase, k=length))

    def generate_vehicle_license(self, id):
        first_section = id[:3]
        second_section = ''.join(random.choices(string.digits, k=4))
        #third_section = ''.join(random.choices(string.ascii_uppercase, k=2))
        return f"{first_section}-{second_section}"


class VeiculoID:
    # gera um id com 12 caracteres
    def gerar_id_veiculo(self):
        veiculo = VehicleRegistry()
        veiculo_id = veiculo.generate_vehicle_id(12) 
        return veiculo_id


class PlacaVeiculo:
    # gera a placa de baseado no id do veículo
    def gerar_id_placa(self):
        placa = VehicleRegistry()
        veiculo_id_gerado = VeiculoID().gerar_id_veiculo()
        placa_id = placa.generate_vehicle_license(veiculo_id_gerado)
        return placa_id


class Porcentagem():
    # calcula a taxa de imposto. o padrão é 5%. para carros eletréticos o valor é 2%
    def taxa_porcentagem(self):
        tax_percentage = 0.05
        electric_models = ['Tesla Model 3',
                           'Chevrolet Bold', 'BMW i3', 'Honda Civic LX']
                           
        if CatalogoCarros().precos_carros():
            taxa_modelos_eletricos = 0.02

        return electric_models


class CatalogoCarros():
    # determina o preco do veiculo
    def precos_carros(self, brand: string):
        catalogue_price = 0
        if brand == 'Tesla Model 3': 
            catalogue_price = 445000
        elif brand == 'Chevrolet Bold':
            catalogue_price = 317000
        elif brand == 'BMW i3':
            catalogue_price = 319950
        elif 'Honda Civic LX':
            catalogue_price = 127900

        # calcula a taxa de imposto. o padrão é 5%. para carros eletréticos o valor é 2%
        electric_models = ['Tesla Model 3','Chevrolet Bold', 'BMW i3']

        if brand in electric_models:
            tax_percentage = 0.02
        else:
            tax_percentage = 0.05

        # calcula a valor a ser pago
        payable_tax = tax_percentage * catalogue_price

        id_veiculo = VeiculoID().gerar_id_veiculo()
        id_placa = PlacaVeiculo().gerar_id_placa()

        print(f'Marca: {brand}')
        print(f'ID: {id_veiculo}')
        print(f'Placa: {id_placa}')
        print(f'Imposto a ser pago: {payable_tax}')


app = CatalogoCarros()
app.precos_carros('Honda Civic LX')
