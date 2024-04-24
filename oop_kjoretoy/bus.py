from vehicle import Vehical

class Bus(Vehical):
    def __init__(self,type, merke, aar, farge,antallSeter):
        super().__init__(type, merke, aar, farge)
        self.antallSeter = antallSeter

    def skrivUt(self):
        super().skrivUt()
        print(f"Antall seter: {self.antallSeter}")    


    def drive(self):
        print("Car is moving")

    def stop(self):
        print("Car has stopped")