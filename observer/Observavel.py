import iObservavel

class Observavel(iObservavel.IObservavel):
    def __init__(self):
        self.palavras = None
        self.qnt_pares = None
        self.qnt_upper = None
        self.clientes = []

    def registra_observador(self, obs):
        self.clientes.append(obs)

    def remove_observador(self, obs):
        if obs in self.clientes:
            self.clientes.remove(obs)

    def notifica_observadores(self):
        for observador in self.clientes:
            observador.update(self)

    def novas_medidas(self):
        self.notifica_observadores()

    def set_nova_frase(self, frase):
        print("\n\n####### Nova Frase #######\n\n")

        aux_a = 0
        aux_b = 0

        palavras = frase.strip().split(" ")
        for i in palavras:
            if (len(i) % 2) == 0:
                aux_a += 1
            if i[0].isupper():
                aux_b += 1
        

        self.palavras = len(palavras)
        self.qnt_pares = aux_a
        self.qnt_upper = aux_b

        self.novas_medidas()

    def get_palavras(self):
        return self.palavras

    def set_palavras(self, palavras):
        self.palavras = palavras

    def get_qnt_pares(self):
        return self.qnt_pares

    def set_qnt_pares(self, qnt_pares):
        self.qnt_pares = qnt_pares

    def get_qnt_upper(self):
        return self.qnt_upper

    def set_qnt_upper(self, qnt_upper):
        self.qnt_upper = qnt_upper

    def set_clientes(self, clientes):
        self.clientes = clientes

    def get_clientes(self):
        return self.clientes

