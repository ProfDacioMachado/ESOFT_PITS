from Model import model as md
class User():
    def __init__(self, login, senha):
        self.login = login
        self.senha = senha

    def set_login(self, login):
        self.login = login  
    def get_login(self):  
        return self.login
    def set_senha(self, senha):
        self.senha = senha
    def get_senha(self):  
        return self.senha
    
    def autenticar(self):
        data_usuario, data_senha = md.get_Usuario_data()
        if self.login == data_usuario  and self.senha == data_senha:
            return True
        else:
            return False
