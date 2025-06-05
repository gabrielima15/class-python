# você irá criar a class carro e eu quero no mínimo 3 propriedades para a classe carro e no mínimo 3 método para ela.

class carro:
    def __init__(self,marca,valor,ano_fabricacao):
        self.marca = marca
        self.valor = valor 
        self.ano_fabricacao = ano_fabricacao
        
    def ligar(self):
        print('ligando o carro')
    
    def desligar(self):
        print('desligando o carro')
    
    def InformacoesCarro(self):
        print(self.marca,self.valor,self.ano_fabricacao)
        
carro1 = carro("Fiat Uno","10.000","1998")
carro1.ligar()
carro1.desligar()
carro1.InformacoesCarro()