class Komponent:
    def __init__(self, navn, pris):
        self.navn = navn
        self.pris = pris

    def vis_komponent(self):
        print(f"Navn: {self.navn}")
        print(f"Pris: {self.pris}")

    def to_dict(self):
        return {
            "Navn": self.navn,
            "pris": self.pris,
        }