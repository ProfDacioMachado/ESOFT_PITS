class Bancario():
    def __init__ (self, bank, ag, cc, tipo):
        self.bank = bank
        self.ag = ag
        self.cc = cc
        self.tipo = tipo

    def set_bank(self, bank):
        self.bank = bank

    def get_bank(self):    
        return self.bank

    def set_ag(self, ag):
        self.ag = ag

    def get_ag(self):    
        return self.ag

    def set_cc(self, cc):    
        self.cc = cc

    def get_cc(self):   
        return self.cc
