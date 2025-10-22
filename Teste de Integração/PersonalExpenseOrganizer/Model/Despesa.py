class Despesa():

    def __init__(self, dat_despesa, valor, cat_despesa, descricao, tag,
                 forma_pgmt, conta):
        self.dat_despesa = dat_despesa
        self.valor = valor
        self.cat_despesa = cat_despesa
        self.descricao = descricao
        self.tag = tag
        self.forma_pgmt = forma_pgmt
        self.conta = conta

    def set_valor(self, valor):
        self.valor = valor

    def get_valor(self):
        return self.valor

    def set_dat_despesa(self, dat_despesa):
        self.dat_despesa = dat_despesa

    def get_dat_despesa(self):
        return self.dat_despesa

    def set_cat_despesa(self, cat_despesa):
        self.cat_despesa = cat_despesa

    def get_cat_despesa(self):
        return self.cat_despesa

    def set_descricao(self, descricao):
        self.descricao = descricao

    def get_descricao(self):
        return self.descricao

    def set_tag(self, tag):
        self.tag = tag

    def get_tag(self):
        return self.tag

    def set_forma_pgmt(self, forma_pgmt):
        self.forma_pgmt = forma_pgmt

    def get_forma_pgmt(self):
        return self.forma_pgmt

    def set_conta(self, conta):
        self.conta = conta
