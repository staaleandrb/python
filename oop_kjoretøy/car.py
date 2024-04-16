class Car:
    def __init__(self,merke,aar,farge):
        self.merke = merke
        self.aar = aar
        self.farge = farge
        


    def drive(self):
        print("Car is moving")

    def stop(self):
        print("Car has stopped")