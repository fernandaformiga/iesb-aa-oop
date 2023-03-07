from classes import Car, RentalCar, Client, RentalReport


def register_new_car():
    print("As categorias cadastradas são:")
    if RentalCar.get_all_rental_cars() == []:
        print("Ainda não há carros registrados.\n")
    for car in RentalCar.get_all_rental_cars():
        print(car.get_info())

    category_presence = input("O carro que será cadastrado está em uma das categorias listadas acima [S/N]?")

    if category_presence == "N":
        category = input("Entre com o nome da categoria: ")
        transmission = input("Informe a Transmissão: ")
        fuel = input("Informe o tipo de Combustível: ")
        brand = input("Informe a Marca: ")
        model = input("Informe o Modelo: ")
        year = input("Informe o Ano: ")
        plate = input("Informe a Placa: ")

        car = Car(category=category, transmission=transmission, fuel=fuel, brand=brand, model=model)
        RentalCar(car=car, year=year, plate=plate)
        
    elif category_presence == "S":
        category_number = input("Escolha o número da categoria:")

        for car in RentalCar.get_all_rental_cars():
            if str(car.number) == category_number:
                selected_car = car

        year = input("Informe o Ano: ")
        plate = input("Informe a Placa: ")
        RentalCar(car=selected_car, year=year, plate=plate)

def register_new_client():
    name = input("Informe o nome do cliente: ")
    rg = input("Informe a RG: ")
    cpf = input("Informe o CPF: ")

    Client(name=name, rg=rg, cpf=cpf)

def rent_a_car():
    print("Escolha um dos carros disponíveis.")
    available_cars = []

    for car in RentalCar.get_all_rental_cars():
        if car.rental_status == "Disponível":
            available_cars.append(car)
            print(car.get_info())

    if available_cars == []:
        print("Não há carros disponíveis para alugar no momento.")
        return

    car_number = input("Insira o número do veículo que deseja alugar: ")

    for car in RentalCar.get_all_rental_cars():
        if car.number == int(car_number):
            selected_car = car

    client_cpf = input("Insira o CPF do cliente que deseja alugar o carro: ")
    for client in Client.all_clients:
        if client_cpf == client.cpf:
            selected_client = client

    begin_date = input("Insira a data de início: ")
    end_date = input("Insira a data de devolução: ")

    selected_car.rent_vehicle()
    RentalReport(client=selected_client, rental_car=selected_car, rental_begin=begin_date, rental_end=end_date)

    print("Car alugado com sucesso!\n")

def obtain_rental_reports():
    for report in RentalReport.all_reports:
        print(report.get_info())
    pass

def run():
    menu = {
        1: register_new_car,
        2: register_new_client,
        3: rent_a_car,
        4: obtain_rental_reports
    }

    while True:
        print("Bem-vindo(a) à locadora Boa Viagem!\n")
        option = (int(input("""
            Escolha uma das opções:

            1) Cadastrar um novo veículo\n
            2) Cadastrar um novo cliente\n
            3) Realizar a locação de um veículo\n
            4) Obter relatório de locação\n
            5) Sair

        """)))

        if option == 5:
            break

        selected_option = menu.get(option)
        if selected_option:
            selected_option()
        else:
            print("Operação inválida")


if __name__ == '__main__':
    run()
