class person():
    def __init__(self, name, id,timelonn):
        self.name = name
        self.id = id
        self.timelonn = timelonn

    def print_name(self):
        print(self.name)
    
    def skrivUT(self):
        print(self.name, self.id, self.timelonn)
