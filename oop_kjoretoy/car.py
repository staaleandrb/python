from vehicle import Vehical

class Car(Vehical):
    def __init__(self,type, merke, aar, farge,antallDorer):
        super().__init__(type, merke, aar, farge)
        self.antall = antallDorer

    def skrivUt(self):
        super().skrivUt()
        print(f"Antall dører: {self.antall}")    


    def drive(self):
        print("Car is moving")

    def stop(self):
        print("Car has stopped")