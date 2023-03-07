class Car:
    def __init__(self, category, model, brand, fuel, transmission):
        self.category = category
        self.model = model
        self.brand = brand
        self.fuel = fuel
        self.transmission = transmission

class RentalCar(Car):
    all_rental_cars = []

    def __init__(self, car, year, plate, client=None):
        super().__init__(
            car.category,
            car.model,
            car.brand,
            car.fuel,
            car.transmission
        )
        self.year = year
        self.plate = plate
        self.client = client
        self.rental_status = "Disponível"
        self.all_rental_cars.append(self)
        self.number = self.all_rental_cars.index(self)


    def get_info(self):
        info = f"""
            Número: {self.number}
            Categoria: {self.category}
            Transmissão: {self.transmission}
            Combustível: {self.fuel}
            Marca: {self.brand}
            Modelo: {self.model}
            Ano: {self.year}
            Placa: {self.plate}
        """
        return info

    @classmethod
    def get_all_rental_cars(self):
        return self.all_rental_cars

    def rent_vehicle(self):
        self.rental_status = "Alugado"

class Client:
    all_clients = []

    def __init__(self, name, cpf, rg):
        self.name = name
        self.cpf = cpf
        self.rg = rg
        self.all_clients.append(self)


class RentalReport:
    all_reports = []

    def __init__(self, client, rental_car, rental_begin, rental_end):
        self.client = client
        self.car = rental_car
        self.rental_begin = rental_begin
        self.rental_end = rental_end
        self.all_reports.append(self)

    def get_info(self):
        info = f"""
            Car Alugado

            Início: {self.rental_begin}
            Fim: {self.rental_end}

            Número: {self.car.number}
            Categoria: {self.car.category}
            Transmissão: {self.car.transmission}
            Combustível: {self.car.fuel}
            Marca: {self.car.brand}
            Modelo: {self.car.model}
            Year: {self.car.year}
            Plate: {self.car.plate}

            Cliente

            Nome: {self.client.name}
            CPF: {self.client.cpf}
            RG: {self.client.rg}
        """
        return info
