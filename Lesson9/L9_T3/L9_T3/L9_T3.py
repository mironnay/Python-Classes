class Car:
    def __init__(self, name, tank_capacity):
        self.name = str(name)
        self.speed = 0
        self.tank_capacity = tank_capacity
        self.is_engine_on = False

    def get_engine_status(self):
        print(f"Engine is on {self.is_engine_on}")

    def switch_engine(self):
        if self.is_engine_on == False:
            self.is_engine_on = True
            print("Now engine is on")
        else:
            self.is_engine_on = False
            print("Now engine is off")

    def speed_up(self, delta):
        self.speed += delta
        print(f"Current speed is {self.speed}")

    def slow_down(self, delta):
        self.speed -= delta
        if self.speed < 0:
            self.speed = 0
        print(f"Current speed is {self.speed}")

    def get_tank_capacity(self):
        return self.tank_capacity

    def get_car_name(self):
        print(f"This car`s name is {self.name}")

car1 = Car("Cello", 200)
car1.switch_engine()
car1.speed_up(100)
car1.slow_down(200)
car1.get_tank_capacity()
car1.get_car_name()