import pytest
import Observador
import Observavel

def test_inscricao():
    frase = Observavel.Observavel()
    obs = Observador.Observador(1)
    frase.registra_observador(obs)
    assert len(frase.get_clientes()) == 1

def test_remocao():
    frase = Observavel.Observavel()
    obs1 = Observador.Observador(1)
    obs2 = Observador.Observador(2)
    obs3 = Observador.Observador(3)

    frase.registra_observador(obs1)
    frase.registra_observador(obs2)
    frase.registra_observador(obs3)

    frase.remove_observador(obs2)
    assert len(frase.get_clientes()) == 2

def test_frase_padrao():
    frase = Observavel.Observavel()
    obs = Observador.Observador(1)
    frase.registra_observador(obs)
    frase.set_nova_frase("Frase de Teste")
    assert (frase.palavras, frase.qnt_pares, frase.qnt_upper) == (3, 1, 2)

def test_frase_numerica():
    frase = Observavel.Observavel()
    obs = Observador.Observador(1)
    frase.registra_observador(obs)
    frase.set_nova_frase("1234 0 05 1")
    assert (frase.palavras, frase.qnt_pares, frase.qnt_upper) == (4, 2, 0)
