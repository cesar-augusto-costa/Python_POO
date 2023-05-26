class ControleRemoto:
    def __init__(self, cor, altura, profundidade, largura):
        self.cor = cor
        self.altura = altura
        self.profundidade = profundidade
        self.largura = largura
    
    def passar_canal(self, botao):
        if botao == '+':
            print('Aumentar Canal')
        elif botao == '-':
            print('Diminuir Canal')

controle_remoto = ControleRemoto("preto", 10, 2, 2)
print(controle_remoto.cor)
controle_remoto.passar_canal('+')

controle_remoto2 = ControleRemoto("cinza", 10, 2, 5)
print(controle_remoto2.largura)
controle_remoto2.passar_canal('-')