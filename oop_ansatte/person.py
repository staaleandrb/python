class person():
    def __init__(self, name, id,timelonn):
        self.name = name
        self.id = id
        self.timelonn = timelonn

    def print_name(self):
        print(self.name)
    
    def skrivUT(self):
        print(f" Navn: {self.name} Ansatt id: {self.id} timelønn: {self.timelonn}")

    def endreLon(self, nyLon):
        self.timelonn = nyLon
        print(f"Endret timelønn til {self.timelonn}")