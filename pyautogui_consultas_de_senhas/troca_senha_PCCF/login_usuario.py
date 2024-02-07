class login:

    def __init__(self, usuarios, senha_atual, senha_nova):
        self.usuario = usuarios
        self.s_atual = senha_atual
        self.s_nova = senha_nova

    def usuario(self):

        return self.usuario

    def senha_atual(self):

        return self.s_atual

    def senha_nova(self):

        return self.s_nova

