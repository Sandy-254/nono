
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def device_info(self):
        return f"{self.brand} {self.model}"



class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        
        super().__init__(brand, model)
        self.storage = storage
        self.battery = battery

    def call(self, number):
        print(f" Calling {number} from {self.device_info()}...")

    def charge(self, amount):
        self.battery = min(100, self.battery + amount)
        print(f" Battery charged to {self.battery}%")

    def phone_info(self):
        return f"{self.device_info()} | Storage: {self.storage}GB | Battery: {self.battery}%"


phone1 = Smartphone("Samsung", "Galaxy S23", 128, 75)
print(phone1.phone_info())
phone1.call("+254712345678")
phone1.charge(20)
