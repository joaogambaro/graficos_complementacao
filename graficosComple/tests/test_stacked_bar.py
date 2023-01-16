

import pytest
import itertools

# importa as funções para teste
from graficosComple.tests_funcoes_plot.f_stacked_bar import fuc_teste_sctack_bar




#-------------------------------------------------
#   Testes
#-------------------------------------------------

#Importante: a narcação do testes deve ser sempre
#"@pytest.mark.mpl_image_compare"


@pytest.mark.mpl_image_compare
def test_stacked_bar_1():

    # valores possíveis para as variáveis
    isNorm=True
    isVert=True
    tipoTexto=0
    tipoValor=None
    # gera/testa o gráfico
    return fuc_teste_sctack_bar(isNorm,isVert, tipoTexto,tipoValor)


@pytest.mark.mpl_image_compare
def test_stacked_bar_2():

    # valores possíveis para as variáveis
    isNorm=True
    isVert=True
    tipoTexto=1
    tipoValor=None

    # gera/testa o gráfico
    return fuc_teste_sctack_bar(isNorm,isVert, tipoTexto,tipoValor)



@pytest.mark.mpl_image_compare
def test_stacked_bar_3():

    # valores possíveis para as variáveis
    isNorm=True
    isVert=True
    tipoTexto=2
    tipoValor=None

    # gera/testa o gráfico
    return fuc_teste_sctack_bar(isNorm,isVert, tipoTexto,tipoValor)



@pytest.mark.mpl_image_compare
def test_stacked_bar_4():

    # valores possíveis para as variáveis
    isNorm=True
    isVert=True
    tipoTexto=3
    tipoValor=None

    # gera/testa o gráfico
    return fuc_teste_sctack_bar(isNorm,isVert, tipoTexto,tipoValor)



@pytest.mark.mpl_image_compare
def test_stacked_bar_5():

    # valores possíveis para as variáveis
    isNorm=True
    isVert=True
    tipoTexto=0
    tipoValor='num'

    # gera/testa o gráfico
    return fuc_teste_sctack_bar(isNorm,isVert, tipoTexto,tipoValor)



@pytest.mark.mpl_image_compare
def test_stacked_bar_6():

    # valores possíveis para as variáveis
    isNorm=True
    isVert=True
    tipoTexto=0
    tipoValor='porc'

    # gera/testa o gráfico
    return fuc_teste_sctack_bar(isNorm,isVert, tipoTexto,tipoValor)


@pytest.mark.mpl_image_compare
def test_stacked_bar_7():

    # valores possíveis para as variáveis
    isNorm=False
    isVert=True
    tipoTexto=3
    tipoValor=None

    # gera/testa o gráfico
    return fuc_teste_sctack_bar(isNorm,isVert, tipoTexto,tipoValor)



@pytest.mark.mpl_image_compare
def test_stacked_bar_8():

    # valores possíveis para as variáveis
    isNorm=False
    isVert=True
    tipoTexto=0
    tipoValor=None

    # gera/testa o gráfico
    return fuc_teste_sctack_bar(isNorm,isVert, tipoTexto,tipoValor)



@pytest.mark.mpl_image_compare
def test_stacked_bar_9():

    # valores possíveis para as variáveis
    isNorm=False
    isVert=False
    tipoTexto=0
    tipoValor=None

    # gera/testa o gráfico
    return fuc_teste_sctack_bar(isNorm,isVert, tipoTexto,tipoValor)



@pytest.mark.mpl_image_compare
def test_stacked_bar_10():

    # valores possíveis para as variáveis
    isNorm=False
    isVert=False
    tipoTexto=2
    tipoValor='num'

    # gera/testa o gráfico
    return fuc_teste_sctack_bar(isNorm,isVert, tipoTexto,tipoValor)


@pytest.mark.mpl_image_compare
def test_stacked_bar_11():

    # valores possíveis para as variáveis
    isNorm=False
    isVert=False
    tipoTexto=1
    tipoValor='porc'

    # gera/testa o gráfico
    return fuc_teste_sctack_bar(isNorm,isVert, tipoTexto,tipoValor)
