class person():
    def __init__(self,navn,id,timelonn):
        self.navn = navn
        self.id = id
        self.timelonn = timelonn
    
    def skrivUt(self):
        print(f"Navn: {self.navn}\nId: {self.id}\nTimelønn: {self.timelonn}")
    