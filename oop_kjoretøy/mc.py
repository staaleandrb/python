from vehicle import Vehical

class Mc(Vehical):
    def __init__(self,type, merke, aar, farge,drivverk):
        super().__init__(type, merke, aar, farge)
        self.drivverk = drivverk

    def skrivUt(self):
        super().skrivUt()
        print(f"Drivverk: {self.drivverk}")    


    def drive(self):
        print("Car is moving")

    def stop(self):
        print("Car has stopped")