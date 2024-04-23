from person import person

class ansatt(person):
    def __init__(self, navn, id, timelonn):
        super().__init__(navn, id, timelonn)

    def skrivUt(self):
        print("Ansatt:")
        super().skrivUt()
    
    def regnUtLonn(self, antall_timer):
        return "Ansatt lonn:"+ str(antall_timer * self.timelonn)