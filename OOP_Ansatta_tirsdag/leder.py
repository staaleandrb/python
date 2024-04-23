from person import person

class leder(person):
    def __init__(self, navn, id, timelonn,bonusandel):
        super().__init__(navn, id, timelonn)            # arver fra person
        self.bonusandel = bonusandel             

    def skrivUt(self):
        print("Leder:")
        super().skrivUt()
        print(f"Bonusandel: {self.bonusandel}")

    def regnUtLonn(self, antall_timer):
        return "Leder lonn:"+ str(antall_timer * self.timelonn + (self.bonusandel/100))
