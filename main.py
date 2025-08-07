class Percobaan_Dengan_Linux:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return "ini hanyalah percobaan dengan " +  self.p1 + self.p2
    
percobaan = Percobaan_Dengan_Linux("WSL", ".")
print(percobaan)
