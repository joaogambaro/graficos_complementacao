

import pytest
import itertools

# importa as funções para teste
from graficosComple.tests_funcoes_plot.f_numeros_ext_bars import fuc_num_barras_verticais
from graficosComple.tests_funcoes_plot.f_numeros_ext_bars import fuc_porc_num_bar_verticais
from graficosComple.tests_funcoes_plot.f_numeros_ext_bars import fuc_num_barras_horizontais
from graficosComple.tests_funcoes_plot.f_numeros_ext_bars import fuc_porc_num_bar_horizontais




#-------------------------------------------------
#   Testes: para barras verticais
#-------------------------------------------------

#Importante: a narcação do testes deve ser sempre
#"@pytest.mark.mpl_image_compare"



@pytest.mark.mpl_image_compare
def test_num_barras_verticais():
    # gera/testa o gráfico
    return fuc_num_barras_verticais()


@pytest.mark.mpl_image_compare
def test_porc_num_bar_verticais_0():
    # valores possíveis para as variáveis
    org_texto=0

    #OBS: para a funcao testada so foi implementado
    # as rotinas para 'org_texto'= 0  e 1, não foram
    #implementado para 2 e 3. Fazer isto no futuro

    # gera/testa o gráfico
    return fuc_porc_num_bar_verticais(org_texto)

@pytest.mark.mpl_image_compare
def test_porc_num_bar_verticais_1():
    # valores possíveis para as variáveis
    org_texto=1
    # gera/testa o gráfico
    return fuc_porc_num_bar_verticais(org_texto)





#-------------------------------------------------
#   Testes: para barras horizontais
#-------------------------------------------------

#Importante: a narcação do testes deve ser sempre
#"@pytest.mark.mpl_image_compare"



@pytest.mark.mpl_image_compare
def test_num_barras_horizontais():
    # gera/testa o gráfico
    return fuc_num_barras_horizontais()


@pytest.mark.mpl_image_compare
def test_porc_num_bar_horizontais_0():
    # valores possíveis para as variáveis
    org_texto=0
    # gera/testa o gráfico
    return fuc_porc_num_bar_horizontais(org_texto)

@pytest.mark.mpl_image_compare
def test_porc_num_bar_horizontais_1():
    # valores possíveis para as variáveis
    org_texto=1
    # gera/testa o gráfico
    return fuc_porc_num_bar_horizontais(org_texto)

@pytest.mark.mpl_image_compare
def test_porc_num_bar_horizontais_2():
    # valores possíveis para as variáveis
    org_texto=2
    # gera/testa o gráfico
    return fuc_porc_num_bar_horizontais(org_texto)

@pytest.mark.mpl_image_compare
def test_porc_num_bar_horizontais_3():
    # valores possíveis para as variáveis
    org_texto=3
    # gera/testa o gráfico
    return fuc_porc_num_bar_horizontais(org_texto)
