from Model import Despesa as dsp
from Model import Bancario as bn
import configparser



# @Alunos --> moc de implementação correta para versões futuras;
bancos = []
bancos.append(bn.Bancario("Banco do Brasil", "0001", "123456-7", "Conta Corrente"))
bancos.append(bn.Bancario("Caixa Econômica Federal", "0002", "654321-8", "Conta Poupança"))
bancos.append(bn.Bancario("Itaú", "0003", "123456-7", "Conta Salário"))

desepesa = []
desepesa.append(dsp.Despesa("01/01/2023", 100.0, "Alimentação", "Supermercado", "Compras", "Cartão de Crédito", "BB"))

class Model(bn.Bancario, dsp.Despesa ):
  def __init__(self, bank, ag, cc, tipo, dat_despesa, valor, cat_despesa, descricao, tag, forma_pgmt, conta):    
    pass

# @Alunos --> moc de implementação correta para versões futuras;

despesas_list = []
bancos_list = [["Banco do Brasil", "0001", "123456-7",], ["Caixa Econômica Federal", "0002", "654321-8",], ["Itaú", "0003", "123456-7",],]
categorias_list = ["Alimentação", "Transporte", "Moradia", "Educação", "Saúde", "Lazer", "Compras online" "Outros"]
config = configparser.ConfigParser()
config.read("user.data", encoding="utf-8")

def adiocionar_despesa(despesa):
  dsp_new = dsp.Despesa(despesa["data"], despesa["valor"], despesa["categoria"], despesa["descricao"], despesa["tag"], despesa["forma_pgmt"], despesa["banco"])
  desepesa.append(dsp_new)

def adiocionar_conta(conta):
    bancos_list.append(conta)

def adiocionar_categoria(categoria):
    categorias_list.append(categoria)

def remover_despesa(despesa):
    despesas_list.remove(despesa)

def clac_total_mensal(competencia):
  total = 0
  for i in range(len(desepesa)):
      data = desepesa[i].get_dat_despesa()
      
  return total

def get_Usuario_data():
  user = config["credenciais"]["user"]
  senha = config["credenciais"]["senha"]
  return user, senha


