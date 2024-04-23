from komponenter import Komponent

class Ram(Komponent):
    def __init__(self, navn, pris, minne, hastighet):
        super().__init__(navn, pris)
        self.minne = minne
        self.hastighet = hastighet

    def vis_komponent(self):
        super().vis_komponent()
        print(f"Minne: {self.minne}")
        print(f"Hastighet: {self.hastighet}")