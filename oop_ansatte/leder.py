
from person import person

class leder(person):
    def __init__(self, name,id,timelonn,bonusandel):
        super().__init__(name, id, timelonn)
        self.bonusandel = bonusandel


        
    def skrivUT(self):
        print("Leder:")
        super().skrivUT()
        print(f"bonusAndel: {self.bonusandel}")

    def beregn_lønn(self, antall_timer):
        return self.timelonn * antall_timer + self.timelonn * antall_timer * self.bonusandel/100