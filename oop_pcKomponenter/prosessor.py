from komponenter import Komponent

class Prosessor(Komponent):
    def __init__(self, navn, pris, kjerner, klokkehastighet):
        super().__init__(navn, pris)
        self.kjerner = kjerner
        self.klokkehastighet = klokkehastighet

    def vis_komponent(self):
        print("Prosessor:")
        super().vis_komponent()
        print(f"Kjerne: {self.kjerner}")
        print(f"klokkehastighet: {self.klokkehastighet}")