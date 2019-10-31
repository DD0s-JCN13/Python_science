class Car:
    wheels_num = 4
    car_doors = 4
    passengers = 5
    def __init__(self, wheels_num=4, car_doors=4, passengers=5):
        self.wheels_num = wheels_num
        self.car_doors = car_doors
        self.passengers = passengers
class SUV(Car):
    brand_name = ""
    airbag = 2
    sunroof = True
    def __init__(self,wheels_num, car_doors, passengers, brand_name="",air_bag=2, sunroof=True):
        super().__init__(wheels_num, car_doors, passengers)
        self.brand_name = brand_name
        self.airbag = air_bag
        self.sunroof = sunroof
    def getDetail(self):
        print("====Details====")
        print("Brand:", self.brand_name)
        print("Wheel numbers:", self.wheels_num)
        print("Passengers:", self.passengers)
        print("Airbags number:", self.airbag)
        print("Sunroof:", self.sunroof)
        print("================")
toyota_rav = SUV(4,5,5,"Toyota Rav",4,True)
toyota_rav.getDetail()
bmw_x5 = SUV(4,5,5,"BMW X5",6,True)
bmw_x5.getDetail()