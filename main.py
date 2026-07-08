class Talaba:
    def __init__(self, ism, yosh, kurs):
        self.ism = ism
        self.yosh = yosh
        self.kurs = kurs

    def info(self):
        print("----- TALABA MA'LUMOTI -----")
        print("Ism:", self.ism)
        print("Yosh:", self.yosh)
        print("Kurs:", self.kurs)
        print()

t1 = Talaba("Azizbek", 18, 1)
t2 = Talaba("Ali", 19, 2)
t3 = Talaba("Vali", 20, 3)

t1.info()
t2.info()
t3.info()