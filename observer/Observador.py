import iObservador

class Observador(iObservador.IObservador):
    def __init__(self, id):
        self.id = id

    def update(self, frase):
        print("Cliente:", self.id)
        print(f"Qtn de palavras na frase: {frase.get_palavras()}")
        print(f"Qtn de palavras com número pares: {frase.get_qnt_pares()}")
        print(f"Qtn de palavras começadas com maiúsculas: {frase.get_qnt_upper()}")