class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def print_car_info(self):
        print(f"Марка: {self.brand}, Модель: {self.model}, Год: {self.year}")

    def change_brand(self, new_brand):
        self.brand = new_brand

    def change_model(self, new_model):
        self.model = new_model

    def change_year(self, new_year):
        self.year = new_year

    def change_all(self, new_brand, new_model, new_year):
        self.brand = new_brand
        self.model = new_model
        self.year = new_year


if __name__ == "__main__":
    car1 = Car("Lada", "Vesta", 2021)
    car2 = Car("Lada", "Granta", 2019)
    car3 = Car("Lada", "Niva", 2023)

    car1.print_car_info()
    car2.print_car_info()
    car3.print_car_info()
