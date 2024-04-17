from person import person

class ansatte():
    def __init__(self, name, id,timelonn):
        super().__init__(name, id, timelonn)
        
    def beregn_lønn(self, antall_timer):
        return self.timelonn * antall_timer
    
    def skrivUT(self):
        super().skrivUT()